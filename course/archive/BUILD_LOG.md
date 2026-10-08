# Build log

Moved here on 2026-10-08, in the governance audit, from course/BUILD_PLAN.md,
unchanged: the status narrative, the open list as it stood, step 0, and the
sections of the finished packages S0, T0, U4-PLAN, U4-A, U4-B, and U4-DP, with
the items the live repository added on 2026-10-08 at the end. It is
history, not instruction. Its citations of "CLAUDE.md section 6" refer to the
charter as it was then; the formats are now in course/formats/. The live notes
that were in the open list moved to course/packages/ (U4-C.md, REV-4.md), to
course/formats/STUDENT_FACING.md (the slide maker workarounds), and to
tools/plan_check.py's manual (the expected notes).

## Where things stand (2026-10-07, after packages S0, T0, U4-PLAN, U4-A, R on U4-A, U4-B, U4-DP, and R on U4-B)

- The outline is approved. Lesson materials exist for 4.1 to 4.8: for
  each lesson a plan, a deck, and a Canvas page, plus the unit's
  Canvas page, three reading quizzes with their Codio files, one
  learning check, one Codio fix, and the unit's Plickers sheet.
- Package S0 is done. Everything Dan approved in step 0 is now in
  DECISIONS.md and CLAUDE.md: the coding content is Units 2, 3, and 4
  with data structures as Unit 4, each unit has reading quizzes,
  learning checks, and a unit quiz, and the formats for learning
  checks, unit quizzes, review guides, mini-projects, and project
  documents are in CLAUDE.md section 6. The eight carried-over entries
  in DECISIONS.md are confirmed and dated. course/COURSE.md has the
  corrected Codio course name and the "Labs/Learning Checks" category.
- Package T0 is done. tools/plan_check.py makes Python Tutor links and
  checks finished materials; "The checking tool" under "Facts packages
  need" says how to use it.
- Package U4-PLAN is done. units/04-data-structures/UNIT_4_PLAN.md
  is APPROVED (2026-10-05) with Dan's answers recorded at its end.
  One item in it is open for U4-D: how much lighter the project's
  stages run, following Dan's FEEDBACK.md note on the text adventure.
- Package U4-A is done: lessons 4.1 to 4.4, QUIZ_4.2 and QUIZ_4.3, and
  the first questions on materials/PLICKERS_4_Questions.md. Dan's
  answers to its report are in UNIT_4_PLAN.md (`not in` at 4.2) and
  DECISIONS.md (two entries dated 2026-10-05).
- Dan's answers on 2026-10-06, already applied: the chapter 7 reading
  quiz moved from 4.1 to 4.2 (the file is now QUIZ_4.2, and
  UNIT_4_PLAN.md records the answer); a lesson plan has no length limit
  (CLAUDE.md section 6 and "Done when" no longer give one); the Codio
  U6.L5 Formative Assessment 2 check was dropped from LP_4.4 (back
  later the same day; see the next item).
- Codio fixes are a category of material (DECISIONS.md, 2026-10-06;
  format in CLAUDE.md section 6). The first is
  units/04-data-structures/materials/CODIO_FIX_4.4_String_Comparison.md:
  it deletes one U6.L5 page, replaces another, changes one line on a
  third, and has a replacement for Formative Assessment 2. Dan chose
  to keep the step that checks that question's key, and LP_4.4's
  Preparation list points at the fix.
- Package R on U4-A is done (2026-10-06), including the lesson 4.4
  Codio fix. It found the keys and answers right and made five small
  fixes: a try-it key in LP_4.1, a comment in LP_4.2, the U6.EX
  problem 4 pitfall and two Codio notes in LP_4.4, and the 4.4 peer
  instruction note in UNIT_4_PLAN.md. QUIZ_4.2 partly rewards coming
  to lesson 4.1; Dan kept it that way, and its header says so.
- Package U4-B is done (2026-10-06): lessons 4.5 to 4.8, QUIZ_4.5,
  CHECK_4.6_Strings_And_Lists, and these lessons' questions on
  materials/PLICKERS_4_Questions.md. No Codio fix was needed. The
  check's fourth question draws on U6.EX problem 5. Dan's four
  answers to its report are in UNIT_4_PLAN.md (items 8 to 11); the one
  that changed a file added a reminder about `range` with a step to
  LP_4.4's Codio section and LP_4.5's Preparation list. Package R
  reviewed it on 2026-10-07; see the R on U4-B item below.
- The materials pipeline is wired up (2026-10-06). pipeline.yml at the
  top of this repo holds the course settings, and CLAUDE.md section 6
  says how to run the makers. Turning a finished file into a Word
  file, Canvas page or deck is a separate step from writing it; a
  package does it only when Dan asks, and the output goes in
  rendered/, which git ignores. On 2026-10-07 Dan asked for all of
  4.1 to 4.8: every plan as a Word file and PDF, every deck as a
  PowerPoint file and PDF, and every Canvas page and the unit page as
  HTML are in rendered/. A file edited after its output was made is
  made again before Dan uses it.
- Peer instruction changed on 2026-10-07 (DECISIONS.md): a lesson
  that runs Plickers runs two or three questions, together in one
  Concept step and numbered in the order to run them, instead of one
  question with spares. Lessons 4.1 to 4.8 each carry three; nine new
  questions were written for CS4120 and confirmed by running the code.
  The Plickers sheet is renumbered with a per-question key, and
  UNIT_4_PLAN.md proposes the sets for 4.9 to 4.12 for package U4-C.
- Package U4-DP is done (2026-10-07, in sessions with Dan rather than
  as a cold package). It added two kinds of artifact, both recorded
  in DECISIONS.md and CLAUDE.md section 6 that day, and wrote them for
  lessons 4.1 to 4.8:
  - A **deck** per lesson (`DECK_4.1` to `DECK_4.8`), written after
    the plan and copying it, in the slide order CLAUDE.md section 6
    lists. The comparison table is projected with its full four-column
    frame from 4.1 (DECISIONS.md, 2026-10-07), and a table that grows
    is two slides, before and after, until the slide maker can reveal
    cells. LP_4.1, LP_4.4, LP_4.5, and the unit plan were edited to
    match.
  - A **Canvas page** per lesson (`PAGE_4.1` to `PAGE_4.8`) and the
    unit's page, `PAGE_4_Unit.md`. The pages carry what happened in
    class, the links the plan says to post, and the deck's Tonight
    list, and never say when anything is due. The Preparation list of
    each plan that posts something now names its page.
  - **Reading quizzes run in Codio** (DECISIONS.md, 2026-10-07,
    closing the open entries of 2026-09-27 and 2026-10-05). The quiz
    file stays the master; its Codio files were made with the
    codio-mcq skill into `rendered/codio/QUIZ_4.2_Iteration_And_Search/`,
    `rendered/codio/QUIZ_4.3_Strings/`, and
    `rendered/codio/QUIZ_4.5_Lists/`, each a guide page and one JSON
    (JavaScript Object Notation) file per question. LP_4.2, LP_4.3, and
    LP_4.5 tell Dan to put them in Codio. course/COURSE.md and
    COURSE_OUTLINE.md were updated the same day.
- Package R on U4-B is done (2026-10-07). It covered lessons 4.5 to
  4.8, QUIZ_4.5, CHECK_4.6, the Plickers sheet, and the decks, Canvas
  pages, and Codio quiz files for 4.1 to 4.8, including the nine
  questions U4-DP wrote for 4.1 to 4.8. Every key, answer, Codio claim,
  and word list was right. Small fixes: four Overviews (4.5 to 4.8)
  and LP_4.5's Connections still spoke of one peer instruction
  question; one wrong-answer line in LP_4.2's question 3; LP_4.2's
  spare now carries the sentence about `\n` that the Plickers sheet
  has; DECK_4.1's note on which lesson fills the String rows; a teacher
  line moved off a DECK_4.7 slide; and lesson numbers taken out of the
  body of PAGE_4.1, 4.4, 4.6, and 4.7 and DECK_4.7's Tonight slide.
  Dan's answers to its report, the same day: he makes the learning
  check slide himself; decks and pages may reword the plan's
  teacher-facing text for students; titles keep the spring numbering
  (three DECISIONS.md entries, with CLAUDE.md section 6 to match). And
  lesson 4.3 now fills the table's two String rows on position and
  order, leaving 4.4 one cell: LP_4.3, LP_4.4, DECK_4.3, DECK_4.4,
  PAGE_4.3, and UNIT_4_PLAN.md were edited. Outputs in rendered/ for
  every file named in this item are older than the markdown.
- **Next:** U4-C (needed October 26), which writes decks, pages, and
  Codio quiz files along with its plans.

**Open after U4-A, U4-B, and U4-DP:**

- For Dan, before October 12: run one saved Thonny file that opens
  `words.txt` on your own laptop (LP_4.2 Preparation).
- For Dan, before each lesson: post its Canvas page, and for 4.2, 4.3,
  and 4.5, put the reading quiz's Codio files into the Codio
  assignment and link it from Canvas (each plan's Preparation list).
- For Dan, before assigning U6.L5 at lesson 4.4: make the edits in
  CODIO_FIX_4.4_String_Comparison.md, including the Formative
  Assessment 2 key check (LP_4.4 Preparation).
- For the pipeline repo (~/Documents/projects/pipeline): the decks
  want two things the slide maker does not do yet, table cells that
  appear on click and a box around a revealed list; the ask is written
  up in that repo's test_output/README.md. Until then a growing table
  is two slides, before and after. Also found while writing decks 4.2
  to 4.8: in the cfe slide style, a list item made only of inline code
  renders tiny, so each such item carries a few plain words after the
  code, changed in the plan first. That one is not yet reported there.
- For REV-4: UNIT_4_PLAN.md's "Fall 2026 lines" lists the 4.2 file
  setup and 4.4's `ord` and `chr` as fall-only, but spring needs both.
  LP_4.2 and LP_4.4 leave them unlabeled, and REV-4 should keep them.
  The chapter 7 quiz moved to 4.2 because 4.1 is the first class after
  fall 2026's Fall Break; REV-4 may move it back for spring.
- For Dan, before assigning U5.EX at lesson 4.7: remove problem 5.
  Before assigning U8.EX at lesson 4.8: remove problems 1 and 4 (LP_4.7
  and LP_4.8 Preparation).
- For U4-C: CHECK_4.11 may not repeat a Quick check. LP_4.6's is a
  `pop` and `append` trace, LP_4.7's is `'-'.join(sorted('cab'))`, and
  LP_4.8's is `y = x`, `y.append(3)`, `x = [0]`. `t = t.append(x)` as
  an explain-and-fix question is still unused. Lesson 4.5's partner
  challenge taught the index loop that U5.EX problem 1 needs.
- For whoever next edits tools/plan_check.py or this file: `check`
  flags the two example Python Tutor links under "Facts packages need"
  ("no python block above this link"). That predates U4-A and still
  stands on 2026-10-07. `check` also prints a note, not a failure, for
  each code block on a Canvas page that has a Python Tutor link and no
  output block under it (PAGE_4.3 and PAGE_4.8); those blocks are
  there for their links, and the note is expected. The same note on a
  deck (DECK_4.1, 4.3, and 4.4) marks a code block in a question or a
  try-it prompt whose answer comes on a later slide, and is expected
  too.

## Step 0: what is still open

Dan answered items 0.1 to 0.5 and 0.7 on 2026-10-05, and package S0
applied them. Only 0.6 is left.

- **0.6 Speed-run tasters for fall 2026,** from the outline's list.
  Recursion is one of the six, because the catalog lists it and fall
  students have not been taught it. Dan has chosen three so far
  (recursion, classes and objects, and windows and buttons with
  tkinter). The other three, and whether recursion gets the 90-minute
  meeting, come from Dan when package U5-S runs. Sessions do not list
  this as an open item for him before then (Dan, 2026-10-06).

  Dan: recursion, basic classes/objects and gui's like tkinter are decided so far

Already answered on 2026-10-05, and recorded in
units/02-python-foundations/UNIT_2_AS_TAUGHT.md: fall students have
used `for` only over `range`, and they have watched Dan use Python
Tutor for about a week without driving it themselves. The Codio page
checks are done; the results are the outline's table "Codio pages
that run ahead of class."

### S0: apply what Dan approved

Done 2026-10-05. It moved the approved ledger entries into
DECISIONS.md, dated the eight carried-over entries, made the approved
edits to CLAUDE.md and course/COURSE.md, marked COURSE_OUTLINE.md
approved, updated README.md, and trimmed step 0 above to the one open
item. The git history has the details.

### T0: the checking tool

Done 2026-10-05. It wrote tools/plan_check.py; "The checking tool"
under "Facts packages need" says what it does and how packages use
it. The link it makes for the four-line aliasing demo matches the one
Dan verified, byte for byte. It passed on a sample plan written for
the test and failed on a copy with one wrong output and one altered
link, flagging exactly those two. The sample files were not kept in
the repository.

### U4-PLAN: the Unit 4 plan

Done 2026-10-05, in a session with Dan rather than as a cold package,
so his answers went straight into the plan. The plan is APPROVED. Its
one open item, the project's stages, waits under "Project" for U4-D.
The unit's Canvas page, `PAGE_4_Unit.md`, was added on 2026-10-07 by
package U4-DP; later unit plan packages write theirs with the plan.

**Writes:** `units/04-data-structures/UNIT_4_PLAN.md`, in the CLAUDE.md
section 6 unit-plan format, from the outline's Unit 4 section.

Beyond the standard format, the plan carries six things the later
packages depend on:

1. A "new in this lesson" column: every Python feature and every term
   introduced, lesson by lesson. Later packages may use only what this
   column has introduced, plus what Units 2 and 3 taught.
2. The peer instruction assignments: for each concept lesson, the bank
   question chosen (deck and slide), one or two spares, or "new." Each
   question appears once in the unit.
3. The comparison table of strings, lists, dictionaries, and tuples,
   complete, with a note of which row each lesson adds.
4. Which fall 2026 lessons need a line or two more because of what
   UNIT_2_AS_TAUGHT.md says fall students have not seen.
5. The two learning checks, at 4.6 and 4.11: the lessons each covers,
   the assignment or mini-project its fourth question draws on, and
   when that work is due, which must be before the check.
6. The unit quiz: that it comes after lesson 4.16, that Dan schedules
   it, and when the Codio review guide is assigned.

**Status line:** if the plan matches the approved outline with no
departures, it is written as "APPROVED with COURSE_OUTLINE.md" and the
approval date. Any departure makes it a PROPOSAL, and U4-A waits for
Dan.

### U4-A: strings (lessons 4.1 to 4.4)

**Writes:** `LP_4.1` through `LP_4.4` in units/04-data-structures/
lessons/; `QUIZ_4.1` (chapter 7; moved to 4.2 as `QUIZ_4.2` on
2026-10-06) and `QUIZ_4.3` (chapter 8, through
"String methods") in assessments/.

**Specific to this package:**

- Fall students have used `for` only over `range`. Looping over a
  string directly, with no `range` and no index, is the one new idea
  in lesson 4.1, and the plan says so.
- Fall students have watched Dan step through code in Python Tutor
  for about a week and have not driven it. The 4.1 demo needs no
  introduction to the tool. The first time they step through code
  themselves is in this package, in 4.3 or earlier, so that lesson
  4.8 is not their first time.
- Codio's U6.L4 is assigned at 4.1, but its pages 324 and 328 loop
  with `while` and `word[index]`. The plan says students may stop
  there and finish after 4.3.
- Lesson 4.2 needs `words.txt` on student laptops. The plan's
  Preparation section says where the file comes from and where
  students save it so Thonny finds it.
- Fall students already put `.strip().lower()` on `input()` in the
  text adventure. Lesson 4.4 starts from those two methods and asks
  why `.lower()` did not change the original string.
- The Caesar cipher mini-project in 4.4 is written with the methods
  chapter 8 teaches. If it needs `ord` and `chr`, the plan says they
  are new and shows them.
- The Codio Unit 6 exercises read `input()` and fail if the program
  prints a prompt. That goes in Pitfalls for 4.4.

### U4-B: lists (lessons 4.5 to 4.8)

Done 2026-10-06. Reviewed by package R on 2026-10-07.

**Writes:** `LP_4.5` through `LP_4.8`; `QUIZ_4.5` (chapter 9);
`CHECK_4.6`, the learning check on lessons 4.1 to 4.5.

**Specific to this package:**

- Lesson 4.5 opens by re-running string code from 4.1 to 4.3 on a
  list, unchanged, before showing the one difference.
- Codio's U5.L1 shows list comprehensions on page 179. The 4.5 plan
  says class does not teach them and students can skip that page.
- Lesson 4.6 covers the bug `t = t.append(x)`, which leaves `t` as
  `None`. It also opens with the learning check, so its plan marks
  what to shorten.
- The learning check's fourth question draws on the work the unit plan
  named (U6.LAB, U6.EX, or the lesson 4.4 mini-project). Read that
  assignment's pages in the export and build the question on the place
  a student gets stuck doing it alone.
- Every U5.EX problem begins with `import sys` lines for the
  autograder. Pitfalls for 4.7 says students leave them alone.
  Problem 5 is waived because it needs a 2D list.
- Lesson 4.8 is the lesson Python Tutor serves best. Students drive
  it. The plan gives three links, not one.
- U8.EX is assigned at 4.8 with problem 4 waived (it needs CSV files).
  U12.EX joins it in spring; package REV-4 adds that, not this one.

### U4-DP: decks, pages, and Codio quiz files for 4.1 to 4.8

Done 2026-10-07, in sessions with Dan rather than as a cold package,
while the deck and Canvas page artifacts were being defined. It wrote
`DECK_4.1` to `DECK_4.8`, `PAGE_4.1` to `PAGE_4.8`, and `PAGE_4_Unit.md`;
made the Codio files for `QUIZ_4.2`, `QUIZ_4.3`, and `QUIZ_4.5` into
rendered/codio/; and edited the plans so each slide and page has its
words in the plan (the comparison table's full frame at 4.1, a few
plain words after any list item that was only inline code, and the
Preparation steps that post the page and put the quiz in Codio). It
also carried the Plickers change of the same day into lessons 4.1 to
4.8 and the Plickers sheet. "Where things stand" has the details.
Later lesson packages do this work as part of writing their lessons,
so this package is not repeated.

## Added in the live repository on 2026-10-08

Written by the sessions that ran U4-C and R on U4-C and applied Dan's
Connect Four decision, before the audit's port. Verbatim from
course/BUILD_PLAN.md as it stood that day.

- Package U4-C is done (2026-10-08): lessons 4.9 to 4.12, each with
  its deck and Canvas page; QUIZ_4.9 and QUIZ_4.12 with their Codio
  files in rendered/codio/; CHECK_4.11_Lists_And_Dictionaries, whose
  fourth question draws on U5.EX problem 4; and twelve questions on the
  Plickers sheet (three Taylor, nine written for CS4120). Dan's answers
  the same day: these four lessons are written as they run in spring,
  with no fall lines (he handles fall in the room), so chapter 10 is
  read whole, "Memos" included, and QUIZ_4.9 has a question on it;
  U10.EX keeps problems 3 and 4, which use `isinstance`; and
  `words.txt` is just a file the course uses, so the 2026-10-05 ledger
  rule about checking and narrowing printed word lists was removed,
  along with the notes in lessons 4.2, 4.7, and 4.11 that followed
  from it.
- Package R on U4-C is done (2026-10-08). It covered lessons 4.9 to
  4.12, QUIZ_4.9, QUIZ_4.12 and their Codio files, CHECK_4.11, the
  Plickers sheet, and the four decks and Canvas pages. Every key,
  answer, Codio page claim, and error message was right, and the Codio
  files match their quizzes. Small fixes: LP_4.9's description of how
  Python Tutor draws a dictionary and its line on `values()`; a lesson
  number in a code comment on LP_4.10 and DECK_4.10; the anagram
  brief in LP_4.11 and DECK_4.11, which assumed every student built
  the 4.7 anagram finder; and in LP_4.12, a line that assumed every
  student did 4.5's swap ceiling and a typo in Extras. UNIT_4_PLAN.md
  now reads chapter 10 whole, "Memos" included, and records Dan's
  answer of 2026-10-08 on writing for spring as its answer 13.
- Dan's decision of 2026-10-08, applied the same day: the project's
  option B is Connect Four, from the brief he ran in spring 2026, in
  place of the codebreaker. The brief is in
  sources/connect_four_spring_2026/, UNIT_4_PLAN.md's "Project"
  section says what the option needs (answer 14), and the outline,
  LP_4.4, LP_4.10, and LP_4.12 with its deck and page were updated.
- **Next:** U4-D (needed November 3). The project's lighter stages in
  UNIT_4_PLAN.md are approved (2026-10-08).

### U4-C: dictionaries and tuples (lessons 4.9 to 4.12)

Done 2026-10-08.

**Writes:** `LP_4.9` through `LP_4.12`; `QUIZ_4.9` (chapter 10) and
`QUIZ_4.12` (chapter 11, the sections lesson 4.12 uses); `CHECK_4.11`,
the learning check on lessons 4.6 to 4.10. With them, the four decks,
the four Canvas pages, and the Codio files for both quizzes.

**Specific to this package:**

- The peer instruction sets for 4.9 to 4.12 are proposed in
  UNIT_4_PLAN.md's "Peer instruction" table, two or three questions a
  lesson. The package writes them from that table and Dan sees them in
  the report.
- Lessons 4.9 and 4.12 add a column to the comparison table. Each deck
  shows the table before and after, with the full frame, as decks 4.1
  and 4.5 do.
- Taylor's bank has three dictionary questions and none on tuples.
  Most questions here are new, so each one's wrong answers need extra
  care.
- Chapter 10 has a section called "Memos" that speeds up the recursive
  Fibonacci function from chapter 6 with a dictionary. Fall 2026
  students have not been taught recursion, so the 4.9 plan tells them
  to skip that section, and `QUIZ_4.9` asks nothing from it. Nothing
  else in chapters 7 to 12 needs recursion except one exercise in
  chapter 11, which is not assigned.
- Codio's U10.L1 uses tuples as dictionary keys on its hashing page.
  The 4.9 plan gives Dan one sentence to say about that.
- Codio's U10.L2 uses `for key, value in d.items()` before lesson
  4.12, and has a section on dictionary comprehensions that class does
  not teach. The 4.10 demo shows the `items()` line and ties it to
  what fall students did in the text adventure, where one call gave
  back three values to three names.
- Lesson 4.11's comparison of `in` on a list and on a dictionary is
  acted out by students first and timed on `words.txt` second. Codio's
  U10.L3 ends with the same timing. Lesson 4.11 also opens with the
  learning check, so its plan marks what to shorten.
- The learning check's fourth question draws on the work the unit plan
  named (U5.LAB, U5.EX, or U8.EX).
- Lesson 4.12 names what fall students have already written:
  `return message, health, treasure` returns a tuple.
- Codio's Unit 10 exercises wrap their tests in
  `if __name__ == "__main__":`. Pitfalls for 4.12 says what that line
  is and that students leave it alone. Problem 5 is waived because it
  needs JSON files.
