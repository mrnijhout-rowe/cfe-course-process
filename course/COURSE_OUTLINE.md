# CS4120 Course Outline, second build

Status: APPROVED 2026-10-05. Written 2026-10-05 and revised the same
day to apply Dan's answers, which are recorded at the end of this file;
Dan approved it in the build plan's step 0.1 (now in
course/archive/BUILD_LOG_2026-10-07.md). It replaces the 2026-09-27
outline.

This file is the course structure: the units, every lesson in one line,
what is read, what is assigned in Codio, where the peer instruction
question comes from, where students build something outside Codio, and
how each unit is assessed. course/BUILD_PLAN.md says how the materials
get written from it.

## Dan's decisions behind this outline

Dan's answers of 2026-10-05, and the choices made while applying them,
are in course/archive/OUTLINE_2026-10-05_ANSWERS.md, as written. The
standing rules among them are in DECISIONS.md, dated 2026-10-05, and are
stated in CLAUDE.md, course/COURSE.md, and course/formats/.

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

**Budget.** A semester is about fifteen weeks at four meetings a week,
three of 50 minutes and one of 90 (course/COURSE.md). Unit 1 takes the
first two weeks and the last three are reserved, which leaves ten weeks
for the 23 lessons of Units 2 and 3 and the 16 of Unit 4. Learning checks
(about ten minutes each) and the three unit quizzes (about 30 minutes
each) come out of the slack. Dan places the unit quizzes; they are not
numbered lessons. In both semesters the mid-semester break falls between
Unit 3 and Unit 4. Where the weeks fall is Dan's schedule, not this
outline's.

## How one lesson uses the pieces

The period shape is in CLAUDE.md, "How class runs", and what each piece
contains is in course/formats/. Conventions the tables below use:

- **Reading.** A Think Python chapter, or part of one, is due on the
  day its first lesson is taught, and a reading quiz opens that lesson.
  On a learning check lesson there is no reading quiz.
- **Concept.** Live code in Thonny. When the idea is about what is
  stored where (assignment, a function call, a list with two names),
  the plan also gives a Python Tutor link.
- **Peer instruction.** "Taylor" in the tables means Cynthia Taylor's
  bank has questions that fit. "New" means it does not, and a question
  is written for this course and labeled that way. "Taylor, plus new"
  means the bank covers part of the set.
- **Outside Codio.** Try-its, partner challenges, and mini-projects are
  typed in Thonny, not Codio. A mini-project day is marked; it takes
  the partner-challenge slot, or the work half of a 90-minute meeting.
  Every mini-project slot lists two or three options: a menu for Dan,
  and on most days students can be given the choice too.
- **Codio.** Each Codio "lesson" assignment is started in the last ten
  minutes and finished as homework. A Codio unit's Lab and Coding
  Exercises are assigned once every lesson they depend on has been
  taught.

## Mini-projects, projects, and assessments

Three sizes of work happen outside Codio: small mini-projects inside
the lesson plan, one larger mini-project (turtle art, closing Unit 2,
with its own file), and a four-lesson unit project closing Units 3 and
4, each written with three options from which Dan chooses. Three kinds
of assessment run in the coding units: reading quizzes, learning checks,
and a unit quiz after each project. What each contains is in
course/formats/; Dan's examples are in sources/assessments/. The tables
below mark where each reading quiz, learning check, and mini-project
falls. The unit quiz is not a numbered lesson; Dan schedules it.

## Where the book and the Codio course do not line up

Codio assignment IDs come from sources/codio_course/
codio_course_reference.md: U6.L4 is Codio Unit 6, lesson 4; U6.LAB is
that unit's lab; U6.EX is its five coding exercises. A "U" always means
a Codio unit. This course's own lessons are written 4.1, with no letter.

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
7. **Not assigned in Units 2, 3, and 4:** U5.L6 (2D lists, except as
   reference for the Unit 4 project's Connect Four option), U6.L2
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
| 4.13 | Project day 1: the option or options Dan chose, write the plan, another pair reviews it. | ch. 12 as project reference, no quiz | U5.L6 as reference for the Connect Four option | none | Unit project begins |
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
- **B. Connect Four.** Two players take turns dropping pieces into a
  board of seven columns and six rows, shown in the terminal after
  every move, until one has four in a row or the board is full. The
  board is a list of lists, and saved positions load from text files.
  It is the brief Dan ran in spring 2026; it replaced a codebreaker
  option on 2026-10-08, and UNIT_4_PLAN.md says what the option needs.
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
and objects, and windows and buttons with tkinter. Recursion is fixed for fall because the
catalog lists it and fall students have not been taught it.

**Final project.** Student's choice, and it must go beyond what the
course covered. Proposals are due during the speed run. Presentations
finish by the last full week of classes, which in fall 2026 ends
December 4. The final-exam period is not used.
