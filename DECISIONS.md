# DECISIONS.md - Standing Decisions Ledger

Entries are added only at Dan's explicit direction. Format:

- YYYY-MM-DD [RULE|DEFAULT|OPEN] Statement. (Rationale: one line.)

Nothing outside this file and CLAUDE.md is a standing requirement, no
matter how many times it has happened before. Superseded entries stay,
annotated, so the history reads in one place.

## Decisions from the second-build kickoff (Dan, 2026-09-27)

- 2026-09-27 [RULE] This repository is the second build of CS4120. The
  first build (../cfe_redesign) supplied only the items listed in
  README.md; its generated units, plans, slides, pages, notebooks,
  assessments, and specs are not read, quoted, or imitated here.
  (Rationale: the first build's materials carried voice problems Dan
  does not want carried forward; regenerating from scratch is cheaper
  than filtering.)
- 2026-09-27 [RULE] Unit 1 (Information) is unchanged and stays in the
  first-build repository. This repository holds a pointer only.
  (Rationale: Unit 1 taught well and is not part of the redesign.)
- 2026-09-27 [DEFAULT] Coding lessons run concept, try it, partner
  challenge, Codio exercises, with a short reading quiz at the top when
  a reading was due. Timings and the full shape are in CLAUDE.md
  section 3. (Rationale: two months of teaching showed the class needs
  more reps and a faster pace than the discovery-first plan gave it,
  especially for the basics through conditionals and loops.)
- 2026-09-27 [DEFAULT] Homework is traditional coding exercises in
  Codio guides, never notebooks. Codio's built-in "Learn to Code with
  Python" course is the first source of exercises and labs; a guide is
  authored here only when nothing in that course fits. (Rationale: the
  notebook companion cycle was slow to build and slow to run; the
  built-in course is already there.)
  *Corrected 2026-10-05: the course's name is "Python Programming from
  Codio" (Dan). See the Codio entry of that date below.*
- 2026-09-27 [RULE] Unit projects are graded by rubric and are never
  autograded. They are the open-ended, bring-it-together piece of each
  unit. (Rationale: the point of the project is student choice, which
  an autograder cannot score.)
- 2026-09-27 [DEFAULT] Reading accountability is a short quiz, three to
  five questions, at the start of the class after the reading is due.
  (Rationale: Dan's choice among quiz, journal, and peer instruction
  options; readings from Think Python continue.)
- 2026-09-27 [OPEN] Where reading quizzes are taken: paper, Canvas, or a
  Codio multiple choice assessment. Masters are written platform-neutral
  (questions plus key in markdown) until this is decided.
  *Narrowed 2026-10-05: paper is out. Reading quizzes are all multiple
  choice and are taken in Canvas or as a Codio multiple-choice
  assessment; which of the two stays open. See the reading quiz entry
  of that date below.*
  *Closed 2026-10-07: Codio. See the reading quiz entry of that date
  below.*
- 2026-09-27 [DEFAULT] Unit 3 teaches strings, lists, and dictionaries
  as one family: shared grammar once (iteration, `in`, `len`, indexing
  and slicing for the ordered ones), then each new container as "same
  rules apply, here is what is different." (Rationale: transfer;
  students should see that iterating a string and a list is the same
  move.)
  *Renumbered 2026-10-05: data structures is now Unit 4. The entry
  otherwise stands. See the unit-numbering entry of that date below.*
- 2026-09-27 [RULE] Governance is three files: CLAUDE.md (charter and
  formats), DECISIONS.md (this ledger), FEEDBACK.md (post-teaching
  notes). No per-session transcripts; git history is the record.
  (Rationale: the first build's governance outgrew its usefulness.)
- 2026-09-27 [RULE] Guiding documents are written to be self-contained
  for any model, with no reliance on chat history or earlier builds.
  Materials will be generated with Claude Opus 5.5. (Rationale: Dan's
  stated plan; the docs must brief a fresh model cold.)

## Decisions from the course-structure session (Dan, 2026-10-05)

- 2026-10-05 [RULE] Student-facing text calls Dan "Mr. Nijhout-Rowe."
  (Rationale: carried from the fall 2026 text adventure lab's own
  ledger, 2026-09-22; that is what students call him.)
- 2026-10-05 [DEFAULT] Time estimates run tight: minutes inside a
  lesson, days for a project, lessons for a unit. Dan stretches them
  in the room if needed. (Rationale: Dan's note in the text adventure
  lab's ledger, 2026-09-22: Claude tends to badly overestimate how
  much time students need.)

The rest of this session's entries were drafted in course/BUILD_PLAN.md,
step 0, and Dan approved them the same day. They are in the next
section.

## Decisions approved in the build plan's step 0 (Dan, 2026-10-05)

- 2026-10-05 [RULE] This build is the plan for spring 2027 from the
  first coding lesson. The rest of fall 2026 is built first, from the
  same structure. (Rationale: Dan, 2026-10-05; closes the open question
  about spring.)
- 2026-10-05 [RULE] The coding content is three units, numbered the
  same in both semesters: Unit 2, Python Foundations (Think Python
  chapters 1 to 4); Unit 3, Decisions and Recursion (chapters 5 and 6);
  Unit 4, Data Structures (chapters 7 to 11). Unit 5 is the speed run
  and final project. Fall 2026 taught chapters 1 to 6 as one unit
  called Unit 2, so Dan changes numbers by hand where a fall student
  would see one, and student-facing text names a unit by its topic
  where it can. (Rationale: Dan, 2026-10-05; one unit of 25 lessons was
  too long, and one set of numbers serves both semesters.)
- 2026-10-05 [DEFAULT] Lesson order follows Think Python's chapter
  order. A unit plan names each departure and gives its reason.
  (Rationale: students read the book alongside class, so the order
  should match.)
- 2026-10-05 [DEFAULT] Recursion is taught in Unit 3 after return
  values, joining the recursion sections of chapters 5 and 6. In fall
  2026 it is a speed-run taster, because the rest of chapters 5 and 6
  was taught before recursion had a place in the plan. (Rationale: book
  order, and the catalog description lists recursion; closes the open
  question.)
- 2026-10-05 [DEFAULT] Codio's course "Python Programming from Codio,"
  described in sources/codio_course/, supplies the practice for each
  new concept. COURSE_OUTLINE.md says which Codio assignment goes with
  which lesson. (Rationale: Dan, 2026-10-05; the course is already
  built and autograded.)
- 2026-10-05 [DEFAULT] Outside Codio guides, students write code in
  Thonny on their own laptops: try-its, partner challenges,
  mini-projects, and projects. (Rationale: students need practice in a
  plain editor with no guide and no autograder.)
- 2026-10-05 [DEFAULT] Mini-projects run from the first coding week. A
  small mini-project is a complete short program with at least one
  student choice, done in class, looked at by Dan while he walks the
  room, and not graded. A larger mini-project takes one to two lessons,
  has a short rubric, and counts as a small grade in the Projects
  category. (Rationale: Dan's practice in another course; building
  something is what the Codio exercises do not ask for.)
- 2026-10-05 [DEFAULT] Peer instruction questions come from Cynthia
  Taylor's bank first. A question is written for this course only where
  her bank has none that fits, and it is labeled as new. (Rationale:
  her questions are classroom-tested and their wrong answers come from
  real student errors.)
- 2026-10-05 [DEFAULT] Python Tutor is the tool for showing what a
  program stores as it runs. Lesson plans link to it for demos.
  Students use it themselves from lesson 2.7 on; in fall 2026, from
  Unit 4 on. (Rationale: Dan, 2026-10-05.)
- 2026-10-05 [DEFAULT] Unit projects follow the plan of the fall 2026
  text adventure: pairs, a written plan reviewed by another pair, Dan's
  sign-off before code, comments before code, a second review of the
  running program, and an individual reflection graded separately. Each
  project is written with several options, and Dan chooses which of
  them a class is offered. (Rationale: it ran and Dan kept it;
  CLAUDE.md already names it the model of the shape.)
- 2026-10-05 [DEFAULT] Reading quizzes are all multiple choice, four
  options and one correct answer, so they can be given in Canvas or as
  Codio multiple-choice assessments and grade themselves. Which of the
  two is used stays open. (Rationale: Dan, 2026-10-05; narrows the open
  entry of 2026-09-27 about where reading quizzes are taken.)
  *Closed 2026-10-07: Codio. See the reading quiz entry of that date
  below.*
- 2026-10-05 [DEFAULT] A learning check runs about every five or six
  class meetings. Four questions, projected, answered in the paper
  journal, which Dan collects. Ten points: three questions (2, 2, and 3
  points) that are easy for a student who was awake and took part in
  class, and one (3 points) that is easy only for a student who worked
  through a recent assignment themselves. Checks are written to the
  length and kind of answer of Dan's examples, which grade in about 90
  seconds a journal, and they count in the Labs/Learning Checks
  category. (Rationale: Dan, 2026-10-05, carried from his Object
  Oriented Design course, with examples in
  sources/assessments/learning_checks/; closes the open question about
  journal learning checks.)
- 2026-10-05 [DEFAULT] Each coding unit ends with a unit quiz, given
  after the unit's project: about 30 minutes of student time, taken in
  Canvas, multiple choice plus two short-answer questions graded by
  rubric, with about a fifth of the points from earlier units. It may
  ask about the project. A Codio review guide is built with each quiz.
  Dan schedules the quiz; lesson plans and lesson counts leave its time
  out. (Rationale: Dan, 2026-10-05; the fall 2026 quiz in
  sources/assessments/unit_2_quiz/ is the model.)

## Decisions from package U4-A (Dan, 2026-10-05)

- 2026-10-05 [DEFAULT] A reading quiz file ends with a "Code check"
  section below its key: each question's code, run, with its output or
  its error in a `text` block, so tools/plan_check.py confirms every
  answer that rests on running code. In the questions themselves, code
  that prints carries an `any-output` directive and code that fails on
  purpose is marked `python no-run`. (Rationale: package U4-A added it
  so the checker covers quiz answers, not only lesson code.)

## Decisions from the Codio fix session (Dan, 2026-10-06)

- 2026-10-06 [DEFAULT] Codio fixes are their own kind of material.
  This course assigns Codio's lessons in a different order from the
  one Codio wrote them for, so a page can depend on something class
  has not taught yet (a string method in a Functions level, for
  example) or, as in U6.L5, teach something wrong. When an assigned
  page or check needs a fix, Claude writes the replacement guide page
  in markdown and replacement assessments as needed, and the lesson
  plan's Preparation list tells Dan to make the fix before assigning.
  A replacement assessment may be a different kind of question from
  the original, such as a Parsons problem in place of a multiple-choice
  question, when that fits better. Untaught material gets a fix only
  when it makes a problem one students cannot do; anywhere else it
  gets a one-line note in the lesson plan, or the page is hidden. The
  format is in CLAUDE.md section 6. (Rationale: Dan, 2026-10-06, after
  U6.L5 told students to compare strings with `is`; on untaught
  material, "let's not stress about it unless it really makes a
  problem undoable by the students.")

## Decisions from the slides session (Dan, 2026-10-07)

- 2026-10-07 [DEFAULT] Every coding lesson has a deck, one markdown
  file beside its lesson plan, made into slides by the materials
  pipeline. The deck projects only what the lesson plan already says,
  in the slide order CLAUDE.md section 6 lists; the plan stays the
  source and the deck copies it. The quick check keeps whatever shape
  the plan gives it: four choices get the fingers-up vote, anything
  else gets its answer on the next slide or on click. (Rationale: Dan,
  2026-10-06 and 2026-10-07, after the first deck for lesson 4.1; this
  supersedes the "no slides by default" line that stood in CLAUDE.md
  from the kickoff.)
- 2026-10-07 [DEFAULT] A table that grows across lessons, such as
  Unit 4's comparison table, is projected with its full frame from the
  first lesson, empty columns included, so students copy the whole
  frame into the journal and can see that more is coming. (Rationale:
  Dan, 2026-10-07: students asked to copy a one-column table would not
  realize there is more to come.)
- 2026-10-07 [DEFAULT] A lesson that runs Plickers runs at least two
  peer instruction questions, and three where the lesson's ideas
  supply them. Not every lesson runs Plickers; one that does carries
  its two or three questions together in the plan, numbered in the
  order to run them, and the unit's Plickers sheet lists them the same
  way. Until this entry, a lesson carried one question, with spares in
  Extras. (Rationale: Dan, 2026-10-07; he generally runs Plickers in
  the warm-up part of the lesson, and when he does, "at least 2 and
  preferably 3 questions.")

## Decisions from the Canvas pages session (Dan, 2026-10-07)

- 2026-10-07 [DEFAULT] Every coding lesson has a Canvas page, one
  markdown file beside its plan and deck, made into HTML by the
  materials pipeline and pasted into Canvas by Dan before class. It
  copies the plan: what happened in class, the links the plan says to
  post, and the deck's Tonight list. A unit has a unit page and a
  project has a project page. No Canvas page says when anything is
  due, in any form; due dates live in Canvas and Codio. The format is
  in CLAUDE.md section 6. (Rationale: Dan, 2026-10-07; the Unit 4
  plans already sent students to "today's Canvas page" for links, and
  nothing authored it. Posting before class is what makes the links
  usable in class. This replaces COURSE.md's line that lesson
  materials were posted by hand after class.)
- 2026-10-07 [DEFAULT] Reading quizzes are taken in Codio as
  multiple-choice assessments. The quiz file stays the master; its
  Codio files (a guide page and one JSON file per question) are made
  from it with the codio-mcq skill into rendered/codio/, one folder
  per quiz, and remade when the quiz changes. (Rationale: Dan,
  2026-10-07; closes the open entries of 2026-09-27 and 2026-10-05,
  and supersedes his 2026-10-05 choice in COURSE_OUTLINE.md to write
  the master only and enter questions by hand.)

## Decisions from package R on U4-B (Dan, 2026-10-07)

- 2026-10-07 [DEFAULT] Dan makes the slide that projects a learning
  check himself. A lesson's deck has no learning check slide; the
  plan's Preparation list reminds him to make it. (Rationale: Dan,
  2026-10-07, after the review found DECK_4.6 had none.)
- 2026-10-07 [DEFAULT] Decks and Canvas pages may reword text that
  the lesson plan addresses to the teacher so that it speaks to
  students: "you" for the student, the words students have been
  taught. Nothing is added or changed in substance, code, values, or
  answers; a change in substance is still first a change to the plan.
  (Rationale: Dan, 2026-10-07; the 4.1 and 4.8 decks already did this,
  and the rule that every word comes from the plan did not allow it.)
- 2026-10-07 [DEFAULT] Deck titles, Canvas page titles, and their
  `unit` fields keep the spring numbering ("Lesson 4.5," "Unit 4"),
  even though fall 2026 students know the unit by another number. Dan
  changes them by hand where he wants to. (Rationale: Dan, 2026-10-07;
  one set of numbers serves both semesters, as in the 2026-10-05
  unit-numbering entry.)

## Carried over from the first build

Dan confirmed these eight as written on 2026-10-05.

- 2026-10-05 [RULE] The semester's last ~12 meeting days are reserved:
  ~6 for a speed run of taster topics (Dan picks each semester), then ~6
  for student final-project work. Presentations finish by the last full
  week; the final-exam period is not used. (Rationale: standing rule in
  the first build; confirmed by Dan.)
- 2026-10-05 [RULE] Lessons are numbered Unit.Lesson (3.4 = Unit 3,
  lesson 4), never by week or weekday. (Rationale: standing rule in the
  first build; confirmed by Dan.)
- 2026-10-05 [RULE] Plans are denominated in 50-minute lessons and never
  depend on a long block. Budget: 13 to 14 lessons per three weeks,
  leaving one or two meetings of slack. (Rationale: standing rule in the
  first build; confirmed by Dan.)
- 2026-10-05 [RULE] Think Python is source material, not the syllabus.
  Topics start out and enter only by explicit curation in the unit plan.
  (Rationale: standing rule in the first build; confirmed by Dan.)
- 2026-10-05 [RULE] Students have standing access to the course Gemini
  Gem on every assignment, all semester. It is never granted or revoked
  per assignment. (Rationale: standing rule in the first build;
  confirmed by Dan.)
- 2026-10-05 [RULE] The learning-check calibration governs every
  assessment: a student who was merely present earns a passing but
  mediocre score; a student who genuinely did the work earns full credit
  easily. The easiest path to an A must be honest work, not delegating
  the work to an AI. (Rationale: standing rule in the first build;
  confirmed by Dan.)
- 2026-10-05 [DEFAULT] Difficulty: single-step, hand-held problems are
  not an assessment tier. Graded problem sets open with one to three
  warm-ups that are multi-step with a little help or single-step with
  none, then lead with multi-step problems where the method is not
  given. (Rationale: standing rule in the first build; confirmed by
  Dan.)
- 2026-10-05 [DEFAULT] Each unit names at least one final-project
  pointer: a topic the course points at but does not teach, so students
  accumulate project ideas all semester. (Rationale: standing rule in
  the first build; confirmed by Dan.)

## Open questions not yet on the ledger

Dan closed all three on 2026-10-05. His answers stay under each
question, with the entry that closes it.

- Do the weekly journal learning checks continue alongside reading
  quizzes, or do reading quizzes replace them as the weekly points?
  - yes, learning checks every 5-6 lessons
  - *Closed 2026-10-05 by the learning check entry above. Reading
    quizzes and learning checks are two separate things.*
- Is recursion still in the course? The first-build plan had it in
  Unit 3; with conditionals and loops already taught and about four
  content weeks left after Fall Break, it competes directly with the
  data structures unit.
  - yes
  - *Closed 2026-10-05 by the recursion entry above: Unit 3 in
    spring, a speed-run taster in fall 2026.*
- Does this build become the spring 2027 plan as well? (Dan: not sure
  yet, 2026-09-27.)
  - yes
  - *Closed 2026-10-05 by the spring 2027 entry above.*
