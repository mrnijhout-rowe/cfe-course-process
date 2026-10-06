# CS4120: Computing for Everyone, course development process

This is the public copy of the planning repository for CS4120, an
introductory Python course at the North Carolina School of Science and
Mathematics, taught by Dan Nijhout-Rowe. It is published automatically
from a private repository on every change, so it is current.

It exists for two reasons: to share the process with other teachers,
and to be transparent with students about how AI is used to build
their course.

## What is here

- `CLAUDE.md`: the operating charter the AI model reads every session.
  It says how class runs, what every artifact must contain, and the
  voice rules.
- `DECISIONS.md`: the standing decisions ledger. It grows only at Dan's
  explicit direction.
- `course/`: course facts, the calendar grid, the course outline, and
  the build plan that turns the outline into materials.
- `units/*/UNIT_N_PLAN.md`: one plan per unit, listing lessons,
  readings, Codio slots, checks, and the project.
- `tools/`: the checking script run on plans.
- `sources/thinkpython/` and `sources/peer_instruction/`: Allen
  Downey's Think Python, 3rd edition, and a question bank drawn from
  Cynthia Taylor's CS1 peer instruction decks (via
  peerinstruction4cs.org). Both are CC BY-NC-SA 4.0 and are
  redistributed here under that license.

## What is deliberately left out

- All generated lesson material: lesson plans, reading quizzes,
  learning checks, unit quizzes, mini-projects, project specs, and
  Codio guide specs. They contain answer keys.
- `FEEDBACK.md`, Dan's notes after teaching each lesson. It is left
  out as a precaution because it is written about real classes.
- Codio's course material and the reference map built from it.
- Dan's own assessments from this and other courses, and the fall 2026
  text adventure lab, which include keys and student-facing briefs.
- The private repository's commit history. This copy is a snapshot
  per change, not a mirror of the history.

Teachers who want to see generated materials can contact Dan through
his GitHub profile, https://github.com/mrnijhout-rowe.

## How it works

The AI model proposes a unit or lesson skeleton, Dan edits or approves
it, the model writes the content, Dan teaches it and records what
happened. The division of labor and the rules the model works under
are all in `CLAUDE.md`, section 4 in particular.
