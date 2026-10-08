# Course outline: Dan's decisions of 2026-10-05

Moved here on 2026-10-08, in the governance audit, from course/COURSE_OUTLINE.md,
as written: the summary of what Dan decided, his answers on the outline's lines,
and the choices made while applying them, which he approved with the outline.
The standing rules among them are in DECISIONS.md, with their 2026-10-05 dates,
and are stated in CLAUDE.md, course/COURSE.md, and course/formats/. Two notes
inside refer to "CLAUDE.md section 6" and "[DEFAULT]" as the charter was then.

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

## The Codio course's name

The reference file and the PDF export both name the course "Python
Programming from Codio." CLAUDE.md and DECISIONS.md call it "Learn to
Code with Python." Dan confirmed on 2026-10-05 that the first name is
right, and both files were corrected that day.

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
