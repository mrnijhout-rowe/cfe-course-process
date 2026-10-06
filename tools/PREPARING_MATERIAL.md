# Preparing material for the pipeline

Read this if you are writing markdown in a course repo that will later be
turned into slides, a Canvas page, or a printed document. It stands on its
own: you do not need the pipeline repo open, and you do not need to run
anything.

It covers form only. What a lesson should say, and whether you may write new
wording at all, is decided by the course repo's own instructions. Follow
those first.

## What happens to your file

Three scripts, called makers, each read one markdown file and produce one
kind of output:

| Maker | Reads | Produces |
|---|---|---|
| document maker | a lesson plan, handout, quiz, rubric, form | a Word file, and a PDF if asked |
| Canvas maker | a page for students | HTML that the teacher pastes into Canvas |
| slide maker | a deck file | a Slidev deck for projecting and a PowerPoint file |

The makers format and do nothing else. That has consequences for how you
write:

- **What you write is what appears.** No one downstream adds a title, a
  "Name: ____" line, a caption, a summary, or a closing slide. If it should
  be on the page, it is in your file.
- **Nothing is tidied.** A typo, a wrong number, or a placeholder such as
  "TBD" comes out exactly as typed.
- **Nothing is cut to fit.** A slide with too much on it runs off the
  bottom. A page breaks wherever the text happens to fall. Fitting is done
  by you, in the file, using the sizes given below.
- **Instructions written as prose do nothing.** "Make this table landscape"
  in a comment is ignored. There is a short fixed list of notes the makers
  act on, described below. Anything else has to be done by how you write
  the file.

That nobody downstream adds these things does not make them yours to add.
If your source has no "Name:" line and nobody asked for one, the worksheet
has none; say in your hand-off that you think one is missing, and let the
teacher decide.

The same goes for the examples in this guide. Their values (a unit number,
a due date, a title) are examples. Every value in your file comes from your
source or your instructions. Where the source does not give one, leave the
setting out.

What you can leave alone: fonts, colours, logos, page numbers, footers, the
design of the title slide. Those belong to the style, which the teacher
chooses when the file is made.

## One file, one output

Decide what each file is before you write it, because the three kinds are
written differently.

| You are writing | Make it a | Why it cannot double as something else |
|---|---|---|
| something to read or print | document file | |
| something students read in Canvas | Canvas page file | Canvas removes a lot; the page needs web addresses for images |
| something to project | deck file | every `##` heading becomes a slide |

A lesson plan is a document. It is not a deck: run through the slide maker,
its Overview, Preparation and Agenda sections would each become a slide.
Whatever should be projected goes in a separate deck file.

The output takes the file's name, so `LP_4.1_String_Sequence.md` becomes
`LP_4.1_String_Sequence.docx`. Use names without spaces.

## Rules for every file

**Ordinary markdown.** Headings, paragraphs, bold, italic, links, bulleted
and numbered lists, tables written with pipes, fenced code, block quotes,
images. Lines within a paragraph are joined, so wrap them however you like.

**Characters are kept as typed.** Quotes are not curled, `--` is not joined
into a dash, `$5` is not read as math. Type the characters you want to see.

**Do not use HTML tags.** They behave differently in each output, and in a
Word document they are removed, sometimes taking their text with them.
Write it in markdown.

**Comments are for you.** An HTML comment never appears in any output, so
it is the place for notes to yourself, to another tool, or to the next
author:

```markdown
<!-- The mini-project takes the partner-challenge slot today. -->
```

**Code.** Put it in a fence and name the language. Put what a program
prints, and error messages, in a fence marked `text`. A line of 80
characters or fewer fits in every kind of output; the exact limits are in
each section below, and they apply to `text` fences as well as code.

Shortening a code line, even by moving a comment onto its own line, changes
the source's code. Do it only if your instructions allow that. If they do
not, leave the line as it is and mention it in your hand-off.

````markdown
```python
print(len('Gadsby'))
```

```text
6
```
````

**Tables.** Pipe tables only. Keep cells short. A pipe character inside a
cell is written `\|`.

**Settings at the top (frontmatter).** Optional. A block between two `---`
lines at the very top of the file:

```yaml
---
title: "Lesson 4.1: A string is a sequence"
subtitle: "Unit 4: Data structures"
---
```

Put quotes around any value that contains a colon. Which settings matter is
given per kind of file below.

**Course-wide settings.** If the course repo has a `pipeline.yml` at its
top, it already supplies the author, the course name and the course's
styles to every file. Do not repeat those in each file.

### Leaving something out of one copy

To keep an answer key, teacher notes, or a slide out of the student copy,
mark the region. This works in all three kinds of file:

```markdown
**1.** What does `len('Gadsby')` return?

<!-- pipeline: only teacher -->
**Answer.** 6.
<!-- pipeline: end only -->
```

The teacher's copy has everything. The copy made for `student` leaves the
region out, along with any notes inside it. So a page break that belongs to
the key goes inside the region, and the student copy gets no blank page.
Every `only` needs its `end only`.

This is how one file gives both a quiz and its key, so the two cannot drift
apart. When you hand the file on, say that both copies are wanted.

### Notes the makers act on

A note is an HTML comment beginning `pipeline:`, on a line of its own. This
is the whole list. A note not on it does nothing.

| Note | In | What it does |
|---|---|---|
| `<!-- pipeline: only NAME -->` ... `<!-- pipeline: end only -->` | any file | keeps the region for that audience only |
| `<!-- pipeline: page-break -->` | document | starts a new page |
| `<!-- pipeline: space 2in -->` | document | blank room to write in (`in`, `cm`, or `lines`) |
| `<!-- pipeline: lines 4 -->` | document | that many ruled lines to write on |
| `<!-- pipeline: table ... -->` | document | shapes the table directly below it |
| `<!-- pipeline: notes ... -->` | deck | speaker notes for the slide it is in |
| `<!-- pipeline: reveal -->` | deck | the slide's list appears one item at a time |
| `<!-- pipeline: split -->` | deck | what is above goes left, what is below goes right |
| `<!-- pipeline: layout NAME -->` | deck | a named Slidev layout, such as `center` |

## Writing a document file

For lesson plans, handouts, worksheets, quizzes, rubrics and forms.

- Open with one `# Heading`. It is the document's title. Use `##` and `###`
  below it.
- A numbered list typed `1.` stays numbered at every depth.
- A task list (`- [ ] Bring the cards`) prints as boxes to tick: good for a
  preparation checklist.
- A block quote is indented with a rule down its side: good for text the
  teacher will project or read aloud.
- An image is found beside the markdown file: `![The table](board.png)`.

**Sizes** (US letter, portrait, in the default style):

| What | Fits |
|---|---|
| a line of code or program output | 83 characters; a longer line wraps onto the next |
| a line of code, landscape | about 110 characters |
| lines of ordinary text on a page | about 50 |
| a table | sized to its contents; past about five columns of real text it gets cramped |

For a wide table or wide code, turn the page with `orientation: landscape`
in the frontmatter.

**Worksheets.** Room to write is made with notes:

```markdown
# Counting letters

**1.** What does `num_vowels('Gadsby')` return?

<!-- pipeline: lines 2 -->

**2.** Sketch the steps before you type.

<!-- pipeline: space 2in -->

**3.** Plan your program.

<!-- pipeline: table widths=30,70 row-height=0.8in -->
| Step | What happens |
|---|---|
| | |
| | |

<!-- pipeline: page-break -->

## Reflection
```

The table note takes any of `width=full` (stretch across the page),
`widths=30,70` (the share each column gets, one number per column), and
`row-height=0.8in` (how tall each empty row is). A table with empty cells
and no note collapses to thin rows, so a table meant for writing in needs
`row-height`.

If the worksheet must fit on one page, count in inches. A letter page has
about 9.5 inches of usable height. A line of text or code is under 0.2
inch, a paragraph break adds half a line, a heading takes about two lines,
and a ruled line for writing is 0.4 inch. Leave some slack, and say in your
hand-off that the page count should be checked, since you are estimating.

## Writing a Canvas page file

The teacher pastes the result into Canvas, which is strict about what it
keeps.

- The title is `title:` in the frontmatter, or a `# Heading` on the first
  line. Canvas shows the title itself, so start the body's headings at `##`.
- **An image must have a web address.** A local file cannot be shown. If
  the image is not online yet, say so when you hand the file on; someone
  has to upload it to Canvas first.
- Links need full addresses (`https://...`).
- Do not use footnotes; their links do not work once pasted.
- A callout is a block quote starting `[!NOTE]`, `[!TIP]`, `[!WARNING]` or
  `[!CAUTION]`. Use one or two on a page at most.
- A code line of up to 80 characters fits. A longer one makes the reader
  scroll sideways.

If the course uses the `cfe` Canvas style, the page has a header card, and
the frontmatter fills it:

```yaml
---
title: "Lesson 4.1: A string is a sequence"
type: class recap
unit: Unit 4
summary: What we did in class and what is due.
details:
  Codio: U6.L4 String Iteration, due before lesson 4.2
  Next class: reading quiz on chapter 7
---

## What happened in class

You wrote a `for` loop that visits every character of a string.
```

- `type` is one of: assignment, quiz, discussion, page, reading, lab,
  project, announcement, module, journal, learning check, class recap,
  unit. Any other word stops the maker.
- `details` is the row of facts in the header, in the order you list them.
  Include only facts you were given. Leave out a due date or point value
  you do not know; do not guess one.
- Only `title` is required.

## Writing a deck file

A deck file is written as slides.

```markdown
---
title: "A string is a *sequence.*"
subtitle: "Lesson 4.1"
---

# Counting with a loop

## Start from the loop they know
<!-- pipeline: notes
Say: you have written this loop all semester.
-->

## Count the letters
<!-- pipeline: reveal -->

1. Start the counter at 0.
2. Visit every character.
3. Add one when the test passes.
```

**How the file is cut into slides**

- `title:` in the frontmatter makes the title slide. `subtitle`, `author`,
  `course` and `date` appear on it if given. Do not repeat the title as a
  `#` heading; that would add a section slide with the same words.
- `# Heading` makes a section slide: a divider between parts of the
  lesson. One short line of text under it is shown as a lead-in. Anything
  longer belongs on a slide of its own after it.
- `## Heading` starts an ordinary slide. Most slides are these.
- A line holding only `---` starts a slide with no heading.
- `###` is a small heading inside a slide.

Because `---` means "new slide", write a horizontal rule as `***`.

**Notes for a slide** may sit anywhere inside that slide, including a
section slide or a slide with no heading. Directly under the heading is the
convention. Their order does not matter, with one exception: `split` marks
the dividing point, so its position is the divide.

- What the teacher says goes in `notes`, not on the slide. It shows in
  presenter view and in PowerPoint's notes pane.
- `reveal` shows the slide's list one item at a time.
- `split` divides the slide: what is above the note goes left, what is
  below goes right. The heading spans both. Once per slide.

**How much fits on a slide.** Nothing is shrunk to fit except over-wide
code, so count before you write. These were measured.

| | default style (`ncssm`) | class style (`cfe`) |
|---|---|---|
| list items or lines of text under a title | 10 | 12 |
| characters across a line of text | about 75 | about 95 |
| lines of code | 15 | 16 |
| characters across a line of code | 80 | 86 |
| characters across code in a split slide | 38 | 41 |
| characters in a slide title, to stay on one line | about 45 | about 45 |

If you do not know which style will be used, write to the default column.
It is the tighter one, and the PowerPoint file fits the same numbers.

For a slide that mixes things, count in rows. A slide in the default style
holds 10 rows under its title.

| On the slide | Rows |
|---|---|
| a list item, or a line of text | 1, and 1 more for each extra line it wraps onto |
| a code block or `text` block | 1 for the block, plus 0.6 for each line in it |
| a block quote | 1 for the quote, plus 1 for each line in it |
| a small table | 1 for each row, counting the header |
| blank lines between things | 0 |

Worked through: fifteen lines of code alone is 1 + 9 = 10. Four lines of
text and an eight-line code block is 4 + 1 + 4.8 = 9.8. A six-line code
block with its one line of output below is 1 + 3.6 + 1 + 0.6 = 6.2. In a
split slide, count each side on its own; each holds 10.

A code line wider than the limit is set smaller so that it still shows, and
at about three quarters of normal size it stops being readable from the
back of a room.

When a slide is over the count, make two slides. Cut where the source
already breaks: between paragraphs, between list items, at the source's own
sub-headings. Start the second slide with `---`, which gives a slide with no
heading, unless the source supplies a heading for it. Do not invent a title
for the continuation, and do not trim the wording to fit unless your
instructions allow you to change wording.

**Other things that matter in a deck**

- One idea per slide. A table on a slide should be small: about four
  columns and six rows.
- Emphasis in the deck's title (`*sequence.*`) becomes one bold orange word
  on the default title slide. Use it once or not at all.
- An image is found beside the deck file and copied along with it.
- Text such as `{{ total }}` or `in <module>` is safe in a deck; it is
  shown as typed.

## Before you hand a file on

- Is every word that should appear in the file, and nothing that should not
  (outside comments and `only` regions)?
- Is it one kind of file, with the right kind of structure?
- Does every `only` have its `end only`?
- Is every note on a line of its own, spelled as in the table above?
- Do code lines fit the width for this kind of file?
- Did every value in the frontmatter come from your source, and none from
  an example?
- For a deck: does each slide fit the count?
- For a Canvas page: does every image have a web address?
- For a worksheet: does every table for writing in have a `row-height`?

## What to say when you hand it on

Whoever runs the makers needs these, one line per file:

1. Which file, and which kind it is: document, Canvas page, or deck.
2. Whether a student copy is wanted as well as the full one.
3. Whether a PDF is wanted.
4. A style, only if the teacher asked for a particular look. Otherwise say
   nothing: the course's `pipeline.yml` or the pipeline's own default
   decides.
5. Anything that still needs a person: an image to upload to Canvas, a
   fact you left out because the source did not give it, a long code line
   you were not allowed to shorten, a page count that should be checked,
   something you think is missing from the source.

For example: "`assessments/QUIZ_4.2.md` is a document; make the full copy
and a student copy, both as PDF. `pages/recap_4_1.md` is a Canvas page; its
image `board.png` has to be uploaded to Canvas first."

## If you can run the makers yourself

Then do, and read what they print: they report a note they do not know, HTML
in a document, an over-wide code line, and a code block too long for a
slide. The pipeline repo's `docs/making-materials.md` covers running them
and checking the result. The complete reference for everything on this page
is `docs/markdown-format.md` there.
