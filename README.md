# How I Build CS4120: Computing for Everyone

Hi, I'm Danial Nijhout-Rowe. I teach CS4120, Computing for Everyone, an
introductory Python course at the North Carolina School of Science and
Mathematics. This repository is a public copy of how I plan and build that
course with help from an AI model, Claude. It updates automatically
whenever I change my private copy, so what you see here is current.

I'm sharing it for two reasons. The first is for my students, who deserve
to know exactly how I'm using AI in the course they're taking. If I want
them to use AI thoughtfully, it's only fair that I show my work. The second
is for other teachers who are curious what this looks like in an actual
classroom.

Several of my students have also asked me some version of "But how do you
get beyond prompting?" This repository is my best attempt at an answer: a
look at how a professional actually works with AI, with written rules, a
clear division of labor, and a human checking everything before it reaches
a classroom.

You don't need any special software to read any of this. It's all plain
text you can read right here on GitHub.

## What it is

When I started teaching math in 2004, my textbook came with a lot more
than the textbook. There was a teacher's edition with suggested lesson
plans, a shelf of resource binders, and a box of overhead transparencies.
If I was teaching slope, I could pull a page of extra practice, a
reteaching worksheet for the students who were out that day, a word
problem about building a wheelchair ramp, and a challenge problem for the
ones who finished early. I never used all of it, but I always had
something to reach for.

An intro Python course doesn't come with any of that, so this is how I
build my own. I decide what the course covers and how the lessons fit
together. The AI fills the binder: examples to use in class, extra practice
for students who need more reps, slides, and quiz questions to check
understanding along the way. I read all of it, change what needs
changing, and toss what doesn't fit, the same as I would with any
supplemental material. The big difference is that this binder gets
written for my class, instead of my class bending to fit the binder.

That fit comes from the rules the AI works from, which describe how I
actually teach. The one I care about most is that the thinking belongs to
the students. So the materials come back built around my favorite
routines: students write in their journals before they talk, pairs work a
problem out on a whiteboard before anyone types, concept questions run as
peer instruction (vote, argue with a partner, vote again), and I live-code
the messy way, errors and all, instead of showing a polished answer. The
AI isn't here to do anyone's thinking for them. It helps me build a class
where students do more of it.

It also handles the busywork that would otherwise eat my evenings, like
formatting lesson pages so they look good in Canvas and putting quiz
questions into the file format Codio (our coding platform) needs, so
I'm not typing each one in by hand.

## How it works

The short version: I'm the teacher, and the AI is a fast, tireless
assistant who has read the textbook.

1. I decide the structure: the units, the lessons, and what each one is
   for.
2. The AI suggests activities to fill in the gaps, and I edit or approve
   them.
3. The AI writes the materials.
4. I teach the lesson to my class and write down how it went.

The AI works from a set of written rules: how we split the work, how my
class runs, even how the writing should sound. Those rules are in plain
English, and you can read them yourself (see "The nerdier stuff" below).

## What you won't find here

Most of what the AI writes stays private, mainly because a lot of it comes
with answer keys and I'd like my quizzes to stay quizzes. Specifically,
I've left out:

- The lesson materials themselves: lesson plans, reading quizzes, learning
  checks, unit quizzes, mini-projects, project instructions, and Codio
  guides. The one exception is lesson 4.1, whose lesson plan, slides, and
  Canvas page are included as a sample of what the process produces.
- My notes after teaching each lesson. They're written about real
  classes, so I keep them private as a precaution.
- Codio's own course content, which isn't mine to share.
- My other assessments, from this course and others.

If you're a teacher and would like to see more of what the process
produces, reach out through my GitHub profile:
https://github.com/mrnijhout-rowe. I'm always happy to talk shop.

---

## The nerdier stuff

Everything from here down is for folks who want to poke around the files
or run the process in their own course.

### What's in here

- `CLAUDE.md`: the charter the AI reads at the start of every session. It
  covers how we divide the work, how class runs, the voice rules, and what
  to read for each kind of job. The "How we work" and "How class runs"
  sections are the best place to start.
- `DECISIONS.md`: the standing decisions ledger. It only grows when I
  explicitly say so, and every rule in the other files cites its entry
  here by date.
- `course/COURSE.md`: the course facts.
- `course/COURSE_OUTLINE.md`: every unit and lesson.
- `course/BUILD_PLAN.md` and `course/packages/`: how a work package runs,
  and the packages themselves.
- `course/formats/`: what each kind of material has to contain.
- `units/*/UNIT_N_PLAN.md`: one plan per unit, listing lessons, readings,
  Codio slots, checks, and the project. `units/04-data-structures/lessons/`
  holds the lesson 4.1 sample: `LP_4.1_String_Sequence.md`,
  `DECK_4.1_String_Sequence.md`, and `PAGE_4.1_String_Sequence.md`.
- `tools/plan_check.py`: the checking script run on every file. Standard
  library only, with its manual at the top.
- `tools/PREPARING_MATERIAL.md`: the guide to writing markdown that the
  materials pipeline can format.
- `sources/thinkpython/`: Allen Downey's *Think Python*, 3rd edition.
- `sources/peer_instruction/`: a question bank drawn from Cynthia Taylor's
  CS1 peer instruction decks (via peerinstruction4cs.org).

Also not included, beyond the list above: `FEEDBACK.md` (my post-lesson
notes), `course/archive/` (the build log and working notes behind the
outline), the reference map I built from Codio's material, and the private
repository's commit history. This copy is a snapshot per change, not a
mirror of the history.

### Try it in your own course

Everything here is plain markdown, so you can adapt it without any tool.
To run the process the way I do, you'll need:

- Claude Code. The charter is its `CLAUDE.md` file; another tool that
  reads `AGENTS.md` can use a copy under that name.
- Python 3, for the checking script.
- The platforms the course assumes: Codio for homework, Canvas for the
  course page, Plickers for peer instruction, Thonny on student laptops,
  and Python Tutor for demos. A course on different platforms keeps the
  same shape and just changes the facts.

To make it yours:

1. Rewrite `course/COURSE.md`: your catalog description, audience,
   meeting rhythm, sources, platforms, room, and grading.
2. Replace my name in `CLAUDE.md` and `pipeline.yml`, along with the room
   and habits in "How class runs" that are mine rather than yours.
3. Delete `DECISIONS.md` and start your own ledger. The rules it records
   are already stated in the charter and the format files, so nothing is
   lost. Delete `FEEDBACK.md` too.
4. Write your own `course/COURSE_OUTLINE.md` and unit plans in the formats
   given. The Unit 4 plan here is a worked example.
5. Open Claude Code at the top of the repository and say "Do work package
   U4-C in course/BUILD_PLAN.md", using your own package's name. The
   session reads what `CLAUDE.md` tells it to and writes the materials.

The materials pipeline that turns the markdown into Word files, slides,
and Canvas pages is public too:
https://github.com/DenialGelon/materials-pipeline. The markdown stands on
its own without it.

### Licenses

- My own content is CC BY-NC-SA 4.0 (see `LICENSE`).
- *Think Python* and the peer instruction question bank are also
  CC BY-NC-SA 4.0 and are redistributed here under that license.
- `plan_check.py` is MIT, like the materials pipeline (see
  `tools/LICENSE`).
