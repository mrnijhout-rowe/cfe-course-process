# COURSE.md - CS4120 course facts

Facts about the course as it is, for every session. A fact is not a
rule a session can break; the ones marked **[RULE]** are those Dan's
ledger holds as rules, with the entry's date. Revised 2026-09-27 at the
start of the second build, 2026-10-05 when Dan approved the course
structure, and 2026-10-08 in the governance audit.

## Catalog

- Official description: introduction to basic programming skills and
  Python 3. Topics: variables, expressions and statements, functions,
  conditionals, loops, recursion, string manipulation, input/output,
  lists, dictionaries. Applications drawn from mathematics, science,
  engineering, and the humanities.
- Audience: students with no prior CS coursework. Assume zero
  programming experience and high general academic ability. Some
  students chose this course because it is not the intensive track;
  respect that. Two fall sections run in parallel and must pace
  identically.

## Meetings

- **[RULE]** Four meetings a week: three of 50 minutes and one of 90,
  on a rotating letter-day timetable, so nothing is tied to a weekday.
  Materials are written in 50-minute lessons and never depend on a long
  block. The budget is 13 to 14 lessons per three weeks, leaving one or
  two meetings of slack (DECISIONS.md, 2026-10-05).
- A semester is about fifteen weeks. Unit 1 takes the first two.
- **[RULE]** The last ~12 meetings are reserved: ~6 for a speed run of
  taster topics Dan picks each semester, then ~6 for final-project
  work. Presentations finish by the last full week; the final-exam
  period is not used (DECISIONS.md, 2026-10-05).
- Dan's schedule for a semester is his own and is not part of the
  materials (Dan, 2026-10-08). course/CALENDAR_MAP.md is his week grid
  for 2026-27; no session needs it.

## Structure

- **[RULE]** The coding content is three units, numbered the same in
  both semesters: Unit 2, Python Foundations (Think Python chapters 1
  to 4); Unit 3, Decisions and Recursion (chapters 5 and 6); Unit 4,
  Data Structures (chapters 7 to 11). Unit 5 is the speed run and final
  project. Unit 1, Information, is unplugged, taught, and unchanged
  from the first build (DECISIONS.md, 2026-10-05 and 2026-09-27).
- This build is the plan for spring 2027 from the first coding lesson.
  The rest of fall 2026 was built first, from the same structure. Fall
  2026 students were taught chapters 1 to 6 as one unit called Unit 2;
  what they know is in units/02-python-foundations/UNIT_2_AS_TAUGHT.md
  (DECISIONS.md, 2026-10-05).
- course/COURSE_OUTLINE.md is the course map: every unit and every
  lesson. Each coding unit has reading quizzes, learning checks,
  mini-projects, a project, and then a unit quiz.

## Sources

- **Unit 1:** the department's reading series (R1 to R4), in the
  first-build repository. Done.
- **[RULE] Think Python**, 3rd edition, by Allen Downey, is the reading
  and the source of examples for the coding units. Every student has
  the print book; the chapter notebooks are in sources/thinkpython/.
  It is source, not syllabus: topics start out and enter only by
  explicit curation in the unit plan (DECISIONS.md, 2026-10-05).
- **Codio's built-in course "Python Programming from Codio"** supplies
  the practice for each new concept: lessons, labs, and exercise sets,
  imported per topic into the course's Codio class. The outline says
  which assignment goes with which lesson, and a guide is authored
  here only when nothing in that course fits. sources/codio_course/
  holds a reference map of the course; its PDF export is on Dan's
  laptop only (DECISIONS.md, 2026-09-27 and 2026-10-05).
- **Cynthia Taylor's peer instruction bank**, sources/peer_instruction/,
  is the first source of Plickers questions (DECISIONS.md, 2026-10-05).
- **Python Tutor** (pythontutor.com) is the tool for showing what a
  program stores as it runs. Plans link to it; students drive it
  themselves from lesson 2.7 on, and in fall 2026 from Unit 4 on
  (DECISIONS.md, 2026-10-05).
- **Dan's own models:** sources/assessments/ (learning checks from his
  Object Oriented Design course, and the fall 2026 unit quiz with its
  Codio review guide) and sources/fall_2026_text_based_adventure/ (the
  project every unit project follows). README.md describes them.

## Platform and room

- Codio is the assignment platform. Homework is Codio guides with .py
  files and autograders; no notebooks in this build (DECISIONS.md,
  2026-09-27).
- Outside Codio, students write code in Thonny on their own laptops:
  try-its, partner challenges, mini-projects, and projects. Code in
  the materials uses nothing newer than Python 3.10 (DECISIONS.md,
  2026-10-05).
- Canvas carries the course page. Each coding lesson has a Canvas page
  written here and pasted in by Dan before class, with a unit page and
  a project page (course/formats/STUDENT_FACING.md). Reading quizzes
  run in Codio, reached through a link in Canvas; unit quizzes are
  taken in Canvas. Due dates live only in Canvas and Codio
  (DECISIONS.md, 2026-10-07).
- **[RULE]** The course Gemini Gem is the sanctioned AI tutor, allowed
  on every assignment all semester, never granted or revoked per
  assignment. Its prompt is Dan's; it is not authored here
  (DECISIONS.md, 2026-10-05).
- The room: tables with partner-size and individual whiteboards,
  several large wall whiteboards, and a class set of micro:bits that
  stay in the box unless a concept genuinely lands better on a device.
  Students keep paper journals, which learning checks are answered in
  and Dan collects. Plickers cards carry A to D.

## Grading

| Category | Weight |
|---|---|
| Projects | 25% |
| Tests and quizzes | 25% |
| Labs/Learning Checks | 35% |
| Final project | 15% |

- Labs/Learning Checks holds Codio work, problem sets, labs, and
  learning checks. Reading quizzes and unit quizzes fall under Tests
  and quizzes. Unit projects and larger mini-projects are rubric-graded
  under Projects; small mini-projects are not graded.
- **[RULE]** Every assessment is calibrated so that honest work is the
  easiest path to full credit: a student who merely showed up earns a
  passing but mediocre score, and a student who did the work earns
  full credit easily. The easiest path to an A is never delegating the
  work to an AI (DECISIONS.md, 2026-10-05).
- Final project: the student's choice of topic, and it must push
  beyond what the course covered. Each unit names at least one pointer
  toward a topic the course does not teach, so students collect ideas
  all semester (DECISIONS.md, 2026-10-05).

## Design threads

- The course's answer to "why learn this when AI writes code" is the
  durable ideas: information and encoding, algorithms, decomposition,
  abstraction. Unit 1 sets that up; the coding units echo it without
  lecturing about it.
- Applied contexts rotate across math, science, and humanities flavors
  rather than committing to one theme.
