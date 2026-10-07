# CS4120 Build Plan, second build

Status: in use. Written 2026-10-05 as a proposal and revised the same
day for Dan's answers in COURSE_OUTLINE.md. Dan answered its step 0
that day, and package S0 applied the answers. It builds what
course/COURSE_OUTLINE.md describes, which is APPROVED (2026-10-05).

This file is the list of jobs that turn the outline into finished
materials. Each job is a work package, written so that a new Claude
Opus 5.5 session with no memory of any conversation can do it from
start to finish. This file sequences work. It sets no standing rules;
those live in CLAUDE.md and DECISIONS.md.

## Where things stand (2026-10-06, after packages S0, T0, U4-PLAN, U4-A, R on U4-A, and U4-B)

- The outline is approved. Lesson materials exist for 4.1 to 4.8.
- Package S0 is done. Everything Dan approved in step 0 is now in
  DECISIONS.md and CLAUDE.md: the coding content is Units 2, 3, and 4
  with data structures as Unit 4, each unit has reading quizzes,
  learning checks, and a unit quiz, and the formats for learning
  checks, unit quizzes, review guides, mini-projects, and project
  documents are in CLAUDE.md section 6. The eight carried-over entries
  in DECISIONS.md are confirmed and dated. course/COURSE.md has the
  corrected Codio course name and the "Labs/Learning Checks" category.
- Package T0 is done. tools/plan_check.py makes Python Tutor links and
  checks finished materials; "The checking tool" under "Facts packages
  need" says how to use it.
- Package U4-PLAN is done. units/04-data-structures/UNIT_4_PLAN.md
  is APPROVED (2026-10-05) with Dan's answers recorded at its end.
  One item in it is open for U4-D: how much lighter the project's
  stages run, following Dan's FEEDBACK.md note on the text adventure.
- Package U4-A is done: lessons 4.1 to 4.4, QUIZ_4.2 and QUIZ_4.3, and
  the first questions on materials/PLICKERS_4_Questions.md. Dan's
  answers to its report are in UNIT_4_PLAN.md (`not in` at 4.2) and
  DECISIONS.md (two entries dated 2026-10-05).
- Dan's answers on 2026-10-06, already applied: the chapter 7 reading
  quiz moved from 4.1 to 4.2 (the file is now QUIZ_4.2, and
  UNIT_4_PLAN.md records the answer); a lesson plan has no length limit
  (CLAUDE.md section 6 and "Done when" no longer give one); the Codio
  U6.L5 Formative Assessment 2 check was dropped from LP_4.4 (back
  later the same day; see the next item).
- Codio fixes are a category of material (DECISIONS.md, 2026-10-06;
  format in CLAUDE.md section 6). The first is
  units/04-data-structures/materials/CODIO_FIX_4.4_String_Comparison.md:
  it deletes one U6.L5 page, replaces another, changes one line on a
  third, and has a replacement for Formative Assessment 2. Dan chose
  to keep the step that checks that question's key, and LP_4.4's
  Preparation list points at the fix.
- Package R on U4-A is done (2026-10-06), including the lesson 4.4
  Codio fix. It found the keys and answers right and made five small
  fixes: a try-it key in LP_4.1, a comment in LP_4.2, the U6.EX
  problem 4 pitfall and two Codio notes in LP_4.4, and the 4.4 peer
  instruction note in UNIT_4_PLAN.md. QUIZ_4.2 partly rewards coming
  to lesson 4.1; Dan kept it that way, and its header says so.
- Package U4-B is done (2026-10-06): lessons 4.5 to 4.8, QUIZ_4.5,
  CHECK_4.6_Strings_And_Lists, and these lessons' questions on
  materials/PLICKERS_4_Questions.md. No Codio fix was needed. The
  check's fourth question draws on U6.EX problem 5. Dan's four
  answers to its report are in UNIT_4_PLAN.md (items 8 to 11); the one
  that changed a file added a reminder about `range` with a step to
  LP_4.4's Codio section and LP_4.5's Preparation list. It has not
  been through package R.
- The materials pipeline is wired up (2026-10-06). pipeline.yml at the
  top of this repo holds the course settings, and CLAUDE.md section 6
  says how to run the makers. Turning a finished file into a Word
  file, Canvas page or deck is a separate step from writing it; a
  package does it only when Dan asks, and the output goes in
  rendered/, which git ignores. Nothing has been made for real yet;
  LP_4.1 and CHECK_4.6 were run once as a test.
- **Next:** R on U4-B, before Dan teaches from it (October 19), then
  U4-C (needed October 26).

**Open after U4-A and U4-B:**

- For Dan, before October 12: run one saved Thonny file that opens
  `words.txt` on your own laptop (LP_4.2 Preparation).
- For Dan, before assigning U6.L5 at lesson 4.4: make the edits in
  CODIO_FIX_4.4_String_Comparison.md, including the Formative
  Assessment 2 key check (LP_4.4 Preparation).
- For REV-4: UNIT_4_PLAN.md's "Fall 2026 lines" lists the 4.2 file
  setup and 4.4's `ord` and `chr` as fall-only, but spring needs both.
  LP_4.2 and LP_4.4 leave them unlabeled, and REV-4 should keep them.
  The chapter 7 quiz moved to 4.2 because 4.1 is the first class after
  fall 2026's Fall Break; REV-4 may move it back for spring.
- For Dan, before assigning U5.EX at lesson 4.7: remove problem 5.
  Before assigning U8.EX at lesson 4.8: remove problems 1 and 4 (LP_4.7
  and LP_4.8 Preparation).
- For U4-C: CHECK_4.11 may not repeat a Quick check. LP_4.6's is a
  `pop` and `append` trace, LP_4.7's is `'-'.join(sorted('cab'))`, and
  LP_4.8's is `y = x`, `y.append(3)`, `x = [0]`. `t = t.append(x)` as
  an explain-and-fix question is still unused. Lesson 4.5's partner
  challenge taught the index loop that U5.EX problem 1 needs.
- For whoever next edits tools/plan_check.py or this file: `check`
  flags the two example Python Tutor links under "Facts packages need"
  ("no python block above this link"). That predates U4-A.

## How to run a work package

Open a new session in this repository on Claude Opus 5.5 and say:

    Do work package T0 in course/BUILD_PLAN.md.

with the package's name in place of T0.

One package per session. The session reads CLAUDE.md, DECISIONS.md,
course/COURSE.md, and course/COURSE_OUTLINE.md, then "Facts packages
need" and "What every lesson package does" below, then its own
package. It works linearly and does not spawn subagents (CLAUDE.md).
It does not open ../cfe_redesign (CLAUDE.md section 1). It does not
commit unless Dan tells it to; Dan drives git. It ends with the report
described under "Report."

Packages inside a unit run in order, because each one reads the lessons
written before it. Packages from different units can run side by side.

## Step 0: what is still open

Dan answered items 0.1 to 0.5 and 0.7 on 2026-10-05, and package S0
applied them. Only 0.6 is left.

- **0.6 Speed-run tasters for fall 2026,** from the outline's list.
  Recursion is one of the six, because the catalog lists it and fall
  students have not been taught it. Dan has chosen three so far
  (recursion, classes and objects, and windows and buttons with
  tkinter). The other three, and whether recursion gets the 90-minute
  meeting, come from Dan when package U5-S runs. Sessions do not list
  this as an open item for him before then (Dan, 2026-10-06).

  Dan: recursion, basic classes/objects and gui's like tkinter are decided so far

Already answered on 2026-10-05, and recorded in
units/02-python-foundations/UNIT_2_AS_TAUGHT.md: fall students have
used `for` only over `range`, and they have watched Dan use Python
Tutor for about a week without driving it themselves. The Codio page
checks are done; the results are the outline's table "Codio pages
that run ahead of class."

## Facts packages need

**Unit numbers.** Files use one set of numbers for both semesters:
Unit 2 (chapters 1 to 4), Unit 3 (chapters 5 and 6), Unit 4 (data
structures), Unit 5 (speed run and final project). The folders are
units/02-python-foundations, units/03-decisions-and-recursion,
units/04-data-structures, and units/05-speed-run-and-final. Fall 2026
students were taught chapters 1 to 6 as one unit called Unit 2 and
have never heard of a Unit 4. Teacher-facing files use the numbers.
Student-facing text (handouts, briefs, quiz and learning check
questions, review guide pages) names a unit by its topic, such as "the
data structures project," and does not use lesson numbers, so Dan has
little to change by hand.

**Python Tutor links.** Checked against pythontutor.com's own script
on 2026-10-05. A link has this form:

    https://pythontutor.com/visualize.html#code=CODE&mode=display&py=311&curInstr=0

CODE is the program, URL-encoded. `py=311` selects Python 3.11.
`mode=display` runs the code when the page opens. `curInstr=0` starts
at the first step. Answers for `input()` can be pre-loaded by adding
`&rawInputLstJSON=` and a URL-encoded JSON list of strings. The whole
link must stay under 5,600 encoded bytes. Python Tutor does not run
turtle, does not open files, and stops long loops at a step limit, so
demo code for it is short and self-contained. Its step buttons are
labeled "Next" and "Prev" (Dan, 2026-10-06).

This example opens a four-line aliasing demo:

    https://pythontutor.com/visualize.html#code=a%20%3D%20%5B1%2C%202%2C%203%5D%0Ab%20%3D%20a%0Ab.append%284%29%0Aprint%28a%29%0A&mode=display&py=311&curInstr=0

Dan has clicked this and verified that it worked.

**The checking tool.** tools/plan_check.py (package T0, standard
library only) does two jobs. The comment at the top of the file is its
full manual.

- `python3 tools/plan_check.py link demo.py --md` prints the "Open in
  Python Tutor" line for a program, ready to paste under its code
  block. Add `--input "Ada"` once for each answer the program reads
  with `input()`. Make every link this way; never encode one by hand.
- `python3 tools/plan_check.py check FILE_OR_FOLDER` runs every
  `python` block and compares its output with the `text` block after
  it, runs each `python no-run` block that shows an error and compares
  the error line, flags syntax newer than Python 3.10, confirms each
  Python Tutor link opens the code above it, flags em dashes, flags
  each line inside a code block longer than 80 characters (CLAUDE.md
  section 6), and checks the sections of a lesson plan and the points
  of a learning check. A package runs it on every file it wrote and fixes what it
  reports before the session's report.
- Each block runs on its own. `input()` shows the prompt and the
  answer on one line, as Thonny's shell does, so a `text` block for
  an input program is pasted that way. An HTML comment directly above
  a block, invisible when rendered, tells the tool what it needs:
  `<!-- plan_check input: ["Ada", "17"] -->` gives the answers;
  `<!-- plan_check skip: reason -->` and
  `<!-- plan_check any-output: reason -->` cover a block that cannot
  run here or prints something random. Turtle and tkinter programs are
  not run, because they open a window; the session reports them as
  not verified. A block that opens `words.txt` needs `--cwd` naming a
  folder that holds the file.
- Error messages differ a little between Python versions (newer ones
  add `~~~^^^` lines under the code). That is fine: paste what the run
  gave. Dan said on 2026-10-05 that students should be comfortable
  reading error messages in different environments.

**Thonny.** Students run Thonny on their own laptops. Code in the
materials uses nothing newer than Python 3.10. Turtle programs run in
Thonny as written, with `import turtle`.

**The word list.** Think Python's `words.txt` is at
https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt.
The book describes it as a modified version of a public-domain list
from Grady Ward's Moby lexicon project. Chapter 12 uses Project
Gutenberg texts.

**Taylor's bank.** sources/peer_instruction/ has one markdown file per
topic and the same content in pi_questions.json. Of 183 multiple-choice
questions, 151 have four real options plus "I don't know."

**The Codio export.** sources/codio_course/
python-programming-from-codio.pdf is the whole course, 1,215 pages.
It is on Dan's laptop only: it is Codio's material, so .gitignore
keeps it out of git. If the file is missing, say so and ask Dan; do
not write a Codio block without it. The page numbers in
codio_course_reference.md are this file's. `pdftotext -layout` turns
it into readable text, one page per form feed. The export leaves out
the interactive widgets and a few exercise prompts; the reference
file has those prompts.

**Codio assignments can be edited.** Dan confirmed on 2026-10-05 that
an imported assignment can have a page hidden or an exercise removed.
Where the outline waives a problem, the lesson plan's Preparation list
tells Dan to remove it before assigning, by Codio ID and problem
number. Where the outline says class does not teach a page (the list
comprehensions page in U5.L1, for example), the plan says Dan may hide
it. Where a page or check needs more than hiding, because it teaches
something wrong or asks for something class has not reached so that
students cannot do it, the package writes a Codio fix (DECISIONS.md,
2026-10-06; format in
CLAUDE.md section 6). The first one is
units/04-data-structures/materials/CODIO_FIX_4.4_String_Comparison.md.

**Plickers.** Dan pastes questions into Plickers (Dan, 2026-10-05).
Each unit keeps one paste-ready sheet, `materials/
PLICKERS_4_Questions.md` for Unit 4. Each lesson package adds its
lessons' peer instruction questions to it, in lesson order, with
spares marked as spares. A question there is plain text with no
markdown marks: a line with the lesson number, the question, any code
as plain lines, then the four options on four lines. The correct
answers are in a key at the bottom of the sheet, not marked beside the
options, so nothing has to be deleted after pasting. Dan puts a
question's code into Plickers as an image taken from the markdown, so
packages don't need to check how Plickers handles indented code (Dan,
2026-10-06).

**Dan's assessment examples.** sources/assessments/ holds two models
Dan added on 2026-10-05.

- `learning_checks/` has three learning checks from Dan's Object
  Oriented Design course. They are in Java and come from another
  course: copy the shape (Part A, Part B, the point split, the teacher
  notes) and never the content. `Learning_Check_1.md` and
  `Learning_Check_3_Final.md` are complete; `Learning_Check_2.md` is
  questions only. Checks here match their length, their kind of
  answer, and their grading pace of about 90 seconds a journal. One
  thing differs: they use em dashes, and files here do not.
- `unit_2_quiz/` has the quiz Dan wrote for fall 2026 on Units 1 and 2
  and the text adventure (`Cumulative_Quiz_Units1-2_LLM.md`, a
  plain-text master for setting the quiz up in Canvas) and the Codio
  review guide that went with it (`Codio_Review/`): four guide pages
  of notes and practice, an answers page, thirteen multiple-choice
  practice questions as JSON, and four short-answer practice questions
  for manual entry. These are the models for every unit quiz and
  review guide. The practice questions parallel the quiz's questions
  without repeating them. "Unit 2" in these files is fall's name for
  what is now Units 2 and 3. The quiz also shows what fall students
  have been tested on: it has no question on return values, `while`,
  or boolean expressions.

**The fall 2026 text adventure.**
sources/fall_2026_text_based_adventure/ holds the project Dan ran in
week 7: the student handout, two feedback forms, the rubric, the run
sheet, a short lesson on handling what the player types, and example
programs. Use it for two things: what fall students have done, and
the plan every unit project follows. Two files there,
`Adventer.agents_bu.md` and `Adventure.decisions_bu.md`, are that
lab's own instructions and ledger. They governed that lab and are
history here; where they differ from this repository's CLAUDE.md,
this repository's wins. Its subfolder
Examples/sample_styled_canvas_pages/ holds two styled Canvas pages.
Dan said on 2026-10-05 that they are fair to open.

**Where fall 2026 students are.** units/02-python-foundations/
UNIT_2_AS_TAUGHT.md is the record. In short: functions with return
values, `if`/`elif`/`else`, `while`, `input()` with
`.strip().lower()`, f-strings, and `for` over `range` only. They have
watched Python Tutor and not driven it. They were not taught recursion
or turtle graphics; they met turtle only where Codio's for-loops lab
uses it.

## What every lesson package does

1. **Read.** CLAUDE.md, DECISIONS.md, course/COURSE.md, the unit's
   section of COURSE_OUTLINE.md and its "Assessments" section, the
   unit plan, FEEDBACK.md entries for the unit, every lesson already
   written in the unit, the Think Python notebooks for the chapters
   involved, the codio_course_reference.md entries for the Codio
   assignments named, and the peer instruction questions the unit plan
   assigned to these lessons. A package that writes a learning check
   also reads sources/assessments/learning_checks/.
2. **Write** each lesson plan in the CLAUDE.md section 6 format, each
   reading quiz due in these lessons, and each learning check the unit
   plan marks on these lessons, and each Codio fix these lessons'
   Codio assignments need. Add these lessons' peer instruction
   questions to the unit's Plickers sheet.
3. **Check.** Run tools/plan_check.py `check` on every file written,
   then every item under "Done when."
4. **Report.**

### Done when

- Every `python` block was run and every `text` block is pasted from
  that run. Error messages in Pitfalls are pasted from a real run, not
  remembered.
- Student-facing code and sample solutions use only what the unit
  plan's "new in this lesson" column has introduced by that lesson.
- Each peer instruction question has its source line, four options, an
  answer confirmed by running the code, and one line per wrong answer.
  No bank question is used in two lessons. The unit's Plickers sheet
  has each of these questions, word for word as in the plan.
- Each Python Tutor link was produced by tools/plan_check.py `link`,
  and `check` confirms it decodes to exactly the code block above it.
- `check` reports no problems on any file the package wrote, and every
  block it lists as not verified is named in the report.
- The Codio block names each assignment by ID and title, says what is
  due when, and repeats any caveat the outline gives for it. The
  session read that assignment's pages in the export before writing
  the block. Each waived problem is in the plan's Preparation list as
  something for Dan to remove in Codio before assigning. Each Codio
  fix is in the plan's Preparation list too, pointing at its file.
- Each mini-project has its brief, its options, what to look for, and a
  sample solution that was run.
- Each reading quiz question is multiple choice with four options and
  exactly one correct answer, and any code in it was run. The correct
  answers are spread across A to D.
- Each learning check has four questions worth 2, 2, 3, and 3 points.
  Its teacher notes name, for each Part A question, the lesson where
  students saw it, and for B1, the assignment or mini-project it draws
  on, which was due before the check. Nothing in it comes from the
  lesson it is marked on or from a later one. Its questions and
  answers are about as long as those in Dan's examples. Any code in it
  was run. No question repeats a reading quiz question, a peer
  instruction question, or a lesson's Quick check.
- The plan for a lesson with a learning check opens its Agenda with
  "Learning check (10 min)," points to the CHECK file, and says in one
  line what to shorten.
- Student-facing text names the unit by its topic and uses no lesson
  numbers.
- Voice: no em dashes, acronyms expanded at first use, no invented
  labels, no invented classroom moments (CLAUDE.md section 7).
- Spare peer instruction questions and extra variants are under
  Extras. A plan has no length limit.

### Report

The session ends by telling Dan: the files written; every departure
from a [DEFAULT] and why; anything it could not verify (for example,
turtle code it could not run because no window was available);
questions for Dan; and any pattern it noticed recurring that might
belong in the ledger.

## Work packages

| Package | Writes | Starts after | Needed by |
|---|---|---|---|
| S0 | Dan's approvals applied to the ledger, charter, course facts, outline, and this file | Dan's answers to 0.1, 0.2, and 0.5 | done 2026-10-05 |
| T0 | tools/plan_check.py | S0 | done 2026-10-05 |
| U4-PLAN | UNIT_4_PLAN.md | S0 | done 2026-10-05 |
| U4-A | lessons 4.1-4.4, two reading quizzes | U4-PLAN approved | done 2026-10-05 |
| U4-B | lessons 4.5-4.8, one reading quiz, learning check at 4.6 | U4-A | done 2026-10-06 |
| U4-C | lessons 4.9-4.12, two reading quizzes, learning check at 4.11 | U4-B | Oct 26 |
| U4-D | project spec, lessons 4.13-4.16 | U4-C | Nov 3 |
| U4-Q | Unit 4 quiz and its Codio review guide | U4-D | Nov 4 |
| R | a review of one finished package | that package | before Dan teaches from it |
| U5-S | six taster plans | 0.6 | Nov 9 |
| U5-F | final project spec | S0 | Nov 9 |
| U2-PLAN | UNIT_2_PLAN.md | S0 | Jan 2027 |
| U2-A | lessons 2.1-2.4, two reading quizzes | U2-PLAN approved | Feb 15, 2027 |
| U2-B | lessons 2.5-2.10, two reading quizzes, learning check at 2.6, turtle art spec | U2-A | Feb 22 |
| U2-Q | Unit 2 quiz and its Codio review guide | U2-B | Mar 1 |
| U3-PLAN | UNIT_3_PLAN.md | S0 | Jan 2027 |
| U3-A | lessons 3.1-3.5, two reading quizzes | U3-PLAN approved | Mar 8 |
| U3-B | lessons 3.6-3.9, one reading quiz, learning check at 3.6 | U3-A | Mar 15 |
| U3-C | project spec, lessons 3.10-3.13 | U3-B | Mar 22 |
| U3-Q | Unit 3 quiz and its Codio review guide | U3-C | Mar 22 |
| REV-4 | Unit 4 revised from fall feedback | fall FEEDBACK.md entries | Apr 5, 2027 |

The "needed by" dates are the first class day that uses the material.
A review guide is needed a few days before its quiz, so the quiz
packages are dated for the guide.

### S0: apply what Dan approved

Done 2026-10-05. It moved the approved ledger entries into
DECISIONS.md, dated the eight carried-over entries, made the approved
edits to CLAUDE.md and course/COURSE.md, marked COURSE_OUTLINE.md
approved, updated README.md, and trimmed step 0 above to the one open
item. The git history has the details.

### T0: the checking tool

Done 2026-10-05. It wrote tools/plan_check.py; "The checking tool"
under "Facts packages need" says what it does and how packages use
it. The link it makes for the four-line aliasing demo matches the one
Dan verified, byte for byte. It passed on a sample plan written for
the test and failed on a copy with one wrong output and one altered
link, flagging exactly those two. The sample files were not kept in
the repository.

### U4-PLAN: the Unit 4 plan

Done 2026-10-05, in a session with Dan rather than as a cold package,
so his answers went straight into the plan. The plan is APPROVED. Its
one open item, the project's stages, waits under "Project" for U4-D.

**Writes:** `units/04-data-structures/UNIT_4_PLAN.md`, in the CLAUDE.md
section 6 unit-plan format, from the outline's Unit 4 section.

Beyond the standard format, the plan carries six things the later
packages depend on:

1. A "new in this lesson" column: every Python feature and every term
   introduced, lesson by lesson. Later packages may use only what this
   column has introduced, plus what Units 2 and 3 taught.
2. The peer instruction assignments: for each concept lesson, the bank
   question chosen (deck and slide), one or two spares, or "new." Each
   question appears once in the unit.
3. The comparison table of strings, lists, dictionaries, and tuples,
   complete, with a note of which row each lesson adds.
4. Which fall 2026 lessons need a line or two more because of what
   UNIT_2_AS_TAUGHT.md says fall students have not seen.
5. The two learning checks, at 4.6 and 4.11: the lessons each covers,
   the assignment or mini-project its fourth question draws on, and
   when that work is due, which must be before the check.
6. The unit quiz: that it comes after lesson 4.16, that Dan schedules
   it, and when the Codio review guide is assigned.

**Status line:** if the plan matches the approved outline with no
departures, it is written as "APPROVED with COURSE_OUTLINE.md" and the
approval date. Any departure makes it a PROPOSAL, and U4-A waits for
Dan.

### U4-A: strings (lessons 4.1 to 4.4)

**Writes:** `LP_4.1` through `LP_4.4` in units/04-data-structures/
lessons/; `QUIZ_4.1` (chapter 7; moved to 4.2 as `QUIZ_4.2` on
2026-10-06) and `QUIZ_4.3` (chapter 8, through
"String methods") in assessments/.

**Specific to this package:**

- Fall students have used `for` only over `range`. Looping over a
  string directly, with no `range` and no index, is the one new idea
  in lesson 4.1, and the plan says so.
- Fall students have watched Dan step through code in Python Tutor
  for about a week and have not driven it. The 4.1 demo needs no
  introduction to the tool. The first time they step through code
  themselves is in this package, in 4.3 or earlier, so that lesson
  4.8 is not their first time.
- Codio's U6.L4 is assigned at 4.1, but its pages 324 and 328 loop
  with `while` and `word[index]`. The plan says students may stop
  there and finish after 4.3.
- Lesson 4.2 needs `words.txt` on student laptops. The plan's
  Preparation section says where the file comes from and where
  students save it so Thonny finds it.
- Fall students already put `.strip().lower()` on `input()` in the
  text adventure. Lesson 4.4 starts from those two methods and asks
  why `.lower()` did not change the original string.
- The Caesar cipher mini-project in 4.4 is written with the methods
  chapter 8 teaches. If it needs `ord` and `chr`, the plan says they
  are new and shows them.
- The Codio Unit 6 exercises read `input()` and fail if the program
  prints a prompt. That goes in Pitfalls for 4.4.

### U4-B: lists (lessons 4.5 to 4.8)

**Writes:** `LP_4.5` through `LP_4.8`; `QUIZ_4.5` (chapter 9);
`CHECK_4.6`, the learning check on lessons 4.1 to 4.5.

**Specific to this package:**

- Lesson 4.5 opens by re-running string code from 4.1 to 4.3 on a
  list, unchanged, before showing the one difference.
- Codio's U5.L1 shows list comprehensions on page 179. The 4.5 plan
  says class does not teach them and students can skip that page.
- Lesson 4.6 covers the bug `t = t.append(x)`, which leaves `t` as
  `None`. It also opens with the learning check, so its plan marks
  what to shorten.
- The learning check's fourth question draws on the work the unit plan
  named (U6.LAB, U6.EX, or the lesson 4.4 mini-project). Read that
  assignment's pages in the export and build the question on the place
  a student gets stuck doing it alone.
- Every U5.EX problem begins with `import sys` lines for the
  autograder. Pitfalls for 4.7 says students leave them alone.
  Problem 5 is waived because it needs a 2D list.
- Lesson 4.8 is the lesson Python Tutor serves best. Students drive
  it. The plan gives three links, not one.
- U8.EX is assigned at 4.8 with problem 4 waived (it needs CSV files).
  U12.EX joins it in spring; package REV-4 adds that, not this one.

### U4-C: dictionaries and tuples (lessons 4.9 to 4.12)

**Writes:** `LP_4.9` through `LP_4.12`; `QUIZ_4.9` (chapter 10) and
`QUIZ_4.12` (chapter 11, the sections lesson 4.12 uses); `CHECK_4.11`,
the learning check on lessons 4.6 to 4.10.

**Specific to this package:**

- Taylor's bank has three dictionary questions and none on tuples.
  Most questions here are new, so each one's wrong answers need extra
  care.
- Chapter 10 has a section called "Memos" that speeds up the recursive
  Fibonacci function from chapter 6 with a dictionary. Fall 2026
  students have not been taught recursion, so the 4.9 plan tells them
  to skip that section, and `QUIZ_4.9` asks nothing from it. Nothing
  else in chapters 7 to 12 needs recursion except one exercise in
  chapter 11, which is not assigned.
- Codio's U10.L1 uses tuples as dictionary keys on its hashing page.
  The 4.9 plan gives Dan one sentence to say about that.
- Codio's U10.L2 uses `for key, value in d.items()` before lesson
  4.12, and has a section on dictionary comprehensions that class does
  not teach. The 4.10 demo shows the `items()` line and ties it to
  what fall students did in the text adventure, where one call gave
  back three values to three names.
- Lesson 4.11's comparison of `in` on a list and on a dictionary is
  acted out by students first and timed on `words.txt` second. Codio's
  U10.L3 ends with the same timing. Lesson 4.11 also opens with the
  learning check, so its plan marks what to shorten.
- The learning check's fourth question draws on the work the unit plan
  named (U5.LAB, U5.EX, or U8.EX).
- Lesson 4.12 names what fall students have already written:
  `return message, health, treasure` returns a tuple.
- Codio's Unit 10 exercises wrap their tests in
  `if __name__ == "__main__":`. Pitfalls for 4.12 says what that line
  is and that students leave it alone. Problem 5 is waived because it
  needs JSON files.

### U4-D: project (lessons 4.13 to 4.16)

**Read first:** the markdown and `.py` files in
sources/fall_2026_text_based_adventure/. Skip its docx folder. It is
the plan this project follows, and fall students have just been
through it. FEEDBACK.md has Dan's note of 2026-10-05 on how it went,
and the unit plan's "Project" section says how the stages change
because of it. If that item is still marked open there, ask Dan
before writing the spec.

**Writes:** `assessments/PROJECT_4_Data_Structures.md` and `LP_4.13`
through `LP_4.16`. The project keeps the text adventure's stages,
adapted: a written plan in place of the story idea, review by another
pair, a flowchart or outline that Dan signs before any code, a work
plan, comments before code, review of the running program by another
pair, and an individual reflection graded on its own. The student
handout, both feedback forms, the rubric, the run sheet, and one brief
per option are separate markdown files beside the spec, named as the
CLAUDE.md section 6 says; Dan asks for Word versions separately
(outline answer 10). The lesson plans are short because they are
project days (CLAUDE.md section 6 allows dropping sections with a
one-line note).

**Specific to this package:**

- Dan chooses which of the three options a class is offered. All
  three are written. Each option's brief stands alone, and the shared
  handout names no option, so nothing has to be rewritten when Dan
  gives out one or two.
- One rubric serves all three options, because it scores the stages
  and the shared requirements. It keeps the text adventure's shape:
  rows in the order the work happens, each scored 1 to 5.
- Each option gets a working sample solution, run, kept in the
  teacher section.
- Times follow the text adventure's run sheet: one 50-minute day, one
  90-minute day, one 50-minute day.
- The handout and briefs say "the data structures project," with no
  unit number.

### U4-Q: Unit 4 quiz and review guide

**Read first:** every Unit 4 lesson plan, both learning checks, the
five reading quizzes, the project spec, and
sources/assessments/unit_2_quiz/ (the quiz file, every page of
Codio_Review, and two or three of the JSON files).

**Writes:** `assessments/QUIZ_4_Unit_Quiz.md` and the folder
`materials/CODIO_4_Quiz_Review/`.

**The quiz:**

- About 30 minutes of student time. Ten to thirteen multiple-choice
  questions at 2 points each and two short-answer questions at 7
  points each. If a question needs more than about eight lines of code
  to trace, the quiz has fewer questions.
- Taken in Canvas, with no notes and no running code, as the model's
  "About this file" block describes. The file keeps that block,
  including the one sentence that says how the quiz is monitored.
- About a fifth of the points come from earlier units. For fall 2026
  that share uses return values, `while`, and boolean expressions,
  which the fall quiz did not test.
- It may ask about the project. Those questions rest on what every
  option shares (the stages, reading a file, choosing between a list
  and a dictionary), because classes may have done different options.
- One short answer asks students to write a short function. The other
  asks them to explain and fix a piece of code, as the model's two do.
  Each has a point-by-point rubric.
- No question repeats a reading quiz, a learning check, or a peer
  instruction question from the unit.

**The review guide:**

- Same layout as the model: one guide page per part of the unit
  (strings; lists; dictionaries and tuples; the project), each with
  short notes and then practice questions; an answers-and-explanations
  page; `MC_Assessments/` with one JSON file per multiple-choice
  practice question; and `SA_manual_entry.md` with the short-answer
  practice questions, sample answers, and rubrics.
- Each practice question parallels a quiz question and is not the
  same question: different code, different values.
- Each JSON file copies the model's fields exactly, with its own
  ten-digit task ID and its own answer IDs.
- Guide pages are student-facing. They say "data structures," not
  "Unit 4."

**Done when:** every answer was confirmed by running the code; the
key shows the answers spread across A to D; each JSON file parses and
has exactly one correct answer; every `{Check It!|assessment}` line on
a guide page names a JSON file that exists; and the quiz and the guide
share no question.

### R: review of a finished package

**Run it** in a new session after any lesson or quiz package, naming
the package: "Do work package R on U4-A."

The reviewer did not write the materials and reads them as Dan would,
five minutes before class, with only the page. It re-runs every code
block, re-solves every peer instruction, reading quiz, learning check,
and unit quiz question before looking at the key, opens nothing from
the first build, and checks every "Done when" item. For a learning
check it also opens the lesson each Part A question cites and confirms
students saw the idea there. It fixes small errors in place and lists
what it changed. It does not rewrite a lesson's approach; it reports
that to Dan.

### U5-S: speed-run tasters

**Writes:** six plans, `LP_5.1` through `LP_5.6`, in
units/05-speed-run-and-final/lessons/, one page each: a demo, a
try-it, and where to learn more.

**Specific to this package:** in fall 2026 the recursion taster uses
Taylor's recursion questions and Codio U12.L1, and U12.EX is its
homework. It opens with the text adventure's first code pattern,
where a scene function calls itself to ask again, and tells students
that this has a name. Fall students were not taught turtle graphics,
so the recursion try-it uses no turtle; a fractal drawn with turtle
is a demo Dan runs and a pointer for final projects. A taster that
needs something installed (pygame, for example) says so in
Preparation, with the install step for Thonny.

### U5-F: final project

**Writes:** `units/05-speed-run-and-final/assessments/
PROJECT_5_Final.md`: the brief, a one-page proposal form, what "beyond
the course" means with examples drawn from each unit's final-project
pointers, checkpoints, the presentation format, the rubric, and a
teacher section.

### U2 and U3 packages: Units 2 and 3, for spring 2027

Same shape as the Unit 4 packages, from the outline's Unit 2 and
Unit 3 sections.

- **U2-PLAN and U3-PLAN** each add the same six things as U4-PLAN,
  less the comparison table and the fall 2026 notes, and list the
  departures from book order with their reasons.
- **U2-A** (2.1 to 2.4): reading quizzes for chapters 1 and 2. Lesson
  2.1 includes getting Thonny installed and a first file saved.
- **U2-B** (2.5 to 2.10): reading quizzes for chapters 3 and 4;
  `CHECK_2.6`, the learning check on lessons 2.1 to 2.5;
  `MINI_2.10_Turtle_Art.md`, which counts as a small project grade.
  Turtle code is run in a window if the session can open one.
- **U2-Q**: `QUIZ_2_Unit_Quiz.md` and `CODIO_2_Quiz_Review/`. The fall
  2026 quiz and review guide are the starting point, because most of
  their questions are on this unit already. The text adventure
  questions come out; turtle and `input()` questions go in. About a
  fifth of the points stay on Unit 1.
- **U3-A** (3.1 to 3.5): reading quizzes for chapter 5 through
  "Nested Conditionals" and chapter 6 through "Boolean functions."
  Codio's U8.L4 (at 3.4) and U8.L2 (at 3.5) both use a list on two
  pages; each plan says so in one line.
- **U3-B** (3.6 to 3.9): one reading quiz on the recursion sections
  of chapters 5 and 6; `CHECK_3.6`, the learning check on lessons 3.1
  to 3.5. Lessons 3.6 and 3.7 have no chapter behind them, so their
  plans carry a little more explanation for Dan. Lesson 3.6 teaches
  the five habits from the text adventure's lesson on handling what
  the player types, with a `while` loop doing the asking again.
- **U3-C** (3.10 to 3.13): `PROJECT_3_Text_Game.md` with the three
  options, one brief per option.
  sources/fall_2026_text_based_adventure/ is the starting point: same
  stages, same times, same rubric shape. Two things change because of
  where the project now sits: `.strip().lower()` and asking again are
  already taught in 3.6, so the short lesson inside the project
  becomes a reminder, and a scene function that calls itself can be
  called recursion.
- **U3-Q**: `QUIZ_3_Unit_Quiz.md` and `CODIO_3_Quiz_Review/`. It asks
  about the project the way the fall 2026 quiz asked about the text
  adventure. About a fifth of the points come from Units 1 and 2.

Unit 2 and Unit 3 packages should not start until Unit 4 has been
taught and FEEDBACK.md has entries from it. What Dan learns from
Unit 4 in the room will change how Units 2 and 3 are written.

### REV-4: Unit 4 for spring

**Writes:** edits to the Unit 4 files, from the fall FEEDBACK.md
entries. It removes the lines added for fall students under U4-PLAN
item 4 and the skip of chapter 10's "Memos" section, adds U12.EX at
4.8, and moves the Unit 4 quiz's earlier-unit questions onto what
spring's Units 2 and 3 taught.
