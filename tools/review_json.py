#!/usr/bin/env python3
# Copyright (c) 2026 Danial Nijhout-Rowe. MIT License; see tools/LICENSE.
"""review_json.py: makes a quiz review guide's Codio JSON files (package U4-Q).

Standard library only.

    python3 tools/review_json.py FOLDER

FOLDER is a review guide, such as
units/04-data-structures/materials/CODIO_4_Quiz_Review/. Its answers page
(the guide page whose name contains "answers") is the source: it writes out
every practice question in full. Each multiple-choice question there is a
"#### N. Title" heading followed by, in order:

    the question, with any code blocks;
    the choices, one "- " bullet each, in the order Codio gets them;
    a paragraph "Answer: ..." that repeats one choice exactly;
    a paragraph of explanation, which becomes the guidance, with
    "Answer: **...**." added at its end, as in Dan's fall 2026 guide.

Anything after the explanation (the code, run, and its output) is for
plan_check and is not copied. A "#### N." entry with no "Answer:" paragraph
is a short-answer question and is skipped; those go in SA_manual_entry.md.

For each multiple-choice question the tool writes
FOLDER/MC_Assessments/multiple-choice-ID.json, with the fields of the fall
2026 model in sources/assessments/unit_2_quiz/Codio_Review/MC_Assessments/.
A question that already has a file (matched by "Practice N:" in its name)
keeps its ten-digit task ID, and its answer IDs when the number of choices
is unchanged, so the guide pages' {Check It!|assessment} lines stay right.
A new question gets a new ID, and the tool prints the line to paste into
its guide page. Last, it lists every Check It line that names no file and
every file no Check It line names.

After running it, run `python3 tools/plan_check.py check FOLDER`, which
confirms each JSON file parses with exactly one correct answer.
"""

import json
import random
import re
import sys
import uuid
from pathlib import Path

PREFIX = "multiple-choice-"


def paragraphs(lines):
    """Split lines into blocks: code fences stay whole, prose is unwrapped."""
    blocks, prose, fence = [], [], None
    for line in lines:
        if fence is not None:
            fence.append(line)
            if line.strip().startswith("```"):
                blocks.append(("code", "\n".join(fence)))
                fence = None
            continue
        if line.strip().startswith("```"):
            if prose:
                blocks.append(("prose", prose))
                prose = []
            fence = [line]
        elif line.strip() == "":
            if prose:
                blocks.append(("prose", prose))
                prose = []
        elif line.startswith("<!--"):
            continue
        else:
            prose.append(line)
    if prose:
        blocks.append(("prose", prose))
    return blocks


def unwrap(lines):
    return " ".join(l.strip() for l in lines)


def parse_entry(n, title, body):
    blocks = paragraphs(body)
    stem, options, answer, explanation = [], None, None, None
    i = 0
    while i < len(blocks):
        kind, content = blocks[i]
        if kind == "prose" and content[0].startswith("- ") and options is None:
            options = []
            for line in content:
                if line.startswith("- "):
                    options.append(line[2:].strip())
                else:
                    options[-1] += " " + line.strip()
        elif kind == "prose" and content[0].startswith("Answer:") and options is not None:
            answer = unwrap(content)[len("Answer:"):].strip()
            if i + 1 < len(blocks) and blocks[i + 1][0] == "prose":
                explanation = unwrap(blocks[i + 1][1])
            break
        elif options is None:
            stem.append(content if kind == "code" else unwrap(content))
        i += 1
    if answer is None:
        return None
    if not options or answer not in options:
        sys.exit(f"Practice {n}: the Answer line does not repeat one of the choices exactly")
    if not explanation:
        sys.exit(f"Practice {n}: no explanation paragraph after the Answer line")
    return dict(n=n, title=title, instructions="\n\n".join(stem), options=options,
                correct=options.index(answer),
                guidance=f"{explanation} Answer: **{answer}**.")


def parse_answers_page(path):
    entries, current = [], None
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^####\s+(\d+)\.\s+(.*)$", line)
        if m:
            current = [int(m.group(1)), m.group(2).strip(), []]
            entries.append(current)
        elif line.startswith("#"):
            current = None
        elif current is not None:
            current[2].append(line)
    items = []
    for n, title, body in entries:
        item = parse_entry(n, title, body)
        if item:
            items.append(item)
    return items


def existing_files(folder):
    found = {}
    for path in folder.glob(PREFIX + "*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        m = re.match(r"Practice (\d+):", data.get("source", {}).get("name", ""))
        if m:
            found[int(m.group(1))] = data
    return found


def make_json(item, old):
    if old:
        task_id = old["taskId"]
        old_ids = [a["_id"] for a in old["source"]["answers"]]
    else:
        task_id, old_ids = None, []
    if len(old_ids) != len(item["options"]):
        old_ids = [str(uuid.uuid4()) for _ in item["options"]]
    answers = [{"_id": old_ids[i], "correct": i == item["correct"], "answer": opt}
               for i, opt in enumerate(item["options"])]
    return task_id, {
        "type": "multiple-choice",
        "taskId": task_id,
        "source": {
            "name": f"Practice {item['n']}: {item['title']}",
            "showName": True,
            "instructions": item["instructions"],
            "multipleResponse": False,
            "isRandomized": True,
            "answers": answers,
            "metadata": {
                "tags": [{"name": "Assessment Type", "value": "Multiple Choice"}],
                "files": [],
                "opened": [],
            },
            "bloomsObjectiveLevel": "",
            "learningObjectives": "",
            "guidance": item["guidance"],
            "showGuidanceAfterResponseOption": {"type": "Attempts", "passedFrom": 1},
            "maxAttemptsCount": 1,
            "showExpectedAnswerOption": {"type": "Always"},
            "points": 1,
            "incorrectPoints": 0,
            "arePartialPointsAllowed": False,
            "useMaximumScore": False,
        },
    }


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = Path(sys.argv[1])
    pages = sorted(p for p in folder.glob("*.md") if "answers" in p.name)
    if len(pages) != 1:
        sys.exit(f"{folder}: expected one answers page (a .md file with 'answers' in its name)")
    items = parse_answers_page(pages[0])
    out = folder / "MC_Assessments"
    out.mkdir(exist_ok=True)
    old = existing_files(out)
    used = {d["taskId"] for d in old.values()}

    for item in items:
        task_id, data = make_json(item, old.get(item["n"]))
        if task_id is None:
            while True:
                task_id = PREFIX + str(random.randint(1000000000, 9999999999))
                if task_id not in used:
                    break
            used.add(task_id)
            data["taskId"] = task_id
            print(f"Practice {item['n']} is new. Paste into its guide page:")
            print(f"    {{Check It!|assessment}}({task_id})")
        (out / f"{task_id}.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(items)} JSON files from {pages[0].name}")

    named = set()
    for page in sorted(folder.glob("*.md")):
        for m in re.finditer(r"\{Check It!\|assessment\}\(([^)]+)\)", page.read_text(encoding="utf-8")):
            named.add(m.group(1))
            if not (out / f"{m.group(1)}.json").exists():
                print(f"{page.name}: Check It line names {m.group(1)}, which has no file")
    current = {n for n in (i["n"] for i in items)}
    for path in sorted(out.glob(PREFIX + "*.json")):
        if path.stem not in named:
            print(f"{path.name}: no guide page names it")
        name = json.loads(path.read_text(encoding="utf-8"))["source"]["name"]
        m = re.match(r"Practice (\d+):", name)
        if m and int(m.group(1)) not in current:
            print(f"{path.name}: {name} is no longer on the answers page")


if __name__ == "__main__":
    main()
