# CLAUDE.md - CS4120 course development, second build

How this repository builds CS4120: Computing for Everyone, an
introductory Python course at the North Carolina School of Science and
Mathematics (NCSSM), taught by Dan Nijhout-Rowe. Claude writes the
materials and Dan decides. A new session with no memory of any earlier
one should be able to do a work package from these files alone.

## What to read

Every session reads this file, course/COURSE.md, course/BUILD_PLAN.md,
and the FEEDBACK.md entries for the unit it touches, if any. Then, by
package:

| Package | Also read, in this order |
|---|---|
| Lesson (U4-C and the like) | course/COURSE_OUTLINE.md, the unit's section and "Where the book and the Codio course do not line up"; your file in course/packages/; course/formats/LESSON.md, ASSESSMENTS.md, and STUDENT_FACING.md; tools/PREPARING_MATERIAL.md; then the unit plan and every lesson, deck, and page already in the unit |
| Review (R) | the outline's unit section; course/packages/R.md; all four files in course/formats/; then the files under review |
| Unit plan | course/COURSE_OUTLINE.md; your package file; course/formats/UNIT_AND_PROJECT.md and STUDENT_FACING.md; tools/PREPARING_MATERIAL.md |
| Quiz | the outline's unit section; your package file; course/formats/ASSESSMENTS.md; then every plan, quiz, and check in the unit |
| Project | the outline's unit section; your package file; course/formats/UNIT_AND_PROJECT.md and STUDENT_FACING.md; tools/PREPARING_MATERIAL.md |

Each package file names the course material it needs beyond that.

DECISIONS.md is Dan's record of every decision, dated. A rule in this
file, in course/COURSE.md, or in a format file cites the entry behind
it, as in (DECISIONS.md, 2026-10-07). Open the ledger when you want the
reason behind a cited date, when you propose changing a rule, and in
package R. It is not read front to back every session (Dan, 2026-10-08).

README.md has the layout of the repository, what was carried over from
the first build, and how outputs are made.

## How we work

- **Claude proposes, Dan decides.** Claude proposes the skeleton, a
  unit's lesson list or a lesson's, and flags anything that departs
  from a default. Dan edits or approves; disagreement is cheap here and
  expensive after generation. Claude writes the content. After Dan
  teaches it, his notes go in FEEDBACK.md, newest on top; they inform
  later proposals and become rules only when he promotes them to the
  ledger. Ask about consequential choices, decide trivia yourself, and
  when torn between two defensible approaches, propose both with a
  recommendation.
- **Where rules live.** Standing rules are in this file,
  course/COURSE.md, and course/formats/. DECISIONS.md is the dated
  record behind them. A statement marked **[RULE]** needs Dan's
  permission to deviate from. Everything else in those files is a
  default: true unless a unit plan, a lesson plan, or Dan says
  otherwise, with the deviation noted where it happens. A past plan, a
  generated artifact, a pattern that has appeared three times, or
  something said in chat creates no obligation. **[RULE]** DECISIONS.md
  grows only at Dan's explicit direction (DECISIONS.md, 2026-09-27).
- **[RULE] Content-complete markdown.** Every key, every explanation,
  every commented solution, and every quiz answer sits in the same file
  as the thing it answers. All artifacts are markdown, except a .py
  file a student opens in an editor.
- **Time estimates run tight:** minutes inside a lesson, days for a
  project, lessons for a unit. Dan stretches them in the room. Claude
  tends to badly overestimate how much time students need (DECISIONS.md,
  2026-10-05).
- **[RULE] The first build is off limits as material.** It lives in
  ../cfe_redesign. Its lesson plans, slides, pages, notebooks,
  assessments, and specs are not opened, quoted, or imitated here; its
  materials carried voice problems Dan does not want back. README.md
  lists the only things carried over. Unit 1 stays there, pointed at
  from units/01-information/README.md. If a question can only be
  answered by reading the old repository, ask Dan (DECISIONS.md,
  2026-09-27).
- **Git.** Dan drives it unless he says otherwise. Commits are the
  project record; there are no session transcripts.
- **Making outputs** (Word files, slides, Canvas HTML) is a separate
  step, taken only when Dan asks. README.md says how.
- **Work linearly.** One package per session. No subagents unless Dan
  asks for them.

## How class runs

Dan is a veteran math teacher (17 years, AP Calculus BC and AP
Statistics), now full-time computer science teacher at NCSSM, a
residential STEM magnet school. His teaching craft is strong; his CS
depth is solid and still growing. Materials hand him what a long-time
CS teacher carries in their head, the errors students will hit and
where an idea goes later, and never assume it.

**[RULE] The thinking belongs to the students.** Dan is lead learner
and facilitator. Students explain to a partner, stand at a whiteboard,
argue about a prediction, before and while they type. A period where
students only watch and then type alone has lost this. Live coding
shows the real process: reasoning aloud, hitting errors, reading
documentation, fixing things. Never present only the polished final
version.

**Journal first, then partner, then room.** Before any discussion of a
question, students think and write in the paper journal for 30 to 60
seconds, then share with an elbow partner, then the room hears a few.
Write discussion questions to survive this: concrete enough to write
about in a minute, rich enough to disagree about.

**Peer instruction.** Concept checks run as peer instruction in the
spirit of peerinstruction4cs.org, with Plickers: a multiple-choice
question whose distractors come from real misconceptions, an
individual vote, partner argument, a revote, then the reveal. It fits
the Concept block when the idea has a common wrong answer worth
surfacing. How many questions a lesson runs, where they come from, and
how a plan carries them is in course/formats/LESSON.md.

**The period.** From the first coding unit on, class is direct and
practice-heavy. A 50-minute coding lesson runs (DECISIONS.md,
2026-09-27):

1. **Reading quiz** (5 minutes) when a reading was due. On the lessons
   a unit plan marks, a
   **learning check** (10 minutes) takes its place, and the plan says
   in one line what to shorten.
2. **Concept** (10 minutes). Dan live-codes one idea, not three. The
   plan gives the code in the order it gets typed, what to say at each
   step, and the error to hit on purpose if there is one. The peer
   instruction questions run here.
3. **Try it** (10 minutes). Every student writes a short program that
   mirrors the demo with one thing changed. Individual, in Thonny.
4. **Partner challenge** (15 minutes). One harder problem for pairs.
   Logic before syntax: pairs talk it through and sketch the steps on
   the table whiteboard before either types. Ceiling variants for
   pairs that finish. On the days a unit plan marks, a mini-project
   takes this slot.
5. **Codio** (10 minutes). Students start the day's Codio work; the
   rest is homework.

Materials are written in lessons, never in weeks or dates. A 90-minute
meeting runs two lessons or one lesson plus work time; how lessons fall
on real meetings, and what to drop when time runs short, is Dan's call
in the room. This repository keeps no calendar (Dan, 2026-10-08).
course/COURSE.md has the meeting rhythm the materials are sized to.

**Discovery where the content supplies a real problem, plain
instruction where it does not.** When a concept has an organic problem
behind it, use it. When it does not, say "here is the concept" and
move to practice. A manufactured mystery, staged withholding, or teaser
is worse than a plain explanation.

**[RULE] Over-provision.** A lesson plan is a menu, not a script. Give
more try-it variants and challenge ceilings than fit, clearly marked,
so Dan can cut live. Dan skipping a component is normal use, not
feedback.

Mini-projects run from the first coding week, and each coding unit ends
with a project and then a unit quiz. What each of those is, and what
every other artifact contains, is in course/formats/.

## Voice

This governs every artifact and every chat. The first build's
materials failed in two opposite directions: first jargon and
curriculum-speak, then, when that was suppressed, coined nicknames
reused as terms, humor above a sprinkle, invented classroom moments,
dramatized machines, and teaser copy. The cure for both is the same:
say what happens, in plain sentences.

1. **Write clearly, warmly, and plainly**, in language fit for a
   school. When a literal phrase is available, use it. No mannered
   prose in either direction: no "leverage" and "scaffold," and no
   "the machine sulks" either.
2. **The reader has only the page.** Write for Dan, tired, five
   minutes before class, three months from now, without this chat.
   Anything a sentence refers to is stated in that sentence or the one
   beside it.
3. **Real names.** Products, people, and techniques go by their
   published names. Never invent a label and reuse it as a term.
4. **Describe what happens.** No teaser copy, no narrated withholding,
   no scripted reader reaction, no personified machine. Claims stay
   modest.
5. **Expand acronyms** at first use in each file. Acronyms read as
   words (ASCII) are exempt.
6. **No em dashes.** Commas, colons, semicolons, or a new sentence.
   tools/plan_check.py flags them.

Required actions (points, materials, restrictions, submission steps)
are stated explicitly enough to survive handoff. Technical substance
(code, output, formulas, attribution, licensing) stays exact through
every edit. Lesson plans talk to "you," the teacher, like a colleague
across the hall: present tense, contractions fine, short sentences.
Student-facing text follows course/formats/STUDENT_FACING.md.

## Keeping the rules small

- A new ledger entry names the failure it prevents, or says it is a
  preference, and names the one file where the rule now lives. The
  entry is not done until that file says it.
- If a program can check a rule, it goes into tools/plan_check.py and
  the prose is one line pointing at the check.
- The files every session reads (this file, course/COURSE.md,
  course/BUILD_PLAN.md, FEEDBACK.md) stay under 32 KB together.
  `python3 tools/plan_check.py budget` prints the total. Over budget,
  the next session prunes before it writes anything else.
- Every package report names any rule that got in the way and the
  lesson it hurt. Each REV package reads the format files once and
  proposes striking what no lesson in the unit used. Dan retires rules
  the way he adds them: with a dated ledger entry.
