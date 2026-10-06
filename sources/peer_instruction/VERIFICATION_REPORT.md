# Verification Report - PI Question Bank

Two passes: a code check of every answer with runnable code (below), and a
concept check of everything else (second section).

## Code check

Date: 2026-07-25. Every recorded answer with runnable code was tested
against actual Python execution: a mechanical pass ran all self-contained
trace questions; agent-run experiments covered fill-in-the-blank, buggy-
by-design, and context-dependent questions; every conflict or judgment
call was independently re-run and adjudicated by a second model.

Each question's markdown entry now carries a "Code check" line (absent
only for questions with nothing to execute: conceptual clickers and
practice exercises).

### Totals

- Confirmed by execution: 106
- Confirmed, with a caveat worth reading: 4
- Not applicable (no code / exercise): 112

### Caveats (answer stands, but know this when using it)

- `11_strings` slide 14: Option B is the correct approach, but as shown it lacks a `return new_s` line and so literally returns None - a missing-return truncation shared by all three options, not a flaw unique to B.
- `13_morelists` slide 10: The slide code is missing a comma between the two inner lists, so run exactly as printed it raises a TypeError (option D); answer C is correct only for the intended code [[1,2,3],[5,10,20]] with the comma inserted, as the instructor's PDF annotation does.
- `15_recursion` slide 11: The code as printed on the slide (else: flush at the left margin) is literally a SyntaxError, i.e. option D; answer C holds only under the intended indentation where the else belongs to the if, making noob a Fibonacci function so noob(4) returns 5.
- `35_review` slide 2: Answer D is correct for the intended function (base case len(s)==1 returning s); the code as printed on the slide has a base-case bug (len 0 returning "") that doubles the middle letter and actually prints "cattac" (option C).

## Concept check

Date: 2026-07-25. The 112 questions with nothing to execute (conceptual
clickers and practice exercises) were verified separately. Method: the 92
of them that carry a recorded answer were re-solved blind by independent
agents (recorded answers withheld), 12 questions per agent, and each blind
result was then compared against the recorded answer; every mismatch was
adjudicated by hand against the original pptx text, speaker notes, the
handwritten PDFs, and (where applicable) actual execution or truth tables.
Each verified question's markdown entry now carries a "Concept check" line
and each JSON record a `concept_check` object.

### Totals

- Confirmed (blind solve agreed with the recorded answer): 88
  - 63 multiple-choice answers matched letter-for-letter
  - 25 open-response exercises where the blind solver independently
    re-derived a solution matching the recorded one in substance
- Confirmed with a caveat: 2
- Discrepancy (recorded answer conflicts with analysis): 2
- Nothing to verify: 20 practice exercises with no recorded answer, plus
  6 opinion/demo polls with no correct answer (the NSA-disclosure series
  in `37_lastclass` and the "best dinosaur" PI demo), which carry no
  check line at all.

### Caveats (answer stands, but know this when using it)

Both are the familiar slide-typo pattern: the recorded answer matches the
instructor's evident intent, not the options as literally printed.

- `21_boolean` slide 10 (A XOR B): Notes say D ("B & C"), but as printed
  only B is XOR - option C simplifies by De Morgan to NAND, differing at
  A=B=0. C was almost certainly meant to be "((NOT A) OR (NOT B)) AND
  (A OR B)", which would make D correct.
- `21_boolean` slide 12 (majority of A, B, C): Notes say D ("B and C"),
  but as printed only C is the majority function - option B repeats
  "(A and C)" where it plainly meant "(B and C)", and as printed reduces
  to "A and (B or C)".

### Discrepancies flagged for review (could not be reconciled)

In both cases the recorded answer comes from speaker notes alone, with no
handwritten confirmation in the annotated PDF, and no typo-style reading
of the options reconciles the notes with the analysis.

- `09_morefunctions` slide 19 (which isFib is correct): Notes say D
  ("All of them"), but executed against a working fib, option A returns
  False for the Fibonacci numbers 2 and 3 (its range(n) loop exits before
  reaching them) and option B returns False for 1 (the while guard f < n
  never admits it). Only C is correct for every input, under either fib
  indexing convention. Verify the answer before using this question.
- `17_fractals` slide 13 (how much will I rotate): Notes say D
  (120, 240, 120), but drawing the Koch bump takes turns of 60, then -120
  (i.e. 240 expressed positively), then 60 - option C - under either
  rotation direction. D's rotations leave a net 120-degree heading change,
  which cannot close the bump; the deck's own slide-2 code shows the
  library takes signed rotations. Verify the answer before using this
  question.
