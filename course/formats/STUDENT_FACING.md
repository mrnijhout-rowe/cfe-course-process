# Student-facing text, decks, and Canvas pages: formats

What students see: the words on decks, Canvas pages, quiz and check
questions, handouts, and briefs. Defaults unless marked **[RULE]**;
each cites its ledger entry. Form is tools/PREPARING_MATERIAL.md's
("Writing a deck file", "Writing a Canvas page file").

## Student-facing text

- "You" is the student. **[RULE]** The teacher is Mr. Nijhout-Rowe, in
  the third person (DECISIONS.md, 2026-10-05). Any monitoring claim
  names the real mechanism once.
- The words are the ones students have been taught, not the words a
  textbook would use. Decks and pages may reword text the plan
  addresses to the teacher so it speaks to students; nothing is added
  or changed in substance, code, values, or answers, and a change in
  substance is first a change to the plan (DECISIONS.md, 2026-10-07).
- **[RULE]** A unit is named by its topic ("the data structures
  project"), not its number, and student-facing text uses no lesson
  numbers, so Dan has little to change by hand for a class that knows
  the unit by another number (DECISIONS.md, 2026-10-05). The
  exception: deck and Canvas page titles and their `unit` fields keep
  the spring numbering ("Lesson 4.5," "Unit 4"), and Dan changes them
  by hand where he wants to (DECISIONS.md, 2026-10-07). `check` flags
  a lesson number anywhere else on a page, on a deck's slides, in a
  quiz's questions, or in a check's projected half.
- A Canvas page never says when anything is due: not a date, not
  "before next class," not "before lesson 4.4." Dan sets due dates in
  Canvas and Codio and says them in the room (DECISIONS.md,
  2026-10-07). `check` flags a due date on a page.
- A handout, an option brief, and a project page name no option, since
  Dan chooses which options a class is offered.

## Deck

`lessons/DECK_N.N_Short_Name.md`, one per coding lesson, beside its
plan, with the same short name (DECISIONS.md, 2026-10-07). It holds
what gets projected during the period and nothing else. Everything on
a slide comes from the lesson plan: the deck is written after the plan
and copies it, reworded for students where the plan speaks to the
teacher. What the teacher says goes in `notes`, not on a slide. A deck
has no slide for a learning check; Dan makes that slide himself
(DECISIONS.md, 2026-10-07). The title slide and the frontmatter use the
spring numbering. The slides, in order:

1. Title: the lesson number and title, with the unit as subtitle, from
   the frontmatter.
2. Objectives, as in the plan.
3. Reading quiz, only when a reading was due: tells students to open
   the link to the chapter's reading quiz in Canvas (the quiz runs in
   Codio, reached through Canvas, so the slide names Canvas).
4. Plickers: one slide telling students to get their cards out, worded
   differently in each deck so it does not become a fixed phrase. The
   questions are not projected; they run in Plickers. The questions,
   in the order the plan runs them, and their answers go in the notes.
5. Anything the plan's Concept section marks "project this," such as
   the unit's comparison table. A table that grows across lessons
   shows its full frame every time, empty columns included, so
   students copy the whole frame and see that more is coming
   (DECISIONS.md, 2026-10-07); the cells added today appear on click,
   and until the slide maker can reveal cells, that is two slides,
   before and after.
6. The try-it prompt, as the plan gives it, with the ceiling variants
   appearing on click below it.
7. The try-it key, with its output.
8. The partner challenge or mini-project brief, as students see it,
   when the plan marks it "project this."
9. The quick check, when the plan has one, in the shape the plan gives
   it: four choices get two slides (one saying the answer is a number
   from 1 to 4 and students hold up that many fingers on "show me,"
   then the question with its choices numbered 1 to 4 and the answer
   in the notes); anything else is the question on one slide and the
   answer on the next or on click. A quick check is never rewritten
   into four choices for the deck's sake.
10. Tonight: the reading and the Codio work.

A diagram a concept needs goes in the deck as well as in the plan. In
the `cfe` slide style a list item made only of inline code renders
tiny, so each such item carries a few plain words after the code,
changed in the plan first. `check` confirms the title matches the file
and that no slide heading is a learning check.

## Canvas page

`lessons/PAGE_N.N_Short_Name.md`, one per coding lesson, beside its
plan and deck (DECISIONS.md, 2026-10-07). Dan posts it in Canvas before
class, so anything the plan tells him to post for students is on it;
the plan's Preparation list tells him to post the page whenever the
plan posts something. Like the deck, it is written after the plan and
copies it. Frontmatter for the `cfe` style: `title` and `unit` in the
spring numbering, `type: class recap`, a one-line `summary`, and
`details` for the header row, naming the Codio assignment, the reading,
and what opens the next class, with no dates. The body, in order:

1. **What happened in class.** In students' words: the idea, the
   error hit on purpose if there was one, and what students built.
2. **Links.** Everything the plan's Preparation list says to post: the
   Python Tutor links students open themselves, files they download,
   anything else "too long to type." Each link has its full address
   and a few words saying what it is. Left out when the plan posts
   nothing.
3. **Tonight.** The reading and the Codio work, in the words of the
   deck's Tonight slide.

A unit also has a page, `units/NN-name/PAGE_N_Unit.md`, with
`type: unit`: what the unit covers, what to bring, what is graded and
in which category, how the unit's lessons run, and any table students
keep in the journal across the unit, as the empty frame with the
lesson each part is added in. A project has one too,
`assessments/PROJECT_N_Page.md`, with `type: project`: it summarizes
the handout and holds the links to the project's files; it does not
replace the handout.

## Done when

- Deck: beside its plan, in the slide order above; everything on a
  slide is in the plan; teacher talk in `notes`; no learning check
  slide; the Plickers slide's notes list the lesson's questions in the
  order run, with answers, and its wording differs from the other
  decks; a growing table shows its full frame; a quick check keeps its
  shape; `check` passes with only the expected notes about code blocks
  that carry a link (tools/plan_check.py's manual, "Expected notes").
- Page: beside its plan, student-facing, with the `cfe` frontmatter;
  every link the plan says to post, each with its full address; no due
  date in any form; `check` passes.
