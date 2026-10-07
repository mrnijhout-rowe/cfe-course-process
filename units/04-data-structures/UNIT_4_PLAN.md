# Unit 4 Plan: Data Structures

Status: APPROVED 2026-10-05. Dan answered the plan's questions that
day; his answers are folded into the text and recorded at the end.
One item stays open for package U4-D, under "Project": how much
lighter the project's stages run than the text adventure's. Lessons
4.1 to 4.12 do not depend on it. Written from the Unit 4 section of
course/COURSE_OUTLINE.md (APPROVED 2026-10-05) with the six additions
course/BUILD_PLAN.md asks of package U4-PLAN. Where this plan goes
beyond the outline, "Departures from the outline" at the end says so.

Think Python means Think Python, 3rd edition. Codio codes such as
U6.L4 come from sources/codio_course/codio_course_reference.md: U6.L4
is Codio Unit 6, lesson 4; U6.LAB is that unit's lab; U6.EX is its
five coding exercises.

## Scope

**In.**

- Chapter 7, all but "Doctest": `for` over a string, reading
  `words.txt` a line at a time, `+=`, counting, `in`, and a search that
  returns from inside a loop.
- Chapter 8 through "String methods": indexing, negative indices,
  slices, immutability, string comparison, methods that return a new
  string.
- Chapter 9, all of it: lists, mutability, slices, `+` and `*`, `sum`,
  `min`, `max`, list methods, `split` and `join`, `sorted`, objects and
  values, aliasing, list arguments, making a word list.
- Chapter 10, all but "Memos": dictionaries, `in`, a dictionary of
  counters, looping over a dictionary, a dictionary whose values are
  lists, accumulating a list.
- Chapter 11, five sections: "Tuples are like lists," "But tuples are
  immutable," "Tuple assignment," "Tuples as return values," and "Zip."
  "Zip" is for pairs who are ready.

**Mentioned only** (a sentence or a pointer, no practice): regular
expressions and writing files (chapter 8), sets, `enumerate`, lists of
lists (Codio U5.L6), `try` and `except`, list and dictionary
comprehensions (they appear in Codio pages), `del`, `while` with an
index over a string (Codio U6.L4).

**Out.** Chapter 8 from "Writing files" on. Chapter 10 "Memos," which
needs recursion. Chapter 11 "Argument packing," "Comparing and
Sorting," and "Inverting a dictionary." Codio U5.L6, U6.L2, Unit 7,
U8.LAB, U9.L2 to U9.L4 with U9.LAB and U9.EX, U10.L4, and Unit 11.
U10.LAB (ASCII art with the Pillow library) is optional enrichment.

**Where fall 2026 students start.** See
units/02-python-foundations/UNIT_2_AS_TAUGHT.md. They write functions
with return values, `if`/`elif`/`else`, `while`, `input()` with
`.strip().lower()`, and f-strings. They have used `for` only over
`range`. They have watched Python Tutor and not driven it. They have
not had recursion, turtle, or a nested-loops lesson.

Dan said on 2026-10-05 that fall students have seen `%`, so the
Caesar cipher at 4.4 and Codio U8.EX problem 2 need no line for it,
and that `+=` was mentioned only in passing. `len` was not asked
about on its own. Lesson 4.1 treats `+=` and `len` as new, which
costs a sentence each if students already know them.

## Lessons

Sixteen lessons: twelve of content, four of project. Fall 2026 weeks 8
to 11 (October 12 to November 6); spring 2027 weeks 9 to 12. Each
Codio entry says when it is due; "due 4.6" means before class on
lesson 4.6. Codio lessons are started in the last ten minutes of class
and finished that night. A lab or exercise set is due two lessons
after it is assigned.

| # | Title | Concept (one idea) | Reading due | Codio | Quiz or check | Outside Codio |
|---|---|---|---|---|---|---|
| 4.1 | A string is a sequence | `for letter in word` visits every character, with no `range` and no index | none | U6.L4, its "for loop" pages, due 4.2; its "while loop" pages after 4.3, due 4.4 | none | Mini: a letter counter. The comparison table starts. |
| 4.2 | Search | A loop that answers yes or no: `return True` inside the loop, `return False` after it. The loop runs over `words.txt`. | ch. 7 | none | reading quiz | Mini: a Spelling Bee helper, or the words with no "e" |
| 4.3 | Indexing and slicing | Positions start at 0, a slice stops before its end, and `IndexError` names the position that is not there | ch. 8 through "String methods" | U6.L1, due 4.4 | reading quiz | Python Tutor demo, then students drive it for the first time |
| 4.4 | Strings cannot be changed | A method returns a new string and leaves the old one alone, so you build a new string in a loop | none | U6.L3 and U6.L5, due 4.5; U6.LAB and U6.EX, due 4.6 | none | Mini: a Caesar cipher, Pig Latin, or a palindrome checker |
| 4.5 | Lists: the same rules, one difference | Everything from 4.1 to 4.3 runs on a list unchanged; a list can be changed in place | ch. 9 | U5.L1 and U5.L2, due 4.6 | reading quiz | Python Tutor demo. Table: lists. |
| 4.6 | List methods | `append` changes the list and returns `None`; a list built in a loop; `sum`, `min`, `max` | none | U5.L3, U5.L4, U5.L5, due 4.7; U5.LAB, due 4.8 | **learning check** on 4.1 to 4.5 | Mini: a dice-roll histogram or a playlist manager |
| 4.7 | Lists and strings | `split` turns a string into a list and `join` turns it back; `sorted` gives a new list | none | U5.EX with problem 5 removed, due 4.9 | none | Mini: an anagram finder or a word scramble |
| 4.8 | Aliasing | Two names, one list; a function that changes a list changes the caller's list | none | U8.EX with problems 1 and 4 removed (spring: 4 only), due 4.10; U12.EX in spring | none | Students drive Python Tutor, three links |
| 4.9 | Dictionaries | A key in place of a position; `KeyError` | ch. 10, skipping "Memos" | U10.L1, due 4.10 | reading quiz | Python Tutor demo. Table: dictionaries. |
| 4.10 | A dictionary of counters | `if key not in d: d[key] = 1`, `else: d[key] += 1`; `for key in d` | none | U10.L2, due 4.11 | none | Mini: letter frequencies of a text you pick |
| 4.11 | Dictionaries holding lists | A value can be a list; `in` on a dictionary is fast, and the class times it | none | U10.L3, due 4.12 | **learning check** on 4.6 to 4.10 | Mini: anagram families or a Scrabble scorer |
| 4.12 | Tuples | `a, b = b, a`; a function that returns two values returns a tuple; `.items()` | ch. 11, the five sections | U9.L1, due 4.13; U10.EX with problem 5 removed, due 4.14 | reading quiz | Table: tuples. The table is complete. |
| 4.13 | Project day 1 | Brief, write the plan, another pair reviews it | ch. 12 as reference for option A only | none | none | Project begins |
| 4.14 | Project day 2, first half | Sign-off, work plan, comments before code | none | none | none | Project |
| 4.15 | Project day 2, second half | Code | none | none | none | Project |
| 4.16 | Project day 3 | Finish, another pair runs and reviews it, fix, turn in | none | none | none | Project due. Reflection is homework. Review guide assigned. |

Lessons 4.14 and 4.15 are one 90-minute meeting when the timetable
allows.

**Heavy nights.** After 4.4, students have U6.L3 and U6.L5 (due 4.5)
and then U6.LAB and U6.EX (due 4.6, with a weekend in between in fall
if 4.4 lands late in week 8). After 4.5, they have U5.L1 and U5.L2 on
top of finishing the Unit 6 lab and exercises.

Dan confirmed this load on 2026-10-05.

**File names.** `LP_4.1_String_Sequence`, `LP_4.2_Search`,
`LP_4.3_Indexing_Slicing`, `LP_4.4_Strings_Do_Not_Change`,
`LP_4.5_Lists`, `LP_4.6_List_Methods`, `LP_4.7_Lists_And_Strings`,
`LP_4.8_Aliasing`, `LP_4.9_Dictionaries`, `LP_4.10_Counters`,
`LP_4.11_Dictionaries_Of_Lists`, `LP_4.12_Tuples`,
`LP_4.13_Project_Day_1`, `LP_4.14_Project_Day_2a`,
`LP_4.15_Project_Day_2b`, `LP_4.16_Project_Day_3`. Reading quizzes:
`QUIZ_4.2`, `QUIZ_4.3`, `QUIZ_4.5`, `QUIZ_4.9`, `QUIZ_4.12`. Checks:
`CHECK_4.6`, `CHECK_4.11`. Project: `PROJECT_4_Data_Structures` and
its separate files. Quiz: `QUIZ_4_Unit_Quiz` and
`materials/CODIO_4_Quiz_Review/`. Plickers sheet:
`materials/PLICKERS_4_Questions.md`.

## New in this lesson

Later packages may use, in student-facing code and sample solutions,
only what this table has introduced by that lesson, plus what Units 2
and 3 taught. "Shown" means it appears in the demo or a key with one
line of explanation and is not practiced.

| # | Python introduced | Terms introduced |
|---|---|---|
| 4.1 | `for letter in word`; `in` on a string; `len`; `+=`; `print(x, end=' ')` | sequence, character, counter |
| 4.2 | `open('words.txt')`; `for line in file`; `line.strip()` on a line; `return` inside a loop; `not in` (shown) | search, file, line |
| 4.3 | `word[0]`, `word[-1]`; `word[2:5]`, `word[:3]`, `word[3:]`; `IndexError`; `<` and `>` on strings (shown) | index, position, slice |
| 4.4 | `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.count()`; `TypeError` from `word[0] = 'x'`; `new = new + letter` in a loop; `ord` and `chr` (Caesar option only, shown) | immutable, a method returns a new value |
| 4.5 | `[1, 2, 3]`, `[]`; `t[1] = x`; `+`, `*`, `in`, `len`, and slices on a list; `for item in t` | list, element, mutable, in place |
| 4.6 | `.append()`, `.pop()`, `.remove()`, `.extend()`; `sum`, `min`, `max`; the bug `t = t.append(x)`; `random.randint` (mini only, shown) | returns `None` |
| 4.7 | `.split()`, `.join()`, `list(s)`, `sorted()`, `.sort()`, `reverse=True` | delimiter |
| 4.8 | `b = a` on a list; `is` (shown); `list(a)` or `a[:]` as a copy; a list as an argument; `open('words.txt').read().split()` | alias, object, reference |
| 4.9 | `{}`, `{'a': 1}`; `d['a']`; `d['b'] = 2`; `in` on a dictionary tests keys; `len(d)`; `KeyError` | dictionary, key, value, mapping, look up |
| 4.10 | the counter pattern; `for key in d`; `d.values()`; `for key, value in d.items()` shown and named at 4.12 | counter, frequency |
| 4.11 | `d[key] = []` then `d[key].append(x)`; `.get(key, default)`; `d.keys()`; `list(d)` | a dictionary of lists, hashing (one sentence) |
| 4.12 | `(1, 2)` and `1, 2`; `a, b = b, a`; `low, high = f()`; `tuple()`; `.items()` named; ceiling: `zip`, `enumerate` | tuple, unpacking |

Not introduced anywhere in the unit, so not used in keys: nested
loops (fall students have not had lesson 3.7; a ceiling variant may
use one and says so), `while` with an index over a sequence, `break`,
`try`/`except`, `isinstance`, list comprehensions, `lambda`, `key=`
in `sorted`, `del`, sets.

## The comparison table

One table grows across the unit. It is projected and students copy
it into the journal, a cell at a time. In 4.1 students copy the whole
frame, with all four columns empty, so they can see that more is
coming (Dan, 2026-10-07). Lessons 4.1 to 4.4 fill the String column:
4.1 the first and last rows, 4.3 the two rows about position and
order, and 4.4 "Can be changed in place" (Dan, 2026-10-07). 4.5 adds
lists, 4.9 adds dictionaries, and 4.12 adds tuples. Lesson
4.12 shows it complete.

| | String | List | Dictionary | Tuple |
|---|---|---|---|---|
| How you write one | `'abc'` | `['a', 'b', 'c']` | `{'a': 1, 'b': 2}` | `('a', 'b')` or `'a', 'b'` |
| How you reach one element | by position: `s[0]` | by position: `t[0]` | by key: `d['a']` | by position: `t[0]` |
| Has an order | yes | yes | keeps the order you added things in, but you look up by key, not by position | yes |
| Can be changed in place | no | yes | yes | no |
| `len`, `in`, `for` | all three; `in` finds a piece of the string; `for` gives each character | all three; `in` finds an element; `for` gives each element | all three; `in` checks the keys; `for` gives each key | all three, as for a list |
| Added in | 4.1 to 4.4 | 4.5 | 4.9 | 4.12 |

## Peer instruction

Two or three questions per concept lesson, run together, from Cynthia
Taylor's bank in sources/peer_instruction/ where it has them. Deck and
slide numbers are hers. Each bank question is used once in the unit.
"New" means written for CS4120 and labeled so. The lesson packages add
every question to `materials/PLICKERS_4_Questions.md`, numbered in the
order the lesson runs them.

*Changed 2026-10-07 (DECISIONS.md): until then each lesson carried one
question, with spares in Extras. Lessons 4.1 to 4.8 now carry the sets
below; the sets for 4.9 to 4.12 are this plan's assignment for package
U4-C, and Dan sees them in that package's report.*

| # | Questions, in the order run | Notes |
|---|---|---|
| 4.1 | new: a trace of a counting loop; new: `len` and `in` on `'banana'`; `11_strings` slide 12: what `mystery(s)` returns (the reverse) | her Q5 in 06_strings.md |
| 4.2 | new: two versions of a search function, one with `return False` inside the loop (chapter 7's `uses_any_incorrect`); new: a `return` inside the loop ends a count at the first "e"; new: `not` in front of the search function. Spare in Extras: `len` of a line before and after `strip`, which fits after Concept step 3 | the bank has nothing on search |
| 4.3 | `11_strings` slide 5 (`s[len(s)-1]`); slide 7 (`s[0:len(s)]`); slide 9: `s[3:-1]` of "Vampires" | slide 9 is missing a closing parenthesis; the lesson adds it and confirms the answer by running the code (Dan, 2026-10-05) |
| 4.4 | new: `word.upper()` with nothing in front of it; new: a loop that doubles each letter; `11_strings` slide 14: which `space_remove` is correct | all three options lack a `return` line (option B needs `return new_s`); VERIFICATION_REPORT.md documents it, so the plan adds one to each. `12_lists` slide 2 is the same question and is not used. |
| 4.5 | `14_Review` slide 12 (valid lists); `12_lists` slide 8: `C = A + B` with "pirate"; `13_morelists` slide 6 (`A * 3`). Spare in Extras: `13_morelists` slide 9 (`for e in A[1:]`) | `12_lists` slide 16 repeats the `A * 3` question |
| 4.6 | new: `len`, `in`, and `[-1]` after two `append` calls; `13_morelists` slide 7: index loop changes the list, element loop does not; `25_review` slide 4: `append` returns `None` | |
| 4.7 | new: `len` and `[0]` of a `split`; new: a `split` and `join` trace; new: `sort` returns `None`. The step runs after `sorted` is shown | the outline said Taylor; the bank has nothing on `split`, `join`, or `sorted` |
| 4.8 | `13_morelists` slide 2: `B = A`, `B[0] = 100`, `C = B + A`; `13_morelists` slide 5 (copy by loop against alias); `12_lists` slide 10 (`inc(A, x)`: the list changes, the number does not). The step runs after lists as arguments are shown | `12_lists` slides 12 and 15 repeat the two `13_morelists` questions |
| 4.9 | `30_DictionariesSets` slide 5 (parallel lists for bird counts) as the problem dictionaries solve; `30_DictionariesSets` slide 8: `d["c"] = 3` then `d["b"] = 4`; new: `len(d)` and `in` on a dictionary, which tests keys and not values | |
| 4.10 | new: a trace of the counter pattern on a short word; new: `for key in d` gives keys, not values; new: what `sum(d.values())` gives | the outline said new |
| 4.11 | `30_DictionariesSets` slide 10: `d.get(4, 8)`; new: `d[key].append(x)` changes the list inside the dictionary; new: `d[key]` on a missing key against `d.get(key, 0)` | needs `.get`, which 4.11 introduces; the outline said new |
| 4.12 | new: `a, b = b, a`; new: unpacking a returned pair, `low, high = f()`; new: `t[0] = 5` on a tuple | |

Not used: `11_strings` slide 3 (string `+` and `*`, a Unit 2 idea),
`13_morelists` slides 10 to 13 (lists of lists), `30_DictionariesSets`
slide 14 (sets), and `10_typesexceptions` slide 12 (`try`). Her two
practice exercises, `11_strings` slide 11 (`num_vowels`) and
`25_review` slide 9 (`min` by hand), are try-it material for 4.1 and
4.6.

## Fall 2026 lines

What UNIT_2_AS_TAUGHT.md says fall students have not seen, and the
lesson that carries a line or two more because of it. Package REV-4
removes these for spring.

- 4.1: the first `for` that is not over `range`. `+=` was mentioned
  only in passing, so it is taught as new, with `len` and
  `print(x, end=' ')`.
- 4.2: the first time a program opens a file. Preparation says where
  `words.txt` comes from and where students save it so Thonny finds it.
- 4.3: the first time students drive Python Tutor. Thirty seconds on
  the Next button is enough; they have watched it for a week.
- 4.4: `ord` and `chr` are new. `%` is known.
- 4.6: `random.randint` appeared in the text adventure's sample program
  and was not taught; the dice mini shows it in one line.
- 4.7 and 4.11: keys use no nested loops. The anagram finder and the
  anagram families each need one loop and a sorted key.
- 4.8: U8.EX problem 1 needs a type check (`isinstance`, chapter 6's
  "Checking types," which spring gets at 3.5). Fall removes problems 1
  and 4; spring removes 4 only.
- 4.9: skip chapter 10 "Memos." `QUIZ_4.9` asks nothing from it. Codio
  U10.L1 uses tuples as keys on its hashing page; the plan gives one
  sentence to say.
- 4.10: `for key, value in d.items()` is tied to the text adventure,
  where one call gave back three values to three names.
- 4.12: students have already written `return message, health,
  treasure`. That is a tuple.
- 4.13: the handout says the stages are the ones the text adventure
  used.

## Learning checks

Format: CLAUDE.md section 6. Each check takes the first ten minutes of
the lesson it is marked on, in place of a reading quiz, and that
lesson's plan says in one line what to shorten. Nothing in a check
comes from the lesson it is marked on or later.

**CHECK_4.6**, on lessons 4.1 to 4.5. Part A: a `for` over a string,
`in` or counting (4.1 or 4.2); an index or slice value (4.3); why
`word.upper()` did not change `word`, or what `t[1] = x` does to a
list (4.4 or 4.5). B1 draws on **U6.EX**, due before 4.6: problem 4
(the first and second half of a word, odd length going to the second
half) or problem 5 (swap characters pairwise) is where a student
working alone gets stuck. If U6.LAB moves to "due 4.7," B1 still
draws on U6.EX. If both move, B1 draws on the 4.4 mini-project.

**CHECK_4.11**, on lessons 4.6 to 4.10. Part A: what `append` returns
or a list built in a loop (4.6); a `split` or `join` result (4.7); an
aliasing trace (4.8) or a dictionary lookup, assignment, or `KeyError`
(4.9). B1 draws on **U5.EX**, due 4.9: problem 1 (replace every
element over 10 with `'*'`, which needs an index loop) or problem 4
(extend a run of numbers by the next two).

Both checks are written to the length of Dan's examples in
sources/assessments/learning_checks/ and grade in about 90 seconds a
journal. They count in Labs/Learning Checks.

## Project

Lessons 4.13 to 4.16, on the plan of the fall 2026 text adventure
(sources/fall_2026_text_based_adventure/): a written plan, review by
another pair, Dan's sign-off before code, a work plan, comments before
code, a second pair's review of the running program, and an individual
reflection graded on its own. Pairs. Written in Thonny. Three options
are written and Dan chooses which a class is offered; each option's
brief is its own file, and the shared handout names no option. Shared
requirements: the program reads a text file, uses a string operation,
a list, and a dictionary where each is the right choice, and is
organized into functions. Rubric-graded, never autograded, under
Projects.

- **A. Text generator.** Count word frequencies in a text, build a
  table of which word follows which, generate new text. Think Python
  chapter 12 as a project.
- **B. Codebreaker.** Write a Caesar cipher, then break one by letter
  frequencies in a real text. Connects to Unit 1.
- **C. Word game.** Wordle, Hangman, or Spelling Bee, with the word
  list from a file and a dictionary that tracks letters or statistics
  across rounds.

Times follow the text adventure's run sheet: 50, 90, and 50 minutes.
In fall that is week 11, November 3 to 6, four calendar days with
Monday out.

Dan confirmed on 2026-10-05 that the rotation puts a 90-minute
meeting in that week.

**Lighter stages [OPEN, settle before U4-D].** Dan's note in
FEEDBACK.md (2026-10-05) on the text adventure: the activities around
the project can carry a little less scaffolding; keep peer critical
feedback during planning and before turn-in; and have partners write
down who is responsible for what as early as possible. The
recommendation below departs from the DECISIONS.md default of
2026-10-05 on project stages, which is allowed for a default and is
noted here.

- Keep: the written plan, reviewed by another pair on a form; a second
  pair's review of the running program before turn-in; the individual
  reflection, graded on its own.
- Add: a partner agreement on the plan page, written on day 1, naming
  which functions each partner writes and who keeps the file. The
  rubric scores it.
- Lighten: Dan's sign-off becomes a look at each plan while walking
  the room, not a gate before typing; the separate work plan folds
  into the plan page; comments before code is a rubric row, not its
  own stage.

Dan: approve as written, or mark what stays as it was in the text
adventure.

## Unit quiz

After lesson 4.16. Dan schedules it; in fall that is week 12 beside
the speed run. About 30 minutes in Canvas: ten to thirteen
multiple-choice questions at 2 points and two short-answer questions
at 7 points, format in CLAUDE.md section 6. About a fifth of the
points come from earlier units; in fall that share uses return values,
`while`, and boolean expressions, which the fall quiz on Units 1 and
2 did not test. It may ask about the project, resting on what every
option shares. The Codio review guide (`materials/CODIO_4_Quiz_Review/`)
is assigned at 4.16 as homework and is due the day of the quiz.
Package U4-Q is needed by November 4.

## Grading summary

| Work | Count | Category |
|---|---|---|
| Reading quizzes (4.2, 4.3, 4.5, 4.9, 4.12) | 5 | Tests and quizzes |
| Learning checks (4.6, 4.11) | 2 | Labs/Learning Checks |
| Codio lessons, labs, and exercises | 12 lessons, 3 labs, 4 exercise sets | Labs/Learning Checks |
| Small mini-projects (4.1, 4.2, 4.4, 4.6, 4.7, 4.10, 4.11) | 7 | not graded |
| Project, with its reflection | 1 | Projects |
| Unit quiz | 1 | Tests and quizzes |

## Calendar and cut points

Fall 2026: week 8 holds 4.1 to 4.4, week 9 holds 4.5 to 4.8, week 10
holds 4.9 to 4.12, and week 11 holds the project. Weeks 8 to 10 have
about 15 lesson slots for 12 lessons, so each week has about one spare
slot. The spare slots are for stretching in the room, not for new
content. The 90-minute meeting each week runs two lessons or one
lesson plus work time; that mapping is Dan's call.

Cut points, in order, applied only if the project would otherwise lose
a day:

1. Fold 4.12 into 4.11 as swap and two return values only. U9.L1 and
   U10.EX are assigned at 4.11. The chapter 11 reading and `QUIZ_4.12`
   are dropped.
2. Merge 4.2 into 4.1: reading `words.txt` becomes a five-minute demo
   at the end of 4.1, and the Spelling Bee mini is dropped. The
   chapter 7 quiz is either dropped or given at 4.3 beside chapter
   8's.
3. Inside a lesson, the first thing to drop is the ceiling variant,
   then the mini-project's second option; 4.11's timing demo goes
   before its mini.

**Final-project pointers:** regular expressions, modern cryptography,
and where the text generator stops and a real language model begins.

## Departures from the outline

1. Peer instruction sources corrected against the bank: 4.7 is new, not
   Taylor; 4.11 is Taylor (slide 10, on `.get`), not new; 4.4 has one
   Taylor question and no spare; 4.1 has a Taylor question (slide 12)
   as its main one.
2. `.get(key, default)` is placed at 4.11, not 4.10, so that 4.10 stays
   on one idea and 4.11 has a bank question.
3. Codio due dates are stated lesson by lesson; the outline gave only
   where each assignment is assigned.
4. U8.EX problem 1 is removed in fall as well as problem 4.
5. The chapter 11 sections for 4.12 are named: five in, three out.
6. Students first drive Python Tutor at 4.3.
7. The project's stages run lighter than the ledger's default, following
   Dan's FEEDBACK.md note of 2026-10-05. Open until Dan approves the
   list under "Project."

## Dan's answers

Kept as written. Each is applied above.

1. Which of `%`, `+=`, `len` have fall students met?

   Dan: They have seen `%` but and `+=` has been mentioned but only in passing.

2. Is the Codio load after 4.4 and 4.5 right, or should U6.LAB move to
   due 4.7?

   Dan: That load is right.

3. May the lesson add the missing closing parenthesis to Taylor's
   `11_strings` slide 9?

   Dan: Yes, just verify with code that the correct answer is provided

4. Does the rotation put a 90-minute meeting in November 3 to 6?

   Dan: Yes

5. How did the text adventure go? Dan wrote the entry in FEEDBACK.md
   the same day.

Asked in chat on 2026-10-05, after package U4-A:

6. Lesson 4.2's Spelling Bee key and lesson 4.4's demo use `not in`,
   which the "New in this lesson" table did not list until 4.10. Add it
   at 4.2?

   Dan: Yes, put it in.

Asked in chat on 2026-10-06:

7. Chapter 7 is due at 4.1, the first class after Fall Break. Keep the
   reading quiz there, or move it?

   Dan: Move the reading quiz to 4.2.

Asked in chat on 2026-10-06, after package U4-B:

8. CHECK_4.6's fourth question expects `range(0, len(word), 2)`. Have
   fall students used `range` with a step?

   Dan: they have but will need a reminder of it.

   Applied: LP_4.4's Codio section gives the reminder when U6.EX is
   assigned, and LP_4.5's Preparation list backs it up.

9. QUIZ_4.5 question 5 asks about equivalent and identical lists, from
   the part of chapter 9 that class reaches at 4.8. Keep it?

   Dan: keep it

10. CHECK_4.6's A3 tests the idea behind lesson 4.4's Quick check with
    different code. Too close?

    Dan: not too close, keep it

11. Lesson 4.5's partner challenge teaches changing a list with a loop
    over positions, which makes the spare peer instruction question at
    4.6 a recap. All right?

    Dan: Yes
