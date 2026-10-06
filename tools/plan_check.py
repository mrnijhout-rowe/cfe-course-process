#!/usr/bin/env python3
"""plan_check.py: checks for CS4120 lesson materials (work package T0).

Standard library only. Two commands:

    python3 tools/plan_check.py link FILE.py [--input ANSWER ...] [--md]
    python3 tools/plan_check.py check FILE.md [FILE.md or FOLDER ...] [-v]

link
    Prints the Python Tutor link that opens FILE.py (use - to read the
    program from standard input). Each --input pre-loads one answer for
    input(), in order. --md prints it as a markdown link labeled
    "Open in Python Tutor", ready to paste under the code block.

check
    For each markdown file (a folder means every .md file inside it):
    - runs every block marked `python` and compares what it prints with
      the `text` block that follows it in the same section;
    - runs every block marked `python no-run` that is followed by a
      `text` block ending in an error message, and confirms the program
      really stops with that error;
    - confirms `python` blocks use no syntax newer than Python 3.10;
    - decodes every Python Tutor link, confirms it opens exactly the
      code block above it, and confirms it is under 5,600 bytes;
    - flags every em dash;
    - flags every line inside a code block that is longer than 80
      characters, the width that fits every output of the materials
      pipeline (tools/PREPARING_MATERIAL.md);
    - in a lesson plan (LP_*.md), flags a missing or out-of-order
      section; in a learning check (CHECK_*.md), confirms four questions
      worth 2, 2, 3, and 3 points.
    The exit status is 1 if anything failed, so a package can tell at a
    glance.

Each block runs on its own, in a fresh Python process, because a
`python` block in these materials runs exactly as written (CLAUDE.md
section 6). input() is replaced by a version that prints the prompt and
the answer on one line, the way Thonny's shell shows them, so a `text`
block for an input program is pasted the way students see it.

Directives. An HTML comment directly above a code block (blank lines
between are fine) tells the checker something about that block. It does
not show when the markdown is rendered.

    <!-- plan_check input: ["Ada", "17"] -->
        Answers for input(), in order, as a JSON list of strings.
    <!-- plan_check skip: needs words.txt -->
        Do not run this block. It is listed as not verified, with the
        reason. Syntax is still checked.
    <!-- plan_check any-output: uses random -->
        Run the block and require that it finishes without an error,
        but do not compare its output.
    <!-- plan_check wide: real output, printed on one line -->
        Above a `text` block only. Its lines may be longer than 80
        characters, because they are a program's real output. The block
        is listed with a note. A long line of code is shortened instead.

Programs that import turtle or tkinter are not run, because they open
a window; the checker lists them as not verified. Programs run in a
fresh temporary folder unless --cwd names one, so a block that opens
words.txt needs --cwd pointing at a folder that holds words.txt.

Error messages differ a little between Python versions. The checker
prints which Python it ran; --python picks a different one.
"""

import argparse
import ast
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
import tokenize
import io
import urllib.parse
from pathlib import Path

TUTOR_BASE = "https://pythontutor.com/visualize.html"
TUTOR_LIMIT = 5600          # encoded bytes, from pythontutor.com's own script
LINK_LABEL = "Open in Python Tutor"
EM_DASH = "\u2014"
WIDTH_LIMIT = 80            # characters in a code-block line; tools/PREPARING_MATERIAL.md

# Lesson plan sections, in the order CLAUDE.md section 6 gives them.
LP_SECTIONS = ["Overview", "Objectives", "Preparation", "Reading", "Agenda", "Pitfalls"]
LP_OPTIONAL = ["Quick check", "Extras"]
# Agenda slots. The first slot is either a reading quiz or a learning check.
AGENDA_SLOTS = [("Reading quiz", "Learning check"), ("Concept",), ("Try it",),
                ("Partner challenge",), ("Codio",)]
AGENDA_OPTIONAL = ["Mini-project"]

CHECK_POINTS = {"A1": 2, "A2": 2, "A3": 3, "B1": 3}
CHECK_JOURNAL_LINE = "Answer in your journal. Label each answer clearly (A1, A2, A3, B1)."

# Runs one program. Replaces input() so answers come from the directive and
# echo like Thonny, and prints tracebacks without this wrapper's own frame.
RUNNER = r'''
import builtins, json, sys, traceback
program, answers = sys.argv[1], json.loads(sys.argv[2])

class NoAnswerLeft(Exception):
    pass

def scripted_input(prompt=""):
    sys.stdout.write(str(prompt))
    if not answers:
        sys.stdout.write("\n")
        raise NoAnswerLeft()
    answer = answers.pop(0)
    sys.stdout.write(answer + "\n")
    return answer

builtins.input = scripted_input
sys.argv = ["program.py"]
with open(program, encoding="utf-8") as f:
    source = f.read()
try:
    exec(compile(source, "program.py", "exec"), {"__name__": "__main__"})
except SystemExit:
    raise
except NoAnswerLeft:
    sys.stdout.flush()
    print("plan_check: input() was called but no answer is left; "
          "add a plan_check input directive above the block", file=sys.stderr)
    sys.exit(1)
except BaseException as e:
    sys.stdout.flush()
    traceback.print_exception(type(e), e, e.__traceback__.tb_next)
    sys.exit(1)
'''


# ---------------------------------------------------------------- links

def tutor_link(code, answers=()):
    """Return the Python Tutor link that opens `code` at its first step."""
    if not code.endswith("\n"):
        code += "\n"
    link = (TUTOR_BASE + "#code=" + urllib.parse.quote(code, safe="")
            + "&mode=display&py=311&curInstr=0")
    if answers:
        link += "&rawInputLstJSON=" + urllib.parse.quote(json.dumps(list(answers)), safe="")
    return link


def parse_tutor_link(url):
    """Return the link's parameters, with code and input answers decoded."""
    parts = urllib.parse.urlsplit(url)
    params = {}
    for item in parts.fragment.split("&"):
        if "=" in item:
            key, value = item.split("=", 1)
            params[key] = value
    if "code" in params:
        # unquote, not unquote_plus: the browser's decodeURIComponent keeps "+".
        params["code"] = urllib.parse.unquote(params["code"])
    if "rawInputLstJSON" in params:
        params["rawInputLstJSON"] = json.loads(urllib.parse.unquote(params["rawInputLstJSON"]))
    return parts, params


# ---------------------------------------------------------------- markdown

FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^`]*?)\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
DIRECTIVE = re.compile(r"^\s*<!--\s*plan_check\s+([\w-]+)\s*:\s*(.*?)\s*-->\s*$")
TUTOR_URL = re.compile(r"https?://(?:www\.)?pythontutor\.com/[^\s)>\]]*")
MD_LINK = re.compile(r"\[([^\]]*)\]\((https?://(?:www\.)?pythontutor\.com/[^\s)]*)\)")
ERROR_LINE = re.compile(r"^\w*(Error|Exception)(:.*)?$")


class Block:
    def __init__(self, start, info, section):
        self.start = start          # 1-based line number of the opening fence
        self.end = start
        words = info.split()
        self.lang = words[0].lower() if words else ""
        self.flags = [w.lower() for w in words[1:]]
        self.section = section      # index of the heading the block sits under
        self.lines = []
        self.directives = []        # (line number, key, value)

    @property
    def code(self):
        return "\n".join(self.lines) + "\n"

    @property
    def kind(self):
        if self.lang == "python":
            return "no-run" if "no-run" in self.flags else "python"
        return self.lang


def parse_markdown(text):
    """Split a markdown file into code blocks, headings, and prose lines.

    Returns (blocks, headings, prose) where headings is a list of
    (line, level, title) and prose is a list of (line, text) for every
    line outside a code block.
    """
    lines = text.split("\n")
    blocks, headings, prose = [], [], []
    section = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        m = FENCE_OPEN.match(line)
        if m:
            indent, fence, info = len(m.group(1)), m.group(2), m.group(3)
            block = Block(i + 1, info, section)
            block.directives = directives_above(lines, i)
            closer = re.compile(r"^\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$")
            i += 1
            while i < len(lines) and not closer.match(lines[i]):
                body = lines[i]
                # Strip the fence's own indentation (code inside a list item).
                strip = min(indent, len(body) - len(body.lstrip(" ")))
                block.lines.append(body[strip:])
                i += 1
            block.end = i + 1
            blocks.append(block)
            i += 1
            continue
        h = HEADING.match(line)
        if h:
            section += 1
            headings.append((i + 1, len(h.group(1)), h.group(2)))
        prose.append((i + 1, line))
        i += 1
    return blocks, headings, prose


def directives_above(lines, fence_index):
    found = []
    j = fence_index - 1
    while j >= 0:
        if not lines[j].strip():
            j -= 1
            continue
        m = DIRECTIVE.match(lines[j])
        if not m:
            break
        found.append((j + 1, m.group(1).lower(), m.group(2)))
        j -= 1
    return list(reversed(found))


# ---------------------------------------------------------------- running

class Report:
    def __init__(self, path, verbose):
        self.path = path
        self.verbose = verbose
        self.fails = 0
        self.unverified = []
        self.counts = {"run": 0, "matched": 0, "errors": 0, "links": 0}
        self.lines = []

    def ok(self, line, msg):
        if self.verbose:
            self.lines.append(f"  ok    line {line}: {msg}")

    def fail(self, line, msg, detail=None):
        self.fails += 1
        self.lines.append(f"  FAIL  line {line}: {msg}")
        if detail:
            self.lines.extend("        " + d for d in detail)

    def skip(self, line, msg):
        self.unverified.append(line)
        self.lines.append(f"  SKIP  line {line}: not verified, {msg}")

    def note(self, line, msg):
        self.lines.append(f"  note  line {line}: {msg}")


def run_program(code, answers, options):
    with tempfile.TemporaryDirectory() as tmp:
        program = Path(tmp) / "program.py"
        program.write_text(code, encoding="utf-8")
        runner = Path(tmp) / "plan_check_runner.py"
        runner.write_text(RUNNER, encoding="utf-8")
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
        try:
            done = subprocess.run(
                [options.python, str(runner), str(program), json.dumps(list(answers))],
                cwd=options.cwd, capture_output=True, text=True, encoding="utf-8",
                timeout=options.timeout, stdin=subprocess.DEVNULL, env=env)
        except subprocess.TimeoutExpired:
            return None
        return done


def normalize(text):
    """Lines with trailing spaces removed and trailing blank lines dropped."""
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return lines


def diff(expected, actual, labels=("text block", "actual output")):
    out = list(difflib.unified_diff(expected, actual, *labels,
                                    lineterm="", n=1))
    return out[:30] + (["..."] if len(out) > 30 else [])


def newer_syntax(code):
    """Return a message if the code uses syntax newer than Python 3.10."""
    try:
        ast.parse(code, feature_version=(3, 10))
    except SyntaxError as e:
        try:
            ast.parse(code)
        except SyntaxError:
            return None     # broken for every version; the run reports it
        return f"{e.msg} (line {e.lineno})"
    # feature_version misses one Python 3.12 change: an f-string whose
    # {} part uses the f-string's own quote mark. Python 3.10 rejects it.
    if hasattr(tokenize, "FSTRING_START"):
        quotes = []
        try:
            for tok in tokenize.generate_tokens(io.StringIO(code).readline):
                if tok.type in (tokenize.FSTRING_START, tokenize.STRING):
                    q = tok.string.lstrip("rRbBfFuU")[:3]
                    q = q if q in ('"""', "'''") else q[:1]
                    if any(q[0] == outer[0] for outer in quotes):
                        return (f"f-string reuses its own quote mark inside {{}} "
                                f"(line {tok.start[0]}); Python 3.10 rejects this")
                    if tok.type == tokenize.FSTRING_START:
                        quotes.append(q)
                elif tok.type == tokenize.FSTRING_END and quotes:
                    quotes.pop()
        except (tokenize.TokenError, SyntaxError):
            return None
    return None


WINDOW_PROGRAM = re.compile(r"^\s*(import\s+(turtle|tkinter)|from\s+(turtle|tkinter)\s+import)", re.M)


def read_directives(block, report):
    """Return (answers, skip reason, any-output reason) for a block."""
    answers, skip, any_output = [], None, None
    for line, key, value in block.directives:
        if key == "input":
            try:
                answers = json.loads(value)
                if not (isinstance(answers, list) and all(isinstance(a, str) for a in answers)):
                    raise ValueError
            except ValueError:
                report.fail(line, 'input directive must be a JSON list of strings, like ["Ada", "17"]')
                answers = []
        elif key == "skip":
            skip = value or "skip directive"
        elif key == "any-output":
            any_output = value or "any-output directive"
        elif key == "wide":
            report.fail(line, "the wide directive is for `text` blocks; shorten this code line instead")
        else:
            report.fail(line, f"unknown plan_check directive '{key}' "
                              "(use input, skip, any-output, or wide)")
    return answers, skip, any_output


def following_text_block(blocks, index):
    """The `text` block after blocks[index] in the same section, if any."""
    block = blocks[index]
    for later in blocks[index + 1:]:
        if later.section != block.section or later.kind in ("python", "no-run"):
            return None
        if later.kind == "text":
            return later
    return None


def check_python_block(blocks, index, report, options):
    block = blocks[index]
    answers, skip, any_output = read_directives(block, report)
    expected = following_text_block(blocks, index)

    problem = newer_syntax(block.code)
    if problem:
        report.fail(block.start, f"syntax newer than Python 3.10: {problem}")

    if skip:
        report.skip(block.start, skip)
        return
    if WINDOW_PROGRAM.search(block.code):
        report.skip(block.start, "turtle or tkinter program (opens a window); run it by hand")
        return

    report.counts["run"] += 1
    done = run_program(block.code, answers, options)
    if done is None:
        report.fail(block.start, f"did not finish in {options.timeout} seconds "
                                 "(an endless loop, or a program waiting for input?)")
        return
    if done.returncode != 0:
        report.fail(block.start, "python block stopped with an error "
                                 "(mark it `python no-run` if that is intended)",
                    normalize(done.stderr)[-6:])
        return
    if any_output:
        report.ok(block.start, f"ran without error; output not compared ({any_output})")
        return
    if expected is None:
        if done.stdout.strip():
            report.note(block.start, "block prints output but no `text` block follows it")
        else:
            report.ok(block.start, "ran without error")
        return
    if normalize(expected.code) == normalize(done.stdout):
        report.counts["matched"] += 1
        report.ok(block.start, f"output matches the text block at line {expected.start}")
    else:
        report.fail(block.start, f"output differs from the text block at line {expected.start}",
                    diff(normalize(expected.code), normalize(done.stdout)))


def check_no_run_block(blocks, index, report, options):
    block = blocks[index]
    answers, skip, _ = read_directives(block, report)
    expected = following_text_block(blocks, index)
    if expected is None:
        return
    shown = normalize(expected.code)
    error_lines = [i for i, line in enumerate(shown) if ERROR_LINE.match(line)]
    if not error_lines:
        report.ok(block.start, "no-run block; its text block shows no error message, not checked")
        return
    if skip:
        report.skip(block.start, skip)
        return
    report.counts["errors"] += 1
    done = run_program(block.code, answers, options)
    if done is None:
        report.fail(block.start, f"did not finish in {options.timeout} seconds")
        return
    if done.returncode == 0:
        report.fail(block.start, f"the text block at line {expected.start} shows an error, "
                                 "but the program ran without one")
        return
    actual_error = normalize(done.stderr)[-1] if done.stderr.strip() else ""
    shown_error = shown[error_lines[-1]]
    if actual_error != shown_error:
        report.fail(block.start, f"error message differs from the text block at line {expected.start}",
                    [f"shown:  {shown_error}", f"actual: {actual_error}"])
        return
    # Anything shown before the traceback is the program's own output.
    first = error_lines[-1]
    for i, line in enumerate(shown):
        if line.startswith("Traceback") or line.lstrip().startswith('File "'):
            first = i
            break
    printed = shown[:first]
    if printed and printed != normalize(done.stdout):
        report.fail(block.start, "output before the error differs from the text block",
                    diff(printed, normalize(done.stdout)))
        return
    report.ok(block.start, f"stops with the error shown at line {expected.start}")


# ---------------------------------------------------------------- links

def check_links(blocks, prose, report, is_lesson_plan):
    labels = {m.group(2): m.group(1) for _, text in prose for m in MD_LINK.finditer(text)}
    for line, text in prose:
        for m in TUTOR_URL.finditer(text):
            url = m.group(0)
            report.counts["links"] += 1
            parts, params = parse_tutor_link(url)
            problems = []
            if parts.path != "/visualize.html":
                problems.append(f"path is {parts.path}, expected /visualize.html")
            if len(url) >= TUTOR_LIMIT:
                problems.append(f"link is {len(url)} bytes; Python Tutor's limit is {TUTOR_LIMIT}")
            if params.get("mode") != "display":
                problems.append("missing mode=display")
            if params.get("py") != "311":
                problems.append("missing py=311")
            if is_lesson_plan and labels.get(url) != LINK_LABEL:
                problems.append(f'link should be labeled "{LINK_LABEL}"')

            code_block = None
            for block in blocks:
                if block.end < line and block.kind in ("python", "no-run"):
                    code_block = block
            if "code" not in params:
                problems.append("link carries no code")
            elif code_block is None:
                problems.append("no python block above this link")
            elif normalize(params["code"]) != normalize(code_block.code):
                problems.append(f"link code differs from the block at line {code_block.start}")
                problems.extend(diff(normalize(code_block.code), normalize(params["code"]),
                                     ("code block", "link")))
            else:
                answers = None
                for _, key, value in code_block.directives:
                    if key == "input":
                        try:
                            answers = json.loads(value)
                        except ValueError:
                            pass
                link_answers = params.get("rawInputLstJSON")
                if answers is not None and link_answers is not None and answers != link_answers:
                    problems.append(f"link's input answers {link_answers} differ from "
                                    f"the block's directive {answers}")
            if problems:
                report.fail(line, "Python Tutor link: " + problems[0], problems[1:])
            else:
                report.ok(line, f"Python Tutor link opens the block at line {code_block.start}")


# ---------------------------------------------------------------- format checks

def check_widths(blocks, report):
    """Flag code-block lines too long for the materials pipeline's outputs."""
    for block in blocks:
        long_lines = [(block.start + 1 + i, len(line))
                      for i, line in enumerate(block.lines) if len(line) > WIDTH_LIMIT]
        if not long_lines:
            continue
        allowed = next((value for _, key, value in block.directives if key == "wide"), None)
        if allowed is not None and block.kind not in ("python", "no-run"):
            report.note(block.start, f"{len(long_lines)} lines over {WIDTH_LIMIT} characters, "
                                     f"allowed ({allowed or 'wide directive'})")
            continue
        for line, length in long_lines:
            report.fail(line, f"line is {length} characters; the limit inside a code block "
                              f"is {WIDTH_LIMIT}")


def heading_name(title):
    """'Concept (10 min)' -> 'concept'."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", title).strip().lower()


def waived(name, text):
    """A missing section is fine when an HTML comment names it and says why."""
    return any(name.lower() in c.lower() for c in re.findall(r"<!--(.*?)-->", text, re.S))


def check_lesson_plan(path, text, headings, report):
    first = next((h for h in headings if h[1] == 1), None)
    m = re.match(r"LP_(\d+\.\d+)_", path.name)
    if first is None or not re.match(r"Lesson \d+\.\d+: \S", first[2]):
        report.fail(1, 'first heading should read "# Lesson N.N: Title"')
    elif m and not first[2].startswith(f"Lesson {m.group(1)}:"):
        report.fail(first[0], f"heading says {first[2].split(':')[0]}, file name says {m.group(1)}")

    level2 = [(line, heading_name(t)) for line, level, t in headings if level == 2]
    check_order(level2, [(s,) for s in LP_SECTIONS], "section", text, report)

    agenda = next((line for line, name in level2 if name == "agenda"), None)
    if agenda is not None:
        after = [line for line, name in level2 if line > agenda]
        agenda_end = after[0] if after else float("inf")
        level3 = [(line, heading_name(t)) for line, level, t in headings
                  if level == 3 and agenda < line < agenda_end]
        check_order(level3, AGENDA_SLOTS, "agenda slot", text, report)


def check_order(found, required, what, text, report):
    names = [name for _, name in found]
    last_pos, last_name = -1, None
    for options in required:
        hits = [i for i, n in enumerate(names) if n in (o.lower() for o in options)]
        label = " or ".join(options)
        if not hits:
            if not any(waived(o, text) for o in options):
                report.fail(1, f"lesson plan has no {what} '{label}' and no comment saying why")
            continue
        if hits[0] < last_pos:
            report.fail(found[hits[0]][0], f"{what} '{label}' comes before '{last_name}'")
        last_pos, last_name = hits[0], label
    if found:
        report.ok(found[0][0], f"{what}s present and in order")


def check_learning_check(text, prose, report):
    top = []
    for line, content in prose:
        if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", content):
            break
        top.append((line, content))
    else:
        report.fail(1, "no divider (---) between the questions and the teacher notes")

    if not any(CHECK_JOURNAL_LINE in c.replace("*", "") for _, c in top):
        report.fail(1, f'missing the line "{CHECK_JOURNAL_LINE}"')
    for part in ("Part A", "Part B"):
        if not any(part in c for _, c in top):
            report.fail(1, f"no {part} above the divider")

    question = re.compile(r"\b([AB]\d)\b[.:*\s]*\((\d+)\s*(?:points?|pts?)\)", re.I)
    found = {}
    for line, content in top:
        for m in question.finditer(content):
            label = m.group(1).upper()
            if label in found:
                report.fail(line, f"{label} appears twice")
            found[label] = (line, int(m.group(2)))
    for label, points in CHECK_POINTS.items():
        if label not in found:
            report.fail(1, f"no question {label} ({points} points) above the divider")
        elif found[label][1] != points:
            report.fail(found[label][0], f"{label} is worth {found[label][1]} points, "
                                         f"should be {points}")
    for label in found:
        if label not in CHECK_POINTS:
            report.fail(found[label][0], f"extra question {label}; a check has A1, A2, A3, B1")
    if set(found) == set(CHECK_POINTS):
        report.ok(1, "four questions, 2 + 2 + 3 + 3 points")


# ---------------------------------------------------------------- commands

def check_file(path, options):
    report = Report(path, options.verbose)
    text = path.read_text(encoding="utf-8")
    blocks, headings, prose = parse_markdown(text)

    for i, block in enumerate(blocks):
        if block.kind == "python":
            check_python_block(blocks, i, report, options)
        elif block.kind == "no-run":
            check_no_run_block(blocks, i, report, options)

    check_links(blocks, prose, report, path.name.startswith("LP_"))

    dashes = [n for n, line in enumerate(text.split("\n"), 1) if EM_DASH in line]
    for n in dashes:
        report.fail(n, "em dash")

    check_widths(blocks, report)

    if path.name.startswith("LP_"):
        check_lesson_plan(path, text, headings, report)
    if path.name.startswith("CHECK_"):
        check_learning_check(text, prose, report)

    c = report.counts
    status = "FAILED" if report.fails else "passed"
    print(f"{path}")
    for line in report.lines:
        print(line)
    print(f"  {status}: {c['run']} python blocks run, {c['matched']} outputs matched, "
          f"{c['errors']} error messages checked, {c['links']} Python Tutor links, "
          f"{len(dashes)} em dashes, {len(report.unverified)} not verified, "
          f"{report.fails} problems")
    return report.fails


def command_check(options):
    files = []
    for name in options.files:
        p = Path(name)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.exists():
            files.append(p)
        else:
            print(f"{p}: no such file")
            return 1
    version = subprocess.run([options.python, "--version"], capture_output=True, text=True)
    print(f"Running blocks with {(version.stdout or version.stderr).strip()} ({options.python})\n")

    own_tmp = None
    if options.cwd is None:
        own_tmp = tempfile.TemporaryDirectory()
        options.cwd = own_tmp.name
    try:
        failed = sum(check_file(f, options) > 0 for f in files)
    finally:
        if own_tmp:
            own_tmp.cleanup()
    print(f"\n{len(files)} files checked, {failed} with problems.")
    return 1 if failed else 0


def command_link(options):
    code = sys.stdin.read() if options.file == "-" else Path(options.file).read_text(encoding="utf-8")
    link = tutor_link(code, options.input or [])
    if len(link) >= TUTOR_LIMIT:
        print(f"Link is {len(link)} bytes; Python Tutor's limit is {TUTOR_LIMIT}. "
              "Shorten the program.", file=sys.stderr)
        return 1
    print(f"[{LINK_LABEL}]({link})" if options.md else link)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Checks for CS4120 lesson materials. See the top of this file for details.")
    commands = parser.add_subparsers(dest="command", required=True)

    link = commands.add_parser("link", help="print the Python Tutor link for a program")
    link.add_argument("file", help="the program, or - to read standard input")
    link.add_argument("--input", action="append", metavar="ANSWER",
                      help="an answer for input(); repeat for more")
    link.add_argument("--md", action="store_true",
                      help=f'print a markdown link labeled "{LINK_LABEL}"')

    check = commands.add_parser("check", help="check markdown materials")
    check.add_argument("files", nargs="+", help="markdown files or folders")
    check.add_argument("-v", "--verbose", action="store_true", help="also list what passed")
    check.add_argument("--python", default=sys.executable,
                       help="the Python that runs the blocks (default: this one)")
    check.add_argument("--cwd", help="folder the blocks run in (default: a fresh temporary one)")
    check.add_argument("--timeout", type=float, default=10, help="seconds per block (default 10)")

    options = parser.parse_args(argv)
    return command_link(options) if options.command == "link" else command_check(options)


if __name__ == "__main__":
    sys.exit(main())
