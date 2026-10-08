# CS4120 Build Plan, second build

Status: in use. Written 2026-10-05; restructured 2026-10-08 in the
governance audit; Units 2 and 3 moved ahead of the speed run the same
day (Dan). It builds what course/COURSE_OUTLINE.md describes
(APPROVED 2026-10-05) as work packages, each written so that a new
session with no memory of any conversation can do it from start to
finish. This file sequences the work and says how a package runs. What
each artifact contains is in course/formats/. Standing rules live in
CLAUDE.md, course/COURSE.md, and course/formats/; this file sets none.

The log of finished packages is course/archive/BUILD_LOG.md.
Dan's schedule, with the date each package is needed by, is his own and
is not part of the materials (Dan, 2026-10-08).

## How to run a work package

Open a new session in this repository and say:

    Do work package U4-C in course/BUILD_PLAN.md.

with the package's name in place of U4-C. One package per session. The
session reads what CLAUDE.md's "What to read" lists for its kind of
package, then its own file in course/packages/, which names the course
material it needs. It runs `python3 tools/plan_check.py budget` first;
over budget, it prunes before it writes anything else (CLAUDE.md,
"Keeping the rules small"). It works linearly, does not commit unless
Dan tells it to, and ends with the report below.

Packages inside a unit run in order, because each one reads the
lessons written before it. Packages from different units can run side
by side, except that U3-PLAN waits for U2-PLAN to be approved, since
Unit 3 lessons may use only what Unit 2's "New in this lesson" table
introduced. Units 2 and 3 are built now, before Unit 4 is taught, from
what fall 2026 taught of chapters 1 to 6 and the FEEDBACK.md entries
on it; what Dan learns in the room this fall reaches them through
REV-2 and REV-3 (Dan, 2026-10-08).

## What every lesson package does

1. **Read.** The list in CLAUDE.md, then: the unit plan; every lesson,
   deck, and page already written in the unit, so its own match them
   in form; the Think Python notebooks for the chapters involved; the
   codio_course_reference.md entries for the Codio assignments named,
   and those assignments' pages in the export; the peer instruction
   questions the unit plan assigned to these lessons. A package that
   writes a learning check also reads
   sources/assessments/learning_checks/.
2. **Write** each lesson plan, each reading quiz due in these lessons,
   each learning check the unit plan marks on them, and each Codio fix
   these lessons' assignments need, in the formats in course/formats/.
   Add these lessons' peer instruction questions to the unit's Plickers
   sheet. Then, after each plan is finished, its deck and its Canvas
   page, which copy the plan. After each reading quiz is final, its
   Codio files, made with the codio-mcq skill into rendered/codio/.
   Making Word, PowerPoint, or HTML output is not part of a package
   unless Dan asks.
3. **Check.** Run `python3 tools/plan_check.py check` on every file
   written, decks and pages included, and fix what it reports. Then go
   through the "Done when" list at the end of each format file used.
4. **Report** (below).

A unit plan package reads the outline's unit section and writes the
plan and the unit's Canvas page (course/formats/UNIT_AND_PROJECT.md and
STUDENT_FACING.md). A quiz package and a project package read what
their package files say. Package R reviews a finished package
(course/packages/R.md).

## Report

The session ends by telling Dan:

- the files written, saying for each whether it is a document, a deck,
  or a Canvas page and whether a student copy is wanted, as the
  hand-off section of tools/PREPARING_MATERIAL.md asks, so Dan can run
  the makers;
- every departure from a default and why;
- anything it could not verify (for example, turtle code it could not
  run because no window was available), and every block `check` listed
  as not verified;
- questions for Dan;
- any rule that got in the way, and the lesson it hurt (CLAUDE.md,
  "Keeping the rules small").

## Facts packages need

- **Codio IDs and the export.** Codio assignment IDs come from
  sources/codio_course/codio_course_reference.md: U6.L4 is Codio Unit
  6, lesson 4; U6.LAB is that unit's lab; U6.EX is its coding
  exercises. A "U" always means a Codio unit; this course's lessons
  are written 4.1, with no letter. The course's PDF export,
  sources/codio_course/python-programming-from-codio.pdf (1,215
  pages), is on Dan's laptop only and git-ignored; the page numbers in
  the reference file are its. `pdftotext -layout` turns it into
  readable text, one page per form feed. The export leaves out the
  interactive widgets and a few exercise prompts; the reference file
  has those prompts. An imported assignment can have a page hidden or
  an exercise removed (Dan, 2026-10-05).
- **The word list.** Think Python's `words.txt` is at
  https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt,
  a modified version of a public-domain list from Grady Ward's Moby
  lexicon project. Chapter 12 uses Project Gutenberg texts. A code
  block that opens it needs `check --cwd` naming a folder that holds
  the file.
- **Python Tutor.** Links are made and checked by tools/plan_check.py,
  whose manual has the link's anatomy. Python Tutor does not run
  turtle, does not open files, and stops long loops at a step limit,
  so demo code for it is short and self-contained. Its step buttons
  are labeled "Next" and "Prev" (Dan, 2026-10-06).
- **Taylor's bank.** sources/peer_instruction/ has one markdown file
  per topic and the same content in pi_questions.json. The rules for
  using it are in course/formats/LESSON.md.
- **Dan's models.** sources/assessments/learning_checks/ (three checks
  from his Object Oriented Design course, in Java) and
  sources/assessments/unit_2_quiz/ (the fall 2026 quiz on Units 1 and
  2 and the text adventure, with its Codio review guide) are the
  models the assessment formats name. "Unit 2" in those files is
  fall's name for what is now Units 2 and 3. The quiz has no question
  on return values, `while`, or boolean expressions.
- **The fall 2026 text adventure.**
  sources/fall_2026_text_based_adventure/ holds the project Dan ran:
  the student handout, two feedback forms, the rubric, the run sheet,
  a short lesson on handling what the player types, and example
  programs. Use it for what fall students have done and for the plan
  every unit project follows. Two files there, `Adventer.agents_bu.md`
  and `Adventure.decisions_bu.md`, are that lab's own instructions and
  ledger: history here, and where they differ from this repository's
  rules, this repository's win. Its Examples/sample_styled_canvas_pages/
  holds two styled Canvas pages, fair to open (Dan, 2026-10-05).
- **The spring 2026 Connect Four brief.**
  sources/connect_four_spring_2026/brief.md is the brief Dan ran last
  semester, the source for option B of the Unit 4 project. Its starter
  code is not in the repository. UNIT_4_PLAN.md's "Project" section
  says how the option is reshaped for this course.
- **Where fall 2026 students are.**
  units/02-python-foundations/UNIT_2_AS_TAUGHT.md is the record. In
  short: functions with return values, `if`/`elif`/`else`, `while`,
  `input()` with `.strip().lower()`, f-strings, and `for` over `range`
  only; they have watched Python Tutor and not driven it; no recursion
  or turtle, except where Codio's for-loops lab used turtle.

## Work packages

| Package | Writes | Starts after |
|---|---|---|
| U2-PLAN | UNIT_2_PLAN.md and PAGE_2_Unit.md | now |
| U2-A | lessons 2.1-2.4, two reading quizzes | U2-PLAN approved |
| U2-B | lessons 2.5-2.10, two reading quizzes, learning check at 2.6, turtle art spec | U2-A |
| U2-Q | Unit 2 quiz and its Codio review guide | U2-B |
| U3-PLAN | UNIT_3_PLAN.md and PAGE_3_Unit.md | U2-PLAN approved |
| U3-A | lessons 3.1-3.5, two reading quizzes | U3-PLAN approved |
| U3-B | lessons 3.6-3.9, one reading quiz, learning check at 3.6 | U3-A |
| U3-C | project spec, lessons 3.10-3.13 | U3-B |
| U3-Q | Unit 3 quiz and its Codio review guide | U3-C |
| R | a review of one finished package | that package |
| U5-S | six taster plans | Dan's choice of tasters |
| U5-F | final project spec | S0 (done) |
| REV-2 | Unit 2 revised from fall feedback | fall FEEDBACK.md entries |
| REV-3 | Unit 3 revised from fall feedback | fall FEEDBACK.md entries |
| REV-4 | Unit 4 revised from fall feedback | fall FEEDBACK.md entries |

Done: S0, T0, U4-PLAN, U4-A, U4-B, U4-DP, U4-C, U4-D, U4-Q, and R on
U4-A, U4-B, U4-C, and U4-D; the log has their stories. U5-S and U5-F
are independent of the Unit 2 and 3 chain and run on whatever day Dan
picks before fall needs them. Every lesson package's "Writes" entry
also means the decks, Canvas pages, and Codio quiz files for its
lessons. Each package's instructions are one file in course/packages/:
U4-D.md, U4-Q.md, R.md, U5-S.md, U5-F.md, U2.md (the four Unit 2
packages and REV-2), U3.md (the five Unit 3 packages and REV-3), and
REV-4.md.
