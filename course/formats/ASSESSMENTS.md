# Assessments: formats

Reading quizzes, learning checks, unit quizzes, and quiz review guides.
Defaults unless marked **[RULE]**; each cites its ledger entry. Every
assessment is calibrated as course/COURSE.md says: honest work is the
easiest path to full credit, and attendance alone earns a passing but
mediocre score (DECISIONS.md, 2026-10-05). The questions in every
assessment are student-facing text (STUDENT_FACING.md): the unit by its
topic, no lesson numbers.

## Reading quiz

`assessments/QUIZ_N.N_Short_Name.md`, for the lesson a reading is due
(DECISIONS.md: 2026-09-27 for the quiz, 2026-10-05 for multiple choice
and the Code check, 2026-10-07 for Codio). Three to five
questions on the assigned reading, answerable in five minutes by a
student who did the reading and not by one who did not. Mix one recall
question with questions that require having run or traced the
chapter's code. Every question is multiple choice with four options,
A to D, and exactly one correct answer, and the correct answers are
spread across A to D. The key, below the questions, is a table:
question, answer, one-line explanation. Below the key, a "Code check"
section runs each question's code with its output or error in a `text`
block, so `check` confirms every answer that rests on code; in the
questions themselves, code that prints carries an `any-output`
directive and code that fails on purpose is marked `python no-run`.
`check` confirms the options, the key rows, the spread, and the Code
check section.

Students take the quiz in Codio, through a link in Canvas. After the
quiz is final, its Codio files are made from it with the codio-mcq
skill into `rendered/codio/QUIZ_N.N_Short_Name/`: a guide page that
embeds the questions and `MC_Assessments/` with one JSON (JavaScript
Object Notation) file per question. Each question's guidance is its key
explanation, the answers keep the quiz's order, the questions are not
shuffled, each JSON file parses and has exactly one correct answer, and
the guide page names every JSON file. Those files are output: remade
when the quiz changes, never edited by hand, and outside git with the
rest of rendered/. The lesson plan's Preparation list tells Dan to put
them in Codio, and the deck's reading quiz slide sends students to the
link in Canvas.

## Learning check

`assessments/CHECK_N.N_Short_Name.md`, named by the lesson it is marked
on, about every five or six class meetings (DECISIONS.md, 2026-10-05).
Four questions, projected, answered in the paper journal, which Dan
collects. Ten points: three questions (2, 2, and 3 points) that are
easy for a student who was awake and took part in class, and one (3
points) that is easy only for a student who worked through a recent
assignment themselves. It counts in Labs/Learning Checks.

The top half is what gets projected: the line "Answer in your journal.
Label each answer clearly (A1, A2, A3, B1)."; Part A with A1 (2
points), A2 (2 points), and A3 (3 points); Part B with B1 (3 points).
Below a divider, teacher notes: the lessons covered; for each Part A
question, the answer, the lesson where students saw it, the common
miss, and how the points split; for B1, the same plus the assignment
or mini-project it draws on, which was due before the check; a grading
budget; and a scoring line saying Part A alone is 7 of 10. The line
`<!-- pipeline: only teacher -->` sits directly above the divider and
`<!-- pipeline: end only -->` is the last line, so the student copy the
pipeline makes holds only the projected half; no other kind of
artifact gets these two lines unless Dan asks for a student copy of
it. `check` confirms the four questions, their points, the journal
line, the divider, and the two pipeline lines.

Content: nothing from the lesson it is marked on or from a later one,
so Dan can give it a day late but not a day early. Any code in it was
run. Questions and answers run to the
length of Dan's examples in sources/assessments/learning_checks/
(three checks from his Object Oriented Design course, in Java: copy
the shape, never the content): an answer is a value, an exact output,
a sentence or two, a few lines of code, or a quick sketch, and a
journal grades in about 90 seconds. Dan makes the slide that projects
the questions himself; the lesson's deck has none, and the file sets
no limit for it (DECISIONS.md, 2026-10-07). The lesson's plan opens its
Agenda with the check (LESSON.md).

## Unit quiz

`assessments/QUIZ_N_Unit_Quiz.md`, after the unit's project, so it can
ask about the project (DECISIONS.md, 2026-10-05). Dan schedules it;
plans and lesson counts leave its time out. Laid out like
sources/assessments/unit_2_quiz/Cumulative_Quiz_Units1-2_LLM.md: an
"About this file" block (total points, coverage, conditions including
the one sentence that says how the quiz is monitored, Canvas question
types), the multiple-choice questions, the short-answer questions, an
answer key table with topic and explanation, the spread of answers
across A to D, and a point-by-point rubric for each short answer.

About 30 minutes of student time, taken in Canvas with no notes and no
running code: ten to thirteen multiple-choice questions at 2 points and
two short-answer questions at 7 points, one asking students to write a
short function and the other to explain and fix a piece of code. If a
question needs more than about eight lines of code to trace, the quiz
has fewer questions. About a fifth of the points come from earlier
units. Questions about the project rest on what every option shares,
because classes may have done different options. Every answer is
confirmed by running the code.

## Quiz review guide

`materials/CODIO_N_Quiz_Review/`, built with each unit quiz and
assigned before it (DECISIONS.md, 2026-10-05), laid out like
sources/assessments/unit_2_quiz/Codio_Review/: numbered guide pages of
short notes followed by practice questions, one page per part of the
unit; an answers-and-explanations page; `MC_Assessments/` with one JSON
file per multiple-choice practice question, copying the model's fields
exactly with its own ten-digit task ID and its own answer IDs; and
`SA_manual_entry.md` with the short-answer practice questions, sample
answers, and rubrics. Each practice question parallels a quiz question
and is not the same question: different code, different values. Every
`{Check It!|assessment}` line on a guide page names a JSON file that
exists, and each JSON file parses with exactly one correct answer.
Guide pages are student-facing and name the unit by its topic.
The answers page writes out every practice question in full, and
`tools/review_json.py` makes the JSON files from it, so a change to a
question is made on the answers page and the tool is run again.

## Done when

- Reading quiz: `check` passes; the Codio files exist in
  rendered/codio/, made from the final quiz; Preparation tells Dan to
  put them in Codio.
- Learning check: `check` passes; the notes name the lesson for each
  Part A question and the assignment for B1, due before the check;
  nothing from the marked lesson or later.
- Unit quiz and review guide: every answer confirmed by running the
  code; the key spread across A to D; each JSON file parses with one
  correct answer; every Check It line names a file that exists; the
  quiz and the guide share no question.
