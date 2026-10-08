# Lesson materials: formats

What a lesson package writes besides its assessments, decks, and pages:
the lesson plan, the Plickers sheet, and any Codio fix. Everything here
is a default unless marked **[RULE]**, and each rule cites the ledger
entry behind it (CLAUDE.md, "Where rules live"). Form (markdown,
frontmatter, widths) is tools/PREPARING_MATERIAL.md's; this file says
what each artifact contains.

## Naming

**[RULE]** Lessons are numbered Unit.Lesson (3.4 is Unit 3, lesson 4),
never by week or weekday (DECISIONS.md, 2026-10-05). Files sit in
`units/NN-name/`, with `UNIT_N_PLAN.md` at the top and `lessons/`,
`assessments/`, and `materials/` beside it. Keep the set of artifacts
small. Names have no spaces and are unique across the course, because
the materials pipeline names each output after its file.

| Artifact | File | Format in |
|---|---|---|
| Lesson plan | `lessons/LP_3.4_Short_Name.md` | this file |
| Deck, Canvas page | `lessons/DECK_3.4_Short_Name.md`, `lessons/PAGE_3.4_Short_Name.md`, same short name as the plan | STUDENT_FACING.md |
| Reading quiz | `assessments/QUIZ_3.4_Short_Name.md`, named by the lesson it opens | ASSESSMENTS.md |
| Learning check | `assessments/CHECK_4.6_Short_Name.md`, named by the lesson it is marked on | ASSESSMENTS.md |
| Unit quiz, review guide | `assessments/QUIZ_4_Unit_Quiz.md`, `materials/CODIO_4_Quiz_Review/` | ASSESSMENTS.md |
| Plickers sheet | `materials/PLICKERS_4_Questions.md`, one per unit | this file |
| Codio fix | `materials/CODIO_FIX_4.4_Short_Name.md`, named by the lesson that assigns the assignment, with the assignment's title as the short name; its JSON in `materials/CODIO_FIX_4.4_Assessments/` | this file |
| Codio guide spec | `materials/CODIO_3.4_Short_Name.md` | UNIT_AND_PROJECT.md |
| Larger mini-project | `assessments/MINI_2.10_Short_Name.md` | UNIT_AND_PROJECT.md |
| Project | `assessments/PROJECT_3_Short_Name.md` and its side files; `assessments/PROJECT_3_Page.md` | UNIT_AND_PROJECT.md, STUDENT_FACING.md |
| Unit plan, unit page | `UNIT_3_PLAN.md`, `PAGE_3_Unit.md` | UNIT_AND_PROJECT.md, STUDENT_FACING.md |

## Lesson plan

Sections, in this order. tools/plan_check.py `check` confirms the
heading, the sections, and the Agenda slots, and accepts a missing
section when an HTML comment names it and says why (a project day, a
quiz day). A plan has no length limit (Dan, 2026-10-06).

```markdown
# Lesson N.N: Title
## Overview          2 to 4 sentences: what students do, in order
## Objectives        "Students will be able to:" then 2 to 4 observable verbs
## Preparation       checkbox list of concrete actions
## Reading           Due today: ... / Assign tonight: ... ("nothing" is an answer)
## Agenda
### Reading quiz (5 min)       pointer to the QUIZ file; or "Learning check (10 min)"
                               with a pointer to the CHECK file; or "none today"
### Concept (10 min)           the code as typed, step by step, with what to say;
                               the peer instruction questions; Python Tutor link
### Try it (10 min)            the problem, then the key, commented
### Partner challenge (15 min) the problem, ceiling variants, then the key, commented
### Mini-project (15 min)      on the days the unit plan marks, in place of the challenge
### Codio (10 min)             which assignments, imported or authored
## Pitfalls
## Connections       optional, one or two lines
## Quick check       optional, one exit-ticket question with its answer
## Extras            spare peer instruction questions and extra variants
```

Section names and times are a starting point; the period shape is in
CLAUDE.md. Keys stay in the plan; a separate .py starter file is made
only when students need to open something. The top of the plan is what
Dan needs in the room, so spares and extra variants go under Extras.

**Preparation** lists everything Dan does before class: post the Canvas
page when the plan posts anything; put a reading quiz's Codio files in
Codio; remove each waived Codio problem, by assignment ID and problem
number; make each Codio fix; make the learning check slide; anything
students download.

**Learning check lessons.** The Agenda opens with "Learning check
(10 min)", points to the CHECK file, and says in one line what to
shorten (DECISIONS.md, 2026-10-05).

**Concept** gives the code in the order it gets typed, what to say at
each step, and the error to hit on purpose. Where the idea is about
what a program stores (assignment, a call, two names for one list), a
link labeled "Open in Python Tutor" sits directly under the code it
opens. Make every link with `python3 tools/plan_check.py link`, never
by hand; `check` confirms each one opens exactly the block above it.
Anything the deck should show is marked in the plan's text with the
words "project this": "Project this:" before it, or "(project this)"
after its heading.

**Peer instruction** (DECISIONS.md, 2026-10-05 and 2026-10-07). A
lesson that runs Plickers runs at least two questions, three where the
lesson's ideas supply them, together in one Concept step and numbered
in the order to run them. Each question has a source line ("Source:
Cynthia Taylor, `13_morelists` slide 7" or "Source: written for
CS4120"), the question, options A to D, the answer confirmed by running
the code, and one line per wrong answer saying what it catches.
Questions beyond three are spares under Extras. No bank question is
used in two lessons. `check` counts the questions and answers under
Concept.

Cynthia Taylor's bank, sources/peer_instruction/, comes first; a
question is written for this course only where the bank has none that
fits, and it is labeled so and never credited to her. Of her 183
questions, 151 have four real options plus "I don't know." Rules for
using them:

- Plickers cards carry A to D. Drop her "I don't know" option. Where
  she has five real options, cut one and say which.
- Otherwise keep her wording, code, and answer. Allowed changes: fixing
  a slide typo that sources/peer_instruction/VERIFICATION_REPORT.md
  documents, and renaming something that depends on a topic this
  course has not taught yet. Note each change in one line.
- Do not use the two questions the verification report lists as
  unresolved discrepancies. Skip questions that depend on her course's
  graphics library.
- A new question follows her pattern: a short piece of code to trace,
  or a choice among versions of a function, with each wrong answer
  produced by one specific wrong idea.

**Try it** mirrors the demo with one thing changed. **Partner
challenge** is one harder problem with ceiling variants, logic before
syntax. Both carry a commented key.

**Mini-project**, on the days the unit plan marks (DECISIONS.md,
2026-10-05): the brief as students see it, marked "project this"; two
or three options; what to look for while walking the room; one
commented sample solution that was run. A small mini-project is a
complete short program with at least one student choice, done in
class, looked at by Dan while he walks the room, and not graded: ten
to fifteen minutes early in the course, up to about twenty-five later.

**Codio.** The block names each assignment by Codio ID and title (the
IDs are explained in course/BUILD_PLAN.md, "Facts packages need"), says
what is due when, in lessons ("due 4.6"), and repeats any caveat the outline
gives for it: a page that runs ahead of class is one line telling Dan
what students will meet. Read that assignment's pages in the export
before writing the block, and do not write one without the export (it
is on Dan's laptop only; if it is missing, say so and ask). A problem
the outline waives goes in Preparation for Dan to remove. A page class
does not teach may be hidden. When a page teaches something wrong, or
asks for something class has not reached so that students cannot do
it, write a Codio fix (below); untaught material anywhere else gets a
one-line note (DECISIONS.md, 2026-10-06).

**Pitfalls:** the errors students will actually hit in this lesson,
what the message looks like, and what to say. Only this lesson's
errors, with every message pasted from a real run. **Connections**,
when they earn their place: where this idea goes later, what a CS
colleague would point out.

**Code.** A block marked `python` runs exactly as written and its
output sits under it in a `text` block, pasted from that run. A block
marked `python no-run` is a fragment or fails on purpose, with the real
error under it. Student-facing code and sample solutions use only what
the unit plan's "new in this lesson" column has introduced by that
lesson, plus what earlier units taught; a ceiling variant may go beyond
and says so. Nothing newer than Python 3.10. A line inside a code block
is 80 characters or fewer: shorten a comment or move it to its own
line, and split long code using only what the lesson has taught; real
output that cannot be shorter keeps its length under a `plan_check
wide` comment. `check` runs every block, compares every output and
error message, checks every link, and flags em dashes and long lines.
Its manual, at the top of tools/plan_check.py, has the directives for
input, for blocks that cannot run here, and for random output. Error
messages differ a little between Python versions; paste what the run
gave (Dan, 2026-10-05).

## Plickers sheet

One paste-ready sheet per unit, `materials/PLICKERS_N_Questions.md`.
Each lesson package adds its lessons' questions in lesson order,
numbered in the order the plan runs them, spares marked, word for word
as in the plan. A question is a bold label line (lesson and question
number) and then a `text` box holding the question, any code as plain
lines, and the four options on four lines, with no backticks or bold
marks inside the box. The answers are in a key at the bottom, not
beside the options, so nothing is deleted after pasting. Dan puts a
question's code into Plickers as an image, so indentation is not
checked (Dan, 2026-10-05 and 2026-10-06). `check` confirms the boxes
are plain.

## Codio fix

`materials/CODIO_FIX_N.N_Short_Name.md`, written when an imported
assignment needs changing before it is assigned (DECISIONS.md,
2026-10-06; the first one fixed U6.L5, which told students to compare
strings with `is`). In order: what is wrong and why, in a few
sentences, with page numbers from the export; a table of every page in
the assignment with its edit (none, delete, replace, or a changed
line); each replacement guide page as students see it, between
horizontal rules, followed by notes for Dan with the answers to its
challenges; each changed line, with the corrected code run; each
replacement assessment, with its source line, the question, the
answer, what each wrong answer catches, the guidance students see
after answering, and how to put it in Codio. A multiple-choice
replacement also comes as Codio's assessment JSON (JavaScript Object
Notation), made with the codio-mcq skill, in
`materials/CODIO_FIX_N.N_Assessments/`; a different kind of question,
such as a Parsons problem, is written out for Codio's assessment
editor. The lesson plan's Preparation list points at the fix.

## Done when

- `python3 tools/plan_check.py check` passes on every file written,
  and every block it lists as not verified is named in the report.
- The Codio block was written from the export's pages; every waived
  problem and every fix is in Preparation.
- The Plickers sheet has each question word for word.
- Each mini-project has its brief, its options, what to look for, and
  a sample solution that was run.
- No bank question is used twice in the unit.
