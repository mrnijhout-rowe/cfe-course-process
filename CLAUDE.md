# CLAUDE.md - CS4120 Course Development, second build

Operating charter for AI-assisted development of CS4120: Computing for
Everyone (NCSSM, Dan Nijhout-Rowe). Read this file first, every session.
It is written for whichever model is doing the work; nothing here assumes
memory of an earlier session or an earlier model.

Read in this order: this file, DECISIONS.md, course/COURSE.md, then the
unit folder you are working in. FEEDBACK.md holds what Dan said after
teaching; read the entries for the unit you are touching.

Work linearly. Do not spawn subagents unless Dan asks for them.

## 1. How to read this repository

Every standing statement carries a tag. Untagged statements are
description, not obligation.

- **[RULE]** Always true. Deviating requires asking Dan first.
- **[DEFAULT]** True unless a unit plan, a lesson plan, or Dan says
  otherwise. Deviating is normal; note the deviation where it happens.
- **[EXAMPLE]** Illustrative only. Zero precedent weight. One example
  does not mean Dan wants more like it.
- **[OPEN]** Undecided. Do not resolve it silently; ask, or propose with
  a recommendation.

**[RULE] Standing requirements live in exactly two files: this one and
DECISIONS.md.** A past lesson plan, a generated artifact, a pattern that
has appeared three times, or something said in chat creates no
obligation. When you notice yourself inferring a recurring pattern, say
so and ask whether it belongs in the ledger. Dan decides; you do not.

**[RULE] DECISIONS.md grows only at Dan's explicit direction.** Entries
are dated, tagged, and carry a one-line rationale.

**[RULE] The previous build is off limits as material.** The first build
of this course lives in ../cfe_redesign. Its generated lesson plans,
slides, pages, notebooks, assessments, and specs are not to be opened,
quoted, or imitated when authoring here. The only things carried over
are listed in README.md. Unit 1 stays there, untouched, and
units/01-information/README.md here points at it. If a question can only
be answered by reading the old repo, ask Dan.

## 2. Who Dan is

- **[RULE]** Veteran math teacher (17 years, AP Calculus BC and AP
  Statistics lineage), now full-time computer science teacher at NCSSM,
  a residential STEM magnet school. Strong teaching craft; CS depth is
  solid and still growing. Materials should hand him what a long-time
  CS teacher carries in their head (see section 5), never assume it.
- **[RULE]** Core identity: lead learner and facilitator. The thinking
  belongs to the students, and movement and talk are how it happens:
  students explain to a partner, stand at a whiteboard, argue about a
  prediction, before and while they type. A period where students only
  watch and then type alone has lost this. Live coding shows the real
  process: reasoning aloud, hitting errors, reading documentation,
  fixing things. Never present only the polished final version.
- **[DEFAULT]** Room reality: tables with partner-size and individual
  whiteboards, several large wall whiteboards, a class set of
  micro:bits that stay in the box unless a concept genuinely lands
  better on a device. Students keep paper journals.
- **[DEFAULT] Journal first, then partner, then room.** Before any
  whole-class or partner discussion of a question, students think and
  write in the journal for 30 to 60 seconds, then share with an elbow
  partner, then the room hears a few. Write discussion questions to
  survive this: concrete enough to write about in a minute, rich enough
  to disagree about.
- **[DEFAULT] Peer instruction.** Concept checks run as peer instruction
  in the spirit of peerinstruction4cs.org, via Plickers: a
  multiple-choice question with distractors built from real
  misconceptions, individual vote, partner argument, revote, then the
  reveal. Use it in the Concept block when the idea has a common wrong
  answer worth surfacing, and give the question, the answer, and what
  each distractor catches. sources/peer_instruction/ is a bank to draw
  from: Cynthia Taylor's questions, used first (DECISIONS.md). Rules
  for using them:
  - Plickers cards carry A to D. Drop her "I don't know" option. Where
    she has five real options, cut one and say which.
  - Otherwise keep her wording, code, and answer. Allowed changes:
    fixing a slide typo that sources/peer_instruction/
    VERIFICATION_REPORT.md documents, and renaming something that
    depends on a topic this course has not taught yet. Note each change
    in one line.
  - Do not use the two questions the verification report lists as
    unresolved discrepancies. Skip questions that depend on her
    course's graphics library.
  - Each question in a plan carries a source line: her deck and slide
    number, or "written for CS4120." A new question is never credited
    to her.
  - A new question follows her pattern: a short piece of code to trace,
    or a choice among versions of a function, with each wrong answer
    produced by one specific wrong idea.

## 3. How class runs in the coding units

This is the change that motivated the second build. Unit 1 (unplugged,
readings-driven) is done and unchanged. From the first coding unit on,
class is direct and practice-heavy, and the pace is faster than the
first build planned.

**[DEFAULT] The period shape.** A 50-minute coding lesson runs:

1. **Reading quiz** (5 minutes) when a reading was due. Short, graded,
   taken in Canvas or as a Codio multiple-choice assessment (which one
   is [OPEN] in DECISIONS.md). On the lessons a unit plan marks, a
   **learning check** (DECISIONS.md) takes the first ten minutes in
   place of the reading quiz, and the plan says in one line what to
   shorten.
2. **Concept** (10 minutes). Dan live-codes one idea. One idea, not
   three. The plan gives the code in the order it gets typed, with what
   to say at each step and the error to hit on purpose if there is one.
   A peer instruction question (section 2) fits here when the idea has
   a common wrong answer.
3. **Try it** (10 minutes). Every student writes a short program that
   mirrors the demo with one thing changed. Individual, at the keyboard,
   in Thonny.
4. **Partner challenge** (15 minutes). One harder problem for pairs.
   Logic before syntax: pairs talk it through and sketch the steps on
   the table whiteboard before either of them types, then type it in
   Thonny. Ceiling variants for pairs that finish.
5. **Codio** (10 minutes). Students start the day's Codio exercises;
   the rest is homework.

A 90-minute meeting runs two lessons, or one lesson plus sustained work
time. Plans are written in 50-minute lessons and never depend on a long
block. How lessons map onto real meetings is Dan's call in the room.

**[DEFAULT] Mini-projects.** On the days a unit plan marks, a
mini-project (DECISIONS.md) takes the partner-challenge slot or the
work half of a 90-minute meeting.

**[DEFAULT] Unit quiz.** Each coding unit ends with one, after the
project (DECISIONS.md). Dan schedules it, and plans do not budget its
time.

**[DEFAULT] Discovery where the content supplies a real problem, plain
instruction where it does not.** Dan's earlier defaults (experience
before formalization, a real headache before its tool) still describe
how he prefers learning to happen when the content affords it. They are
dispositions, not per-lesson requirements. A manufactured mystery,
staged withholding, or teaser is worse than a plain explanation. When a
concept has an organic problem behind it, use it; when it does not, say
"here is the concept" and move to practice.

**[RULE] Over-provision.** A lesson plan is a menu, not a script. Give
more try-it variants and challenge ceilings than fit, clearly marked, so
Dan can cut live. Dan skipping a component is normal use, not feedback.

**[DEFAULT] Sources.** Think Python, 3rd edition, is the reading and the
source of examples. Codio's built-in course "Python Programming from
Codio" supplies imported exercises and labs; when a lesson's Codio block
can be served by importing, the plan says which exercises, and no new
guide is written. Codio guides are authored here only when the built-in
course has nothing that fits. Python Tutor (pythontutor.com) is the
default for demos about what a program stores as it runs.

**[DEFAULT] Unit projects** bring a unit's ideas together and leave room
for student choice. They are graded by rubric, never autograded. The
fall 2026 text adventure lab is the model of the shape, not of the
content. Each project is written with several options, and Dan chooses
which of them a class is offered.

## 4. Working loop

1. **Propose.** Claude proposes the unit skeleton (lesson list, one line
   each, readings, Codio slots, project idea) or the lesson skeleton.
   Flag anything that departs from a [DEFAULT].
2. **Approve.** Dan edits or approves. Disagreement is cheap here and
   expensive after generation.
3. **Author.** Content-complete markdown, with every key, every
   commented solution, and every quiz answer in the same file as the
   thing it answers.
4. **Feedback.** After Dan teaches it, his notes go in FEEDBACK.md,
   newest on top. Notes inform later proposals; they become rules only
   when Dan promotes them to DECISIONS.md.

Claude proposes structure, Dan approves it, Claude generates content.
Ask about consequential choices; decide trivia yourself; when torn
between two defensible approaches, propose both with a recommendation.

Git: Dan drives it unless he says otherwise. Commits are the project
record; there is no separate session-transcript requirement in this
build.

## 5. What every teacher-facing artifact carries

- **[RULE]** Answers and explanations for every question; commented
  code for every snippet and solution.
- **[DEFAULT]** A short **Pitfalls** list: the errors students will
  actually hit in this lesson, what the message looks like, and what to
  say. Keep it to the errors this lesson produces.
- **[DEFAULT]** One or two **Connections** lines when they earn their
  place: where this idea goes later, what a CS colleague would point out.

## 6. Artifact formats

All artifacts are markdown unless a file is meant to be opened by a
student in an editor, in which case it is a .py file. Keep the set
small. This section is the format authority; there is no separate style
guide.

**Naming.** Lessons are numbered Unit.Lesson (3.4 is Unit 3, lesson 4),
never by week. Files: `LP_3.4_Short_Name.md`, `CODIO_3.4_Short_Name.md`,
`QUIZ_3.4_Short_Name.md` (reading quiz), `CHECK_4.6_Short_Name.md`
(learning check, named by the lesson it is marked on),
`QUIZ_4_Unit_Quiz.md` (unit quiz), `MINI_2.10_Short_Name.md` (larger
mini-project), `PROJECT_3_Short_Name.md`, `UNIT_3_PLAN.md`.

**Unit plan** (`units/NN-name/UNIT_N_PLAN.md`, one per unit). Status
line (PROPOSAL or APPROVED with date). Scope: which Think Python
chapters and topics, which are in, out, or mentioned only. Lesson table:
number, title, concept, reading due, Codio block, quiz yes or no; it
also marks each learning check. For each check the plan names the
lessons it covers and the assignment its fourth question draws on.
Project paragraph, and a line saying the unit quiz comes after the
project. Grading summary. Cut points if the calendar shrinks. One to
two pages.

**Lesson plan** (`lessons/LP_N.N_Short_Name.md`). Sections, in order:

```markdown
# Lesson N.N: Title
## Overview          2-4 sentences, what students do, in order
## Objectives        "Students will be able to:" then 2-4 observable verbs
## Preparation       checkbox list, concrete actions
## Reading           Due today: ... / Assign tonight: ... ("nothing" is a real answer)
## Agenda
### Reading quiz (5 min)      pointer to the QUIZ file; or "Learning check (10 min)"
                              with a pointer to the CHECK file on the lessons the
                              unit plan marks; or "none today"
### Concept (10 min)          the code as typed, step by step, with what to say;
                              the peer instruction question; Python Tutor link
### Try it (10 min)           the problem, then the key, commented
### Partner challenge (15 min) the problem, ceiling variants, then the key, commented
### Mini-project (15 min)     optional, on days the unit plan marks
### Codio (10 min)            which exercises, imported or authored, and what is due when
## Pitfalls
## Quick check       one exit-ticket question with its answer, optional
## Extras            spare peer instruction questions and extra variants
```

The Concept section holds the peer instruction question: its source
line, the question, options A to D, the answer, and one line per wrong
answer saying what it catches. Where the outline calls for one, a link
labeled "Open in Python Tutor" sits directly under the code it opens.

The optional Mini-project section gives the brief as students see it,
marked "project this"; two or three options; what to look for while
walking the room; and one commented sample solution.

Spare peer instruction questions and extra variants go under Extras,
so the first two pages stay what Dan needs in the room.

**Code blocks.** A block marked `python` runs exactly as written. A
block marked `python no-run` is a fragment or fails on purpose, and the
real error message is shown under it. Output is shown in a block marked
`text`.

Section names and times are a starting point. Drop or rename a section
when the day is shaped differently (a project work day, a quiz day) and
leave a one-line comment saying why. Target length: two rendered pages.
Keys stay in the plan; a separate .py starter file is made only when
students need to open something.

**Reading quiz** (`assessments/QUIZ_N.N_Short_Name.md`). Three to five
questions on the assigned reading, answerable in five minutes by a
student who did the reading and not by one who did not. Mix one recall
question with questions that require having run or traced the chapter's
code. Every question is multiple choice with four options, A to D, and
exactly one correct answer. The key, below the questions, is a table:
question, answer, one-line explanation.

**Learning check** (`assessments/CHECK_N.N_Short_Name.md`). The top
half is what gets projected: the line "Answer in your journal. Label
each answer clearly (A1, A2, A3, B1)."; Part A with A1 (2 points), A2
(2 points), and A3 (3 points); Part B with B1 (3 points). Below a
divider, teacher notes: the lessons covered; for each Part A question,
the answer, the lesson where students saw it, the common miss, and how
the points split; for B1, the same plus the assignment or mini-project
it draws on; a grading budget; and a scoring line saying Part A alone
is 7 of 10. Questions and answers run to the length of the examples in
sources/assessments/learning_checks/: an answer is a value, an exact
output, a sentence or two, a few lines of code, or a quick sketch, and
a journal grades in about 90 seconds. Dan puts the questions on a
slide; the file sets no limit for that.

**Unit quiz** (`assessments/QUIZ_N_Unit_Quiz.md`), laid out like
sources/assessments/unit_2_quiz/Cumulative_Quiz_Units1-2_LLM.md: an
"About this file" block (total points, coverage, conditions, Canvas
question types), the multiple-choice questions, the short-answer
questions, an answer key table with topic and explanation, the spread
of answers across A to D, and a point-by-point rubric for each short
answer. Ten to thirteen multiple-choice questions at 2 points and two
short-answer questions at 7 points, sized for about 30 minutes.

**Quiz review guide** (folder `materials/CODIO_N_Quiz_Review/`), laid
out like sources/assessments/unit_2_quiz/Codio_Review/: numbered guide
pages of short notes followed by practice questions, an
answers-and-explanations page, `MC_Assessments/` with one JSON file per
multiple-choice practice question, and `SA_manual_entry.md` for the
short-answer practice questions.

**Codio guide spec** (`materials/CODIO_N.N_Short_Name.md`). Only when
the built-in course has nothing that fits. Page by page: instructions
as the student sees them, starter code, expected output, autograder
rule (output match unless the spec says otherwise), points. Reference
solution, commented, at the bottom.

**Larger mini-project** (`assessments/MINI_N.N_Short_Name.md`).
Student-facing brief, requirements, choice points, a rubric of about
ten points, and a teacher section with a commented sample solution.

**Project spec** (`assessments/PROJECT_N_Short_Name.md`). Student-facing
brief, requirements, choice points, rubric with point values, and a
teacher section: what strong, adequate, and thin submissions look like.
The things students and Dan print are separate markdown files beside
the spec, so each can become its own Word file later:
`PROJECT_4_Handout.md`, `PROJECT_4_Feedback_Plan.md`,
`PROJECT_4_Feedback_Program.md`, `PROJECT_4_Rubric.md`, and
`PROJECT_4_Run_Sheet.md`. Each option's brief is its own file too, such
as `PROJECT_4_Option_A_Text_Generator.md`, so Dan gives out only the
options he chose; the shared handout names no option. The spec itself,
`PROJECT_4_Short_Name.md`, keeps the requirements, the list of options,
and the teacher section with sample solutions.

**Slides.** None by default. When a concept needs a diagram or a table
on the wall, the lesson plan's Concept section includes it and marks it
"project this."

## 7. Voice

This governs every artifact and chat. It is short on purpose. The first
build's materials failed in two opposite directions: first jargon and
curriculum-speak, then, when that was suppressed, coined nicknames
reused as terms, humor above a sprinkle, invented classroom moments,
dramatized machines, and teaser copy. The cure for both is the same:
say what happens, in plain sentences.

1. **Write clearly, warmly, and plainly**, in language fit for a
   school. When a literal phrase is available, use it. No mannered
   prose in either direction: no "leverage" and "scaffold," and no
   "the machine sulks" either.
2. **The reader has only the page.** Write for Dan, tired, five minutes
   before class, three months from now, without this chat. Anything a
   sentence refers to is stated in that sentence or the one beside it.
3. **Real names.** Products, people, and techniques go by their
   published names. Never invent a label and reuse it as a term.
4. **Describe what happens.** No teaser copy, no narrated withholding,
   no scripted reader reaction, no personified machine. Claims stay
   modest. In student-facing text, the teacher appears in third person
   and any monitoring claim names the real mechanism once.
5. **Expand acronyms** at first use in each file. Acronyms read as
   words (ASCII) are exempt.
6. **No em dashes.** Commas, colons, semicolons, or a new sentence.

Required actions (due dates, points, materials, restrictions,
submission steps) are stated explicitly enough to survive handoff.
Technical substance (code, output, formulas, attribution, licensing)
stays exact through every edit.

Lesson plans talk to "you," the teacher, like a colleague across the
hall: present tense, contractions fine, short sentences. Student-facing
text uses the words students have been taught, not the words a
textbook would use.

## 8. Repo layout

```
CLAUDE.md            this file
DECISIONS.md         the ledger; grows only at Dan's direction
FEEDBACK.md          what Dan said after teaching, newest on top
README.md            what this repo is and what was carried over
course/COURSE.md     course facts: catalog, audience, meetings, grading, sources
course/CALENDAR_MAP.md   the week grid for fall 2026 and spring 2027
course/COURSE_OUTLINE.md the semester map: taught so far, and every unit and lesson ahead
course/BUILD_PLAN.md     the work packages that turn the outline into materials
sources/             Think Python notebooks, PI question bank, the school calendar
tools/               plan_check.py, the checking tool (work package T0)
units/NN-name/       UNIT_N_PLAN.md at the top; lessons/, assessments/, materials/
```
