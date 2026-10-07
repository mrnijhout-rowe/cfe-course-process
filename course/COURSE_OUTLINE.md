# CS4120 Course Outline, second build

Status: APPROVED 2026-10-05. Written 2026-10-05 and revised the same
day to apply Dan's answers, which are recorded at the end of this file;
Dan approved it in BUILD_PLAN.md, step 0.1. It replaces the 2026-09-27
outline. Tags follow CLAUDE.md section 1.

This file is the course structure: the units, every lesson in one line,
what is read, what is assigned in Codio, where the peer instruction
question comes from, where students build something outside Codio, and
how each unit is assessed. course/BUILD_PLAN.md says how the materials
get written from it.

## What Dan decided on 2026-10-05

These are Dan's answers from the conversation that produced this
outline and from what he wrote at the end of this file. They are
written here so the outline reads on its own. The ones that are
standing rules are in DECISIONS.md and CLAUDE.md, entered 2026-10-05.

- The structure covers the whole course from the first coding lesson,
  which is how spring 2027 will run. The rest of fall 2026 is built
  first, because class resumes October 12.
- The coding content is three units, not two. Unit 2 is Think Python
  chapters 1 to 4, Unit 3 is chapters 5 and 6, and Unit 4 is data
  structures. Unit 5 is the speed run and final project. Files built
  this fall use these numbers. Fall 2026 students were taught chapters
  1 to 6 as one unit called Unit 2, so Dan changes numbers by hand
  where a fall student would see one, and student-facing text names a
  unit by its topic where it can.
- Lesson order follows Think Python's chapter order. Practice of each
  new concept comes from the ready-made Codio course described in
  sources/codio_course/. Its name is "Python Programming from Codio."
- `input()` and f-strings are taught before the book has them. `while`
  loops are required. Nested loops get one lesson, which is the first
  cut. Turtle graphics stays.
- Outside Codio guides, students write code in Thonny on their laptops.
- Mini-projects and project options start in the first coding week.
  Small ones are looked at while Dan walks the room, with no grade.
  The larger one, turtle art, counts as a small grade in the Projects
  category.
- Each unit project is written with three options. Dan chooses which
  of them a class is offered.
- Three kinds of assessment run in the coding units: reading quizzes,
  learning checks, and a unit quiz. The section "Assessments" below
  describes each.
- Peer instruction with Plickers stays, drawing first on Cynthia
  Taylor's questions in sources/peer_instruction/.
- Python Tutor (pythontutor.com) is used for live demos. Lesson plans
  give links that open the demo code there, and students come to use
  the tool themselves.
- Recursion is taught in book order, after return values. In fall 2026
  that block is already past, so recursion is a speed-run taster.
- Strings, lists, and dictionaries are taught as one family. This is
  already a [DEFAULT] in DECISIONS.md.
- Project documents (handout, feedback forms, rubric, run sheet) are
  written in markdown here. Turning them into Word files is a separate
  step Dan asks for when a project is about to run.
- Two entries went into DECISIONS.md at Dan's direction: student-facing
  text says "Mr. Nijhout-Rowe," and time estimates run tight.

## Taught so far (fall 2026, weeks 1 through 7)

- **Unit 1: Information** (weeks 1 to 2). Eight lessons, unplugged,
  ending in Quiz 1. Unchanged from the first build; see
  units/01-information/README.md.
- **Think Python chapters 1 to 6, taught as one unit called Unit 2**
  (weeks 2 to 7). In this outline's numbering that content is Units 2
  and 3. Expressions, types, variables, print and f-strings, functions
  with and without return values, conditionals, loops, `input()`.
  Closed with the text-based adventure lab in week 7: pairs, three
  meetings (50, 90, and 50 minutes), written in Thonny. The lab's
  materials are in sources/fall_2026_text_based_adventure/. They show
  that fall students have used `while` loops, functions that return two
  or three values, `.strip().lower()` on input, and a function that
  calls itself to ask again, though the lab kept the word "recursion"
  out of it. Recursion was not taught as a topic. The quiz Dan wrote on
  Units 1 and 2 and the lab, with its Codio review guide, is in
  sources/assessments/unit_2_quiz/. See
  units/02-python-foundations/UNIT_2_AS_TAUGHT.md for the full record
  and the gaps that remain.

## The course at a glance

| Unit | What | Think Python | Lessons | Spring 2027 | Fall 2026 |
|---|---|---|---|---|---|
| 1 | Information | none (department readings) | 8 | weeks 1-2 | taught |
| 2 | Python Foundations | chapters 1-4 | 10 | weeks 3-5 | taught, in an earlier shape |
| 3 | Decisions and Recursion | chapters 5-6 | 13 | weeks 6-8 | taught, in an earlier shape, without recursion |
| 4 | Data Structures | chapters 7-11; chapter 12 feeds the project | 16 | weeks 9-12 | weeks 8-11 |
| 5 | Speed run and final project | picks from chapters 13-18 | about 12 meetings | weeks 13-15 | weeks 12-15 |

Fall 2026 taught Units 2 and 3 together and called them Unit 2. The
files built this fall use the numbers above anyway, so the same files
serve spring. Dan changes a number by hand where a fall student would
see one.

**Budget.** A semester is 15 weeks at four meetings a week, three of 50
minutes and one of 90. Unit 1 takes the first two weeks and the last
three are reserved, which leaves ten weeks for Units 2, 3, and 4.
Counting a 90-minute meeting as two lesson slots, spring weeks 3 to 8
hold about 28 slots for the 23 lessons of Units 2 and 3, and weeks 9 to
12 hold about 19 slots for Unit 4's 16. Learning checks (about ten
minutes each) and the three unit quizzes (about 30 minutes each) come
out of the slots left over. Dan places the unit quizzes; they are not
numbered lessons. In both semesters the mid-semester break falls
between Unit 3 and Unit 4.

## How one lesson uses the pieces

The period shape is CLAUDE.md section 3. This is how the pieces Dan
asked for sit inside it.

- **Reading.** A Think Python chapter, or part of one, is due on the
  day its first lesson is taught. A reading quiz opens that lesson.
- **Learning check.** On the lessons marked below, a learning check
  takes the first ten minutes. Those lessons have no reading quiz.
- **Concept.** Live code in Thonny. When the idea is about what is
  stored where (assignment, a function call, a list with two names),
  the plan also gives a Python Tutor link that opens the same code,
  ready to step through.
- **Peer instruction.** Two or three Plickers questions per concept
  lesson (DECISIONS.md, 2026-10-07), from Cynthia Taylor's bank where
  it has them. "Taylor" in the tables below means the bank has
  questions that fit. "New" means it does not, and a question is
  written for this course and labeled that way. "Taylor, plus new"
  means the bank covers part of the set.
- **Try it and partner challenge.** Typed in Thonny, not Codio.
- **Mini-project.** On the days marked below, a small build takes the
  partner-challenge slot, or the work half of a 90-minute meeting.
- **Codio.** Each Codio "lesson" assignment is started in the last ten
  minutes and finished as homework. A Codio unit's Lab and Coding
  Exercises are assigned once every lesson they depend on has been
  taught.

## Mini-projects and projects

Three sizes of work happen outside Codio. All of it is written in
Thonny.

- **Small mini-project.** Ten to fifteen minutes early in the course,
  up to about twenty-five later. A complete small program with a
  purpose and at least one thing the student chooses. Dan looks at each
  one while walking the room. No grade. It lives inside the lesson
  plan: the brief as students see it, two or three options, what to
  look for, and one commented sample solution.
- **Larger mini-project.** One to two lessons of class time, with a
  short rubric. It counts as a small grade in the Projects category.
  There is one in this outline: turtle art, which closes Unit 2. It
  gets its own file.
- **Unit project.** Four lessons, rubric-graded, never autograded.
  Unit 3 and Unit 4 each end with one. Each is written with three
  options, and Dan chooses which of them a class is offered. Both
  follow the plan of the fall 2026 text adventure, which ran in three
  meetings of 50, 90, and 50 minutes: pairs write a plan, another pair
  reviews it, Dan signs off before any code is typed, comments go in
  before code, another pair reviews the running program, and each
  student writes a reflection.

Every mini-project slot below lists two or three options. They are a
menu for Dan, and on most days students can be given the choice too.

## Assessments

Three kinds run in the coding units. Dan's examples of the second and
third are in sources/assessments/.

- **Reading quiz.** Three to five questions at the start of the lesson
  a reading is due for, about five minutes. Every question is multiple
  choice with four options and one correct answer, so the quiz can be
  given as Codio multiple-choice assessments, and it grades itself
  (DECISIONS.md, 2026-10-07). The file written here is the markdown
  master with its key; its Codio files are made from it with the
  codio-mcq skill (CLAUDE.md section 6).
- **Learning check.** About every five or six class meetings. Four
  questions, projected, answered in the paper journal, which Dan
  collects. Ten points. The first three questions (2, 2, and 3 points)
  are easy for a student who was awake and took part in class. The
  fourth (3 points) is easy for a student who worked through a recent
  assignment themselves, and hard for one who did not. Attention alone
  earns 7 of 10. Checks are written to the length and kind of answer
  of Dan's examples, which grade in about 90 seconds a journal. They
  count in the Labs/Learning Checks category. Each check covers only
  the lessons before the one it is marked on, so Dan can give it a day
  late but not a day early.
- **Unit quiz.** After the unit's project, so it can ask about the
  project. About 30 minutes of student time, taken in Canvas: ten to
  thirteen multiple-choice questions and two short-answer questions
  graded by rubric. About a fifth of the points come from earlier
  units. A Codio review guide (notes, practice questions, and an
  answer page) is built with each quiz and assigned before it. The
  unit quiz is not a numbered lesson. Dan schedules it, and the lesson
  counts and lesson plans leave its time out.

## Where the book and the Codio course do not line up

Codio assignment IDs come from sources/codio_course/
codio_course_reference.md: U6.L4 is Codio Unit 6, lesson 4; U6.LAB is
that unit's lab; U6.EX is its five coding exercises. A "U" always means
a Codio unit. This course's own lessons are written 4.1, with no letter.

The reference file and the PDF export both name the course "Python
Programming from Codio." CLAUDE.md and DECISIONS.md call it "Learn to
Code with Python." Dan confirmed on 2026-10-05 that the first name is
right, and both files were corrected that day.

1. **Functions.** The book teaches them in chapters 3 and 6. Codio
   holds them until its Unit 8, after lists, strings, and files. The
   five Unit 8 lessons are assigned in this course's Units 2 and 3,
   where the book puts them, in an order that keeps each one within
   reach: U8.L1 and U8.L3 with chapter 3, then U8.L4, U8.L2, and U8.L5
   with chapter 6. U8.EX uses lists and strings, so it waits until
   lesson 4.8 and works there as review. U8.LAB is a CSV movie sorter
   and is not assigned.
2. **Strings and lists.** The book teaches strings first; Codio teaches
   lists first. Nothing breaks. Codio Unit 6 is assigned before Codio
   Unit 5.
3. **Dictionaries and tuples.** The book teaches dictionaries first;
   Codio teaches tuples first. Codio's U10.L2 loops with
   `for key, value in d.items()` two lessons before tuples get their
   day here. The lesson 4.10 demo shows that one line and says tuples
   are coming.
4. **Tuples.** Codio's Unit 9 goes far past the book (`lambda`, `map`,
   `filter`). Only U9.L1 is assigned.
5. **`while` and nested loops.** Think Python, 3rd edition, has no
   `while` loop and no section on nested loops. Codio Unit 4 and
   Taylor's bank both cover them. They enter Unit 3 by choice, not from
   the book.
6. **Whole assignments.** A Codio Lab or Coding Exercises set is one
   assignment. Where one problem in a set does not fit, the table
   names the problem to waive.
7. **Not assigned in Units 2, 3, and 4:** U5.L6 (2D lists), U6.L2
   (`min` and `max` on strings), Codio Unit 7 (files), U8.LAB, U9.L2 to
   U9.L4 with U9.LAB and U9.EX (nested tuples, `zip`, and `lambda`),
   U10.L4 (nested dictionaries and JSON), Codio Unit 11 (sets), and
   Codio Units 13 to 18 (objects). Several of these supply speed-run
   tasters. U10.LAB (ASCII art with the Pillow library) is optional
   enrichment.

### Codio pages that run ahead of class

Every Codio assignment named in Units 2, 3, and 4 was checked on
2026-10-05 against the PDF export in sources/codio_course/. The text
of each was scanned for code that uses something the class has not
reached at the lesson where it is assigned, and the pages that matched
were read. Assignments not listed here were clean. The export leaves
out the interactive widgets and a few exercise prompts, so those were
not checked. Page numbers are the PDF's.

| Codio lesson | Assigned at | What runs ahead |
|---|---|---|
| U8.L1 Function Basics | 2.5 | p. 428 shows one `return`. p. 436 draws a house with turtle and `for i in range(3)`, two and three lessons early. |
| U8.L4 Returning Values | 3.4 | p. 473 returns a list. p. 478 builds a list with `append` in a loop. Lists are Unit 4. |
| U8.L2 Parameters | 3.5 | pp. 442 and 448 pass a list as an argument. pp. 449-450 teach `try`/`except`. p. 452 loops over `*nums`. Class teaches none of these. |
| U12.L1 What is Recursion? | 3.8 | p. 868 speeds up Fibonacci with a dictionary. The second check question is about a list. |
| U6.L4 String Iteration | 4.1 | pp. 324 and 328 loop with `while` and `word[index]`. Indexing is lesson 4.3. |
| U5.L1 List Basics | 4.5 | p. 179 shows list comprehensions, which class does not teach. |
| U10.L1 Introduction to Dictionaries | 4.9 | The page on hashing uses tuples as keys. Tuples are lesson 4.12. |
| U10.L2 Iterating Over Dictionaries | 4.10 | `for key, value in d.items()` throughout, and a section on dictionary comprehensions. |
| U9.L1 Introduction to Tuples | 4.12 | 32 pages. The last section converts among tuples, lists, sets, and dictionaries; sets are not taught. |

None of these blocks an assignment. Each is one line in that lesson's
plan, telling Dan what students will meet in Codio that class has not
covered.

## Unit 2: Python Foundations (Think Python chapters 1 to 4)

Ten lessons. Built for spring 2027; fall 2026 already taught this
content in an earlier shape.

Two things are taught earlier than the book has them, so that early
mini-projects can be real programs: `input()` (chapter 5 in the book)
and f-strings (chapter 13).

### Values, variables, and statements (chapters 1 and 2)

| # | Lesson | Reading due | Codio | Peer instruction | Outside Codio |
|---|---|---|---|---|---|
| 2.1 | Expressions, values, and types. Thonny's shell as a calculator, then a first saved program. | ch. 1, quiz | U1.L1 | Taylor | Mini: a name banner built with `+` and `*` on strings |
| 2.2 | Variables and assignment; reassignment; what a name refers to. | ch. 2, quiz | U1.L2 | Taylor | Python Tutor demo of assignment |
| 2.3 | Statements and output: `print`, f-strings, comments, `import math`; reading the last line of an error message. | none | U2.L1 | Taylor | Mini: a receipt, a recipe scaler, or which pizza is the better deal |
| 2.4 | `input()` and converting types with `int`, `float`, `str`. | none | U6.L6, U1.LAB, U1.EX | new | Mini: a Mad Lib, a tip splitter, or a unit converter |

### Functions and repetition (chapters 3 and 4)

| # | Lesson | Reading due | Codio | Peer instruction | Outside Codio |
|---|---|---|---|---|---|
| 2.5 | Defining and calling a function; define before you call. | ch. 3, quiz | U8.L1 | Taylor | none |
| 2.6 | Parameters and arguments; variables inside a function are local. | none; **learning check** on 2.1 to 2.5 | U8.L3 | Taylor | Python Tutor demo of a function call. Mini: a song-verse printer or a greeting card |
| 2.7 | Repetition with `for` and `range`; the loop variable; a running total. | none | U4.L1, loop pages | Taylor | Students step through a loop in Python Tutor themselves for the first time |
| 2.8 | Turtle graphics: functions and loops that draw. | ch. 4, quiz | U4.L1, turtle pages | Taylor | Mini: your initials, a house, or a row of stars |
| 2.9 | Making a function general: `square` to `polygon` to `circle`; docstrings; tidying code that works. | none | none | new | Turtle art begins |
| 2.10 | Turtle art work day and gallery walk. | none | none | none | **Larger mini-project: turtle art**, a small project grade |

Notes:

- Codio's five function lessons are not assigned in Codio's order.
  U8.L1 and U8.L3 are assigned here; U8.L3 (scope) is clean and fits
  2.6. The other three wait for Unit 3.
- Lessons 2.9 and 2.10 have no Codio match. The turtle work is the
  practice.
- The learning check at 2.6 draws its fourth question from U1.LAB or
  U1.EX, assigned at 2.4.

**Unit 2 quiz.** After turtle art. The fall 2026 quiz in
sources/assessments/unit_2_quiz/ is the starting point: most of it
already covers this unit, and about a fifth of it covers Unit 1. Its
text adventure questions move to the Unit 3 quiz, and turtle and
`input()` questions take their place.

**Final-project pointer from Unit 2:** generative art with turtle.

**Cut point:** shrink turtle art to the second half of 2.9, which
removes 2.10.

## Unit 3: Decisions and Recursion (Think Python chapters 5 and 6)

Thirteen lessons: nine of content and a four-lesson project. Built for
spring 2027; fall 2026 taught this content in an earlier shape, without
recursion as a topic.

Recursion is taught once, after return values, joining the recursion
sections of chapters 5 and 6. `while` loops and nested loops are not in
the book and enter here by choice.

| # | Lesson | Reading due | Codio | Peer instruction | Outside Codio |
|---|---|---|---|---|---|
| 3.1 | Boolean expressions and `if`; `//` and `%`. | ch. 5 through "Nested Conditionals," quiz | U2.L2, U3.L1 | Taylor | none |
| 3.2 | `else`, `elif`, and nested conditionals. | none | U3.L2, U3.L4 | Taylor | Mini: a ticket price, a quiz that keeps score, or a story with two choices |
| 3.3 | `and`, `or`, `not`; one compound condition in place of nested ones. | none | U3.L3; then U3.LAB, U3.EX, U2.LAB, U2.EX | Taylor | none |
| 3.4 | Return values; `return` versus `print`; `None`. | ch. 6 through "Boolean functions," quiz | U8.L4 | Taylor | Python Tutor demo of a value coming back |
| 3.5 | Boolean functions; building a function in small tested steps; functions that use other functions. | none | U8.L2, U8.L5 | Taylor | Mini: a triangle checker, a leap-year test, or a letter-grade function |
| 3.6 | `while` loops; `break`; asking again until the input is valid, with `.strip().lower()` to clean what was typed. Not in the book. | none; **learning check** on 3.1 to 3.5 | U4.L2 | Taylor | Mini: a guessing game, a PIN entry, or a countdown |
| 3.7 | Nested loops and patterns. Not in the book. First cut point. | none | U4.L3; then U4.LAB, U4.EX | Taylor | Mini: a times table or a pattern of your own |
| 3.8 | Recursion: a function that calls itself; the base case; the stack of calls. | recursion sections of ch. 5 and ch. 6, quiz | U12.L1 | Taylor | Python Tutor demo; students step through one themselves |
| 3.9 | Recursion that returns a value: factorial and Fibonacci. | none | U12.LAB | Taylor | Mini, for pairs who are ready: a recursive turtle tree or a sum of digits |
| 3.10 | Project day 1: play an example, flowcharts, pairs write a story idea, another pair reviews it. | none | none | none | Unit project begins |
| 3.11 | Project day 2, first half: flowchart sign-off, work plan, handling what the player types, comments before code. | none | none | none | Unit project |
| 3.12 | Project day 2, second half: code. | none | none | none | Unit project |
| 3.13 | Project day 3: finish, another pair plays and reviews it, fix, turn in. Reflection is homework. | none | none | none | Unit project due |

Notes:

- U8.L2 (parameters) uses `if`, a list, and `try`/`except`, so it
  waits for 3.5, where chapter 6's "Checking types" section gives it a
  home.
- U8.L5 uses turtle's `goto`, `penup`, and `pendown`, which lesson 2.8
  will have shown.
- U2.LAB and U2.EX include boolean problems, so they wait for 3.3.
- U12.EX has one list problem and one string problem, so it is
  assigned in Unit 4 at lesson 4.8.
- The learning check at 3.6 draws its fourth question from U3.LAB,
  U3.EX, U2.LAB, or U2.EX, assigned at 3.3. There is one check in this
  unit; the project days do not get one.

**Unit 3 project (3.10 to 3.13).** The text adventure Dan ran in fall
2026 is the model, and its materials are in
sources/fall_2026_text_based_adventure/. Lessons 3.11 and 3.12 are one
90-minute meeting when the timetable allows. In spring the project
comes after `while` and recursion have been taught, so the "ask again"
step can use a loop, and a scene function that calls itself can be
called what it is. Three options are written, and Dan chooses which of
them a class is offered. They share one set of requirements: the
player types choices, at least five decisions, a win ending and a lose
ending, comments before code, functions, and input that never breaks
the game.

- **A. Text adventure.** As run in fall 2026: scenes, decisions, and
  endings, in either of the lab's two code patterns.
- **B. Quiz show.** Questions, scoring, and one twist of the student's
  design, such as lifelines, a wager round, or two players.
- **C. Survival trip.** A turn-by-turn game of supplies and decisions,
  in the spirit of The Oregon Trail. This is the lab's second code
  pattern (one function, a `while` loop, and stats) grown into a game.

**Unit 3 quiz.** After the project. It can ask about the project, as
the fall 2026 quiz did with the text adventure. About a fifth of its
points come from Units 1 and 2.

**Final-project pointers from Unit 3:** games with pygame, and
fractals.

**Cut points, in order:** lesson 3.7 (nested loops); fold 3.9 into
3.8.

## Unit 4: Data Structures (Think Python chapters 7 to 11)

Sixteen lessons: twelve of content and a four-lesson project. Built
first, for fall 2026 weeks 8 to 11. The same unit runs in spring 2027
weeks 9 to 12.

**Where fall 2026 students start.** The text adventure shows they have
already used three things this unit teaches properly: `.strip()` and
`.lower()` (lesson 4.4 starts from those two and widens), a function
that returns two or three values that are then assigned to two or
three names (lesson 4.12 gives that a name), and a function that calls
itself (the recursion taster starts there). They have written `while`
loops and worked in Thonny. They have used `for` only over `range`,
so looping over a string directly is new in lesson 4.1. They have
watched Dan step through code in Python Tutor for about a week and
have not driven it themselves.

**Organizing idea.** Strings, lists, and dictionaries are one family.
The shared rules (loop with `for`, test membership with `in`, measure
with `len`, index and slice the ordered ones) are taught once, on
strings. Each new container then arrives as "the same rules apply;
here is what is different." One comparison table grows across the
unit: a row is added for strings in 4.1 to 4.4, lists in 4.5,
dictionaries in 4.9, and tuples in 4.12. Its columns are: how you
write one, how you reach one element, whether it has an order, whether
it can be changed in place, and whether `len`, `in`, and `for` work.

| # | Lesson | Reading due | Codio | Peer instruction | Outside Codio |
|---|---|---|---|---|---|
| 4.1 | A string is a sequence: `for` over a string, `len`, `in`, counting. | ch. 7, quiz | U6.L4 | Taylor, plus new | Mini: a letter counter. The comparison table starts. |
| 4.2 | Search: reading `words.txt` line by line; a loop that answers yes or no. | none | none | new | Mini: a Spelling Bee helper, or find the words with no "e" |
| 4.3 | Indexing and slicing; negative indices; `IndexError`. | ch. 8 through "String methods," quiz | U6.L1 | Taylor | Python Tutor demo |
| 4.4 | Strings cannot be changed in place; methods return new strings; building a string in a loop. | none | U6.L3, U6.L5; then U6.LAB, U6.EX | Taylor, plus new | Mini: a Caesar cipher, Pig Latin, or a palindrome checker |
| 4.5 | Lists: the same rules, and one difference. A list can be changed in place. | ch. 9, quiz | U5.L1, U5.L2 | Taylor | Python Tutor demo. Table: lists. |
| 4.6 | List methods; building a list in a loop; `sum`, `min`, `max`. | none; **learning check** on 4.1 to 4.5 | U5.L3, U5.L4, U5.L5; then U5.LAB | Taylor, plus new | Mini: a dice-roll histogram or a playlist manager |
| 4.7 | Lists and strings: `split`, `join`, `sorted`. | none | U5.EX, waive problem 5 | new | Mini: an anagram finder or a word scramble |
| 4.8 | Aliasing: two names, one list; lists as arguments. | none | U8.EX, waive problem 4; U12.EX in spring | Taylor | Students drive Python Tutor |
| 4.9 | Dictionaries: keys in place of positions; look up, add, change; `KeyError`. | ch. 10, quiz | U10.L1 | Taylor, plus new | Python Tutor demo. Table: dictionaries. |
| 4.10 | A dictionary of counters; looping over a dictionary. | none | U10.L2 | new | Mini: letter frequencies of a text you pick |
| 4.11 | Dictionaries and lists together; why dictionary lookup is fast. | none; **learning check** on 4.6 to 4.10 | U10.L3 | Taylor, plus new | Mini: anagram families or a Scrabble scorer |
| 4.12 | Tuples: swap, two return values, `items()`. `zip` and `enumerate` for pairs who are ready. | ch. 11, selected sections, quiz | U9.L1; then U10.EX, waive problem 5 | new | Table: tuples. The table is complete. |
| 4.13 | Project day 1: the option or options Dan chose, write the plan, another pair reviews it. | ch. 12 as project reference, no quiz | none | none | Unit project begins |
| 4.14 | Project day 2, first half: sign-off, work plan, comments before code. | none | none | none | Unit project |
| 4.15 | Project day 2, second half: code. | none | none | none | Unit project |
| 4.16 | Project day 3: finish, another pair runs and reviews it, fix, turn in. Reflection is homework. | none | none | none | Unit project due |

Notes:

- U6.L4 is the closest Codio match for lesson 4.1, but two of its
  pages index into the string two lessons early. Students can stop at
  those pages and finish after 4.3.
- U10.L3 is 31 pages and ends by timing a list against a dictionary,
  which is lesson 4.11's demo.
- Every U5.EX problem starts with `import sys` lines that feed the
  autograder; students leave them alone. Problem 5 needs a 2D list,
  which is not taught. U10.EX problem 5 needs JSON files. Every U10.EX
  problem wraps its tests in `if __name__ == "__main__":`.
- The learning check at 4.6 draws its fourth question from U6.LAB,
  U6.EX, or the lesson 4.4 mini-project. The check at 4.11 draws its
  fourth from U5.LAB, U5.EX, or U8.EX. The unit plan picks one for
  each and says why.
- Files enter as far as the book uses them in chapter 7: opening
  `words.txt` and looping over its lines. Writing files and CSV data
  stay out of this unit.
- Regular expressions (chapter 8) and sets are named as pointers and
  not taught.
- Taylor's bank is deep on lists (17 questions) and thin on strings
  (7) and dictionaries (3), with nothing on tuples. About half of this
  unit's questions will be new.
- U10.LAB (ASCII art) is optional enrichment for a long block.
- For fall 2026, U12.EX follows the recursion taster in the speed run.

**Unit 4 project (4.13 to 4.16).** It runs on the plan fall students
already know from the text adventure: a written plan, review by
another pair, sign-off, comments before code, a second review, and an
individual reflection. In fall 2026 it fills week 11, which by the
calendar map's count has three meetings, one of them 90 minutes: the
same time the text adventure had. Three options are written, and Dan
chooses which of them a class is offered. They share one set of
requirements: the program reads a text file, uses a string operation,
a list, and a dictionary where each one is the right choice, and is
organized into functions.

- **A. Text generator.** Choose a text, count word frequencies, then
  build a model of which word follows which and generate new text from
  it. This is Think Python chapter 12, done as a project. It connects
  to how tools like ChatGPT work.
- **B. Codebreaker.** Write a Caesar cipher, then break one by counting
  letter frequencies in a real text. It connects back to Unit 1.
- **C. Word game.** Wordle, Hangman, or a Spelling Bee, with the word
  list read from a file and a dictionary that tracks letters or
  statistics across rounds.

**Unit 4 quiz.** After the project. About a fifth of its points come
from earlier units. For fall 2026 students that share can use return
values, `while`, and boolean expressions, which the fall quiz on
Units 1 and 2 did not test directly.

**Final-project pointers from Unit 4:** regular expressions, modern
cryptography, and where the text generator stops and a real language
model begins.

**Cut points, in order:** fold tuples (4.12) into 4.11 as swap and two
return values only; drop the search lesson's file reading to a
five-minute demo and merge 4.2 into 4.1.

## Unit 5: Speed run and final project

About twelve meetings: six one-meeting tasters, then six for the final
project. Each taster is a demo, a try-it, and a pointer to where to
learn more. Dan picks the six each semester.

| Taster | Support in the sources |
|---|---|
| Files and CSV data | Codio Unit 7 |
| Sets, `Counter`, and list comprehensions | Think Python ch. 18; Codio Unit 11 |
| Classes and objects | Think Python ch. 14-15; Codio Unit 13; 13 Taylor questions |
| Searching, sorting, and how run time grows | 28 Taylor questions; connects to Unit 1's algorithms |
| Windows and buttons with tkinter | Codio Unit 13 lab |
| Animation with pygame | Codio Unit 14 lab |
| Recursion and fractals (fall 2026 only) | Think Python ch. 5-6; Codio Unit 12; 15 Taylor questions. Starts from the text adventure's scene function that calls itself to ask again. |
| micro:bit with MicroPython, from Thonny | the class set of micro:bits |
| numpy and data tools | none in the sources |

**Chosen for fall 2026 so far** (Dan, 2026-10-05): recursion, classes
and objects, and windows and buttons with tkinter. Three more are
needed by about October 30. Recursion is fixed for fall because the
catalog lists it and fall students have not been taught it.

**Final project.** Student's choice, and it must go beyond what the
course covered. Proposals are due during the speed run. Presentations
finish by the last full week of classes, which in fall 2026 ends
December 4. The final-exam period is not used.

## Calendar

### Fall 2026, from October 12

| Weeks | Dates | What |
|---|---|---|
| 8 | Oct 12-16 | Unit 4, lessons 4.1 to 4.4: strings |
| 9 | Oct 19-23 | 4.5 to 4.8: lists; learning check at 4.6 |
| 10 | Oct 26-30 | 4.9 to 4.12: dictionaries and tuples; learning check at 4.11 |
| 11 | Nov 3-6 | 4.13 to 4.16: project |
| after the project | Dan places it | Unit 4 quiz, about 30 minutes |
| 12-13 | Nov 9-20 | Speed run, six meetings, recursion included; final project proposals due; final project opens in the last meetings before Thanksgiving |
| 14 | Nov 30-Dec 4 | Final project work; presentations finish this week |
| 15 | Dec 7 | One class day after presentations, for Dan to use |

Weeks 8 to 10 hold about 15 lesson slots for 12 lessons and two
learning checks. Week 11 is short and holds the whole project. If
Unit 4 runs long, the cut points above apply before the project loses
a day.

### Spring 2027

| Weeks | Dates | What |
|---|---|---|
| 1-2 | Feb 1-12 | Unit 1 |
| 3 | Feb 15-19 | Unit 2, lessons 2.1 to 2.4 |
| 4-5 | Feb 22-Mar 5 | 2.5 to 2.10, with the learning check at 2.6; then the Unit 2 quiz |
| 6-7 | Mar 8-19 | Unit 3, lessons 3.1 to 3.9, with the learning check at 3.6 |
| 8 | Mar 22-25 | Unit 3 project, 3.10 to 3.13, due before Spring Break. The Unit 3 quiz falls on one side of the break or the other; Dan places it. |
| 9-12 | Apr 5-29 | Unit 4, then the Unit 4 quiz |
| 13-15 | May 3-20 | Unit 5: speed run and final project, during Advanced Placement exams |

## Dan's answers, 2026-10-05

Dan wrote the first nine on the lines this outline left for him. His
words are kept as written. Each answer has been applied above, and
the ledger and charter wording that follows from them is in
DECISIONS.md and CLAUDE.md as of 2026-10-05.

1. **Unit 2 as one unit in three parts, or two units.** The
   recommendation was one unit.

   Dan: Let's split it into two units going forward. I will adjust the unit numbering manually as I use it this semester.

2. **`input()` and f-strings early.** Both come before the book has
   them.

   Dan: yes

3. **`while` and nested loops.** Neither is in the book. `while` is
   required; nested loops is one lesson and the first cut.

   Dan: yes

4. **Turtle.** Two lessons and a work day on chapter 4.

   Dan: yes

5. **Paper quizzes 2, 3, and 4.** The recommendation was a 20 to 25
   minute paper quiz at three marked spots.

   Dan: Let's have quizzes at the end of each unit, but let's have "learning checks" every 5-6 classes. These should be 4 questions, displayed on a slide and projected for the class. The first three questions should be easy if the student was awake and participated in class, the fourth should be easy if they actually struggled with an assignment during the previous lessons. Getting the first 3 right should be ~60-70% the last one should be 30-40% They are answered in their journals which are actual physical journals that I collect. The class set should be gradeable in ~15 minutes. I have placed examples of learning checks from my level two Object Oriented Design course in the sources folder. And an example of the unit 2 quiz in there as well.

6. **How the larger mini-project counts.** The recommendation was as a
   lab.

   Dan: As (small) project grades.

7. **Project options.** Three per unit are listed. The recommendation
   was to let students choose among all three.

   Dan: I will choose from those which are offered.

8. **Codio course name.** The export and the reference file say
   "Python Programming from Codio." The recommendation was to correct
   the charter.

   Dan: yes

9. **Still open from DECISIONS.md:** whether journal learning checks
   continue beside reading quizzes, and where reading quizzes are
   taken.

   Dan: As noted above, the quizzes and learning checks will be two separate things

Answered earlier on 2026-10-05:

10. **Project handouts.** The project packages write the handout, the
    two feedback forms, the rubric, and the run sheet in markdown.
    Turning them into Word files is a separate step Dan asks for when
    a project is about to run.
11. **Two decisions from the text adventure's own ledger.** Both are
    now in DECISIONS.md: student-facing text says "Mr. Nijhout-Rowe,"
    and time estimates run tight.
12. **The text adventure folder's own instruction files.** Dan renamed
    them so no session mistakes them for this repository's rules:
    `Adventer.agents_bu.md` and `Adventure.decisions_bu.md`. README.md
    now lists both new source folders.

Four follow-up questions, asked and answered in chat later on
2026-10-05:

13. **After the split, how are the files built this fall numbered?**
    Dan chose: Unit 4 now. Files are LP_4.1 and up in
    units/04-data-structures, matching spring. Dan relabels by hand for
    fall students. Student-facing pages avoid unit numbers where they
    can.
14. **Do the five-minute reading quizzes stay?** Dan: "Keep them, make
    them simple to be administered via Canva LMS or Codio MCQ." That
    is read here as Canvas, or Codio multiple-choice assessments.
15. **Where does the unit quiz go?** Dan: "After the project, keep the
    time needed for the students down to about 30 minutes, I can
    account for that time, you do not need to in your class plans."
16. **Should each unit quiz come with a Codio review guide like the
    one in sources/assessments/unit_2_quiz/Codio_Review?** Dan chose:
    yes, build both.

Three more, asked in chat on 2026-10-05 after Dan edited choices 5, 6,
and 7 below:

17. **Are learning checks here shorter than Dan's examples?** Dan
    chose: like my examples. Same length and kind of answer, about 90
    seconds a journal; a sketch or a few lines of code in an answer is
    fine.
18. **How do the four questions go on the projector?** Dan: "Do not
    worry about this." The files set no limit for fitting a slide.
19. **What is "Labs/Learning Checks"?** Dan chose: the 35 percent
    category, renamed. It is the category COURSE.md calls "Codio work,
    problem sets, and labs."

Two more, asked in chat on 2026-10-05 after Dan answered step 0 in
BUILD_PLAN.md:

20. **How should the eight carried-over entries in DECISIONS.md be
    treated?** Dan chose: confirm as written. All eight become dated
    entries unchanged. One of them says presentations finish by the
    last full week, so this outline was changed from "by the last
    class day" to match.
21. **Should lesson packages also write reading quizzes as Codio
    files?** Dan chose: master only. He enters the questions in Canvas
    or Codio himself.
    *Superseded 2026-10-07: the quizzes run in Codio, and the Codio
    files are made from the master (DECISIONS.md, 2026-10-07).*

## Choices made while applying the answers

Dan's answers left these to be filled in. Each was decided so the
outline could be revised. Dan approved the outline with this list in
it on 2026-10-05 (BUILD_PLAN.md, step 0.1), so all ten stand.

1. **Where Unit 2 splits.** After turtle art. Unit 2 is chapters 1 to
   4 (lessons 2.1 to 2.10) and Unit 3 is chapters 5 and 6. That is
   where the outline already had a quiz and something built.
2. **Unit 3's name.** "Decisions and Recursion." Its folder is
   units/03-decisions-and-recursion.
3. **Where the learning checks sit.** One in Unit 2 (at 2.6), one in
   Unit 3 (at 3.6), and two in Unit 4 (at 4.6 and 4.11). "Every 5-6
   classes" was read as class meetings. No check falls on a project
   day or on a day with a reading quiz.
4. **Learning check points.** 2, 2, 3, and 3, as in Dan's examples, so
   the first three questions are 70 percent.
5. **Learning check grading time.** Dan's examples budget 30 minutes
   for 20 journals. Checks here are written to the same length and
   pace (answer 17).
6. **Learning checks are markdown files, not slide files.** Questions
   on top, sized to project the questions to a screen; teacher notes
   below, as in the examples. Dan puts them on a slide, and how they
   fit is his to handle (answer 18).
7. **Learning checks count under "Labs/Learning Checks."** That is the
   35 percent category, under its current name (answer 19).
8. **Unit quiz format.** It follows the fall 2026 quiz: taken in
   Canvas with no notes and no running code, multiple-choice questions
   at 2 points each, two short-answer questions at 7 points each, and
   about a fifth of the points from earlier units. It is held to ten
   to thirteen multiple-choice questions to fit 30 minutes.
9. **Reading quizzes are all multiple choice.** That is what lets them
   run in Canvas or Codio with no hand grading. The choice between
   Canvas and Codio stays [OPEN].
   *Closed 2026-10-07: Codio (DECISIONS.md).*
10. **Project handouts.** Because Dan chooses the options, each
    option's brief is its own file, and the shared handout does not
    mention the options a class was not given.
