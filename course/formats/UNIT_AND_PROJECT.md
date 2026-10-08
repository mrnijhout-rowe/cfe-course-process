# Unit plans, projects, and the rest: formats

The unit plan, the project spec and its side files, the larger
mini-project, and the Codio guide spec. Defaults unless marked
**[RULE]**; each cites its ledger entry.

## Unit plan

`units/NN-name/UNIT_N_PLAN.md`, one per unit, written from the
outline's unit section. Status line: PROPOSAL, or APPROVED with the
date. If the plan matches the approved outline with no departures, it
is "APPROVED with COURSE_OUTLINE.md" and the date; any departure makes
it a PROPOSAL, and the next package waits for Dan. Lesson order follows
Think Python's chapter order, and the plan names each departure and
gives its reason (DECISIONS.md, 2026-10-05). The plan proper fits about
two pages; the tables and Dan's answers follow it.

1. **Scope:** which chapters and topics are in, out, or mentioned only.
2. **Lesson table:** number, title, concept, reading due, Codio
   assignments with when each is due in lessons, quiz or check, what
   happens outside Codio. It marks each learning check and each
   mini-project day.
3. **New in this lesson:** every Python feature and every term
   introduced, lesson by lesson. Later packages may use only what this
   table has introduced, plus what earlier units taught.
4. **Peer instruction:** for each concept lesson, the bank questions
   chosen (deck and slide) or "new," two or three a lesson. Each bank
   question appears once in the unit.
5. **Learning checks:** the lessons each covers, the assignment or
   mini-project its fourth question draws on, and when that work is
   due, which is before the check.
6. **Project paragraph,** and a line saying the unit quiz comes after
   the project and when the review guide is assigned.
7. **Grading summary:** what is graded, in which category.
8. **Optional lessons:** what to drop first if time runs short, in
   order, the way a textbook marks optional sections.
9. **Final-project pointer:** at least one topic the course points at
   and does not teach (DECISIONS.md, 2026-10-05).

A unit whose containers share a frame (Unit 4) also carries the
comparison table, complete, with a note of which row each lesson adds.
A unit plan package also writes the unit's Canvas page
(STUDENT_FACING.md).

## Project spec

`assessments/PROJECT_N_Short_Name.md`, for the unit project that ends
each coding unit (DECISIONS.md, 2026-09-27 and 2026-10-05). **[RULE]**
Unit projects are graded by rubric and never autograded. The project
brings the unit's ideas together and leaves room for student choice.
It follows the plan of the fall 2026 text adventure
(sources/fall_2026_text_based_adventure/ is the model of the shape,
not the content): pairs; a written plan reviewed by another pair;
Dan's sign-off before any code; comments before code; a second pair's
review of the running program; and an individual reflection graded on
its own. Each project is written with several options, and Dan chooses
which of them a class is offered.

The spec keeps the student-facing brief, the requirements, the choice
points, the list of options, a rubric with point values (one rubric
for all options, scoring the stages and the shared requirements, rows
in the order the work happens, each scored 1 to 5), and a teacher
section: what strong, adequate, and thin submissions look like, and a
working sample solution per option, run. The things students and Dan
print are separate markdown files beside the spec, so each can become
its own Word file when Dan asks: `PROJECT_4_Handout.md`,
`PROJECT_4_Feedback_Plan.md`, `PROJECT_4_Feedback_Program.md`,
`PROJECT_4_Rubric.md`, `PROJECT_4_Run_Sheet.md`, and one brief per
option, such as `PROJECT_4_Option_A_Text_Generator.md`. The shared
handout names no option and names the unit by its topic. The project's
Canvas page, `PROJECT_N_Page.md`, is in STUDENT_FACING.md. Times follow
the text adventure's run sheet: one 50-minute day, one 90-minute day,
one 50-minute day. Project-day lesson plans are short, and so are
their decks.

## Larger mini-project

`assessments/MINI_N.N_Short_Name.md`, one to two lessons of class time
with a short rubric, counted as a small grade in the Projects category
(DECISIONS.md, 2026-10-05). Student-facing brief, requirements, choice
points, a rubric of about ten points, and a teacher section with a
commented sample solution that was run.

## Codio guide spec

`materials/CODIO_N.N_Short_Name.md`, only when the built-in course has
nothing that fits (DECISIONS.md, 2026-09-27). Page by page: the
instructions as the student sees them, starter code, expected output,
the autograder rule (output match unless the spec says otherwise), and
points. A commented reference solution at the bottom.

## Done when

- Unit plan: every item above present; the status line right; each
  bank question used once; each check's fourth question tied to work
  due before it.
- Project: every option has a run sample solution; the handout and
  page name no option; each side file stands on its own; `check`
  passes.
