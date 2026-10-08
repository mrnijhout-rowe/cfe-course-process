# CS4120: Computing for Everyone, course development process

This is the public copy of the planning repository for CS4120, an
introductory Python course at the North Carolina School of Science and
Mathematics, taught by me, Danial Nijhout-Rowe. It is published
automatically from a private repository on every change, so it is current.

It exists for two reasons: to share the process with other teachers, and to
be transparent with students about my use of AI.

## What it is

This builds out what would have been "supplemental textbook materials" when
I first started teaching math in 2004. Back then, if I wanted to teach a
topic, for example using the quadratic formula to solve second-degree
polynomials, I would have a library of examples to choose from and extra
practice options for the students. This serves to give me those examples
to use in this class, as well as extra practice problems as needed. I
also have it do some of the "grunt work," such as creating the HTML for
Canvas LMS so that it looks good and creating the JSON that Codio
understands when I want to use assessment questions so I do not have to do
each one by hand.

## How it works

The structure of the course, units, and lessons are decided by me; the
model suggests activities that fill in the gaps, I edit or approve them,
the model writes the content, I teach it to my class and record what
happened. The division of labor and the rules the model works under are
all in `CLAUDE.md`, under "How we work" and "How class runs". What each
kind of material must contain is in `course/formats/`.

## What is deliberately left out

- All generated lesson material: lesson plans, reading quizzes, learning
  checks, unit quizzes, mini-projects, project specs, and Codio guide
  specs. They contain answer keys. One exception: lesson 4.1's plan, deck,
  and Canvas page are here as a sample of what the process produces.
- `FEEDBACK.md`, my notes after teaching each lesson. It is left out as
  a precaution because it is written about real classes.
- Codio's course material and the reference map built from it.
- My own assessments from this and other courses, and the fall 2026 text
  adventure lab, which include keys and student-facing briefs.
- My planning calendar. The materials are written in lessons, not weeks.
- `course/archive/`, the build log and my working notes behind the
  outline.
- The private repository's commit history. This copy is a snapshot per
  change, not a mirror of the history.

Teachers who want to see generated materials can contact me through my
GitHub profile: https://github.com/mrnijhout-rowe.

## What is here

- `CLAUDE.md`: the charter the AI model reads every session. It says how
  we divide the work, how class runs, the voice rules, and what to read
  for each kind of job.
- `DECISIONS.md`: the standing decisions ledger. It grows only at my
  explicit direction, and every rule in the other files cites its entry
  here by date.
- `course/COURSE.md`, the course facts; `course/COURSE_OUTLINE.md`, every
  unit and lesson; `course/BUILD_PLAN.md` and `course/packages/`, how a
  work package runs and the packages themselves; `course/formats/`, what
  each kind of material contains.
- `units/*/UNIT_N_PLAN.md`: one plan per unit, listing lessons, readings,
  Codio slots, checks, and the project. `units/04-data-structures/lessons/`
  holds the lesson 4.1 sample: `LP_4.1_String_Sequence.md`,
  `DECK_4.1_String_Sequence.md`, and `PAGE_4.1_String_Sequence.md`.
- `tools/plan_check.py`, the checking script run on every file, standard
  library only, with its manual at the top; and
  `tools/PREPARING_MATERIAL.md`, the guide to writing markdown that the
  materials pipeline can format.
- `sources/thinkpython/` and `sources/peer_instruction/`: Allen Downey's
  Think Python, 3rd edition, and a question bank drawn from Cynthia
  Taylor's CS1 peer instruction decks (via peerinstruction4cs.org). Both
  are CC BY-NC-SA 4.0 and are redistributed here under that license.
- `LICENSE`: my own content is CC BY-NC-SA 4.0 as well. `plan_check.py`
  is MIT, like the materials pipeline (`tools/LICENSE`).

## Try it in your course

Everything here is plain markdown, so you can read it on GitHub and
adapt it without any tool. To run the process the way I do, you need
Claude Code (the charter is its `CLAUDE.md` file; another tool that reads
`AGENTS.md` can use a copy under that name), Python 3 for the checking
script, and the platforms the course assumes: Codio for homework, Canvas
for the course page, Plickers for peer instruction, Thonny on student
laptops, and Python Tutor for demos. A course on different platforms
keeps the shape and changes the facts.

To make it yours:

1. Rewrite `course/COURSE.md`: your catalog description, audience,
   meeting rhythm, sources, platforms, room, and grading.
2. Replace my name in `CLAUDE.md` and `pipeline.yml`, and the room and
   habits in "How class runs" that are mine rather than yours.
3. Delete `DECISIONS.md` and start your own ledger; the rules it
   records are already stated in the charter and the format files, so
   nothing is lost. Delete `FEEDBACK.md` too.
4. Write your own `course/COURSE_OUTLINE.md` and unit plans in the
   formats given; the Unit 4 plan here is a worked example.
5. Open Claude Code at the top of the repository and say
   "Do work package U4-C in course/BUILD_PLAN.md", with your package's
   name. The session reads what `CLAUDE.md` tells it to and writes the
   materials.

The materials pipeline that turns the markdown into Word files, slides,
and Canvas pages is public too:
https://github.com/DenialGelon/materials-pipeline. The markdown stands
on its own without it.
