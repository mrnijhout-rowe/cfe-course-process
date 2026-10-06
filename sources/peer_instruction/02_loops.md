# Peer Instruction Questions: Loops (for, nested, while)

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## For loops

### Q1. At the end of this code, what will appear on the terminal?

**Source:** `03_loops.pptx` slide 12 - worked answer in `03_loops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(1,5):
	print(i,i*i,end='')
```

- **A.** 2 4 3 9 4 16
- **B.** 2 4 3 9 4 16 5 25
- **C.** 1 1 2 4 3 9 4 16
- **D.** 1 1 2 4 3 9 4 16 5 25
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C - run code; PDF has C circled; range(1,5) runs i=1 through 4, printing i and i*i each iteration.

**Code check:** confirmed by execution

*Also touches: range, loop-tracing, print-output*

### Q2. How many times will we print "Done!"?

**Source:** `03_loops.pptx` slide 14 - worked answer in `03_loops.pdf`

How many times will we print "Done!"?

```python
for i in range(1,5):
	print(i)
	print(i*i)
print("Done!")
```

- **A.** 0
- **B.** 1
- **C.** 4
- **D.** 5
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B - run code; PDF has B circled; print("Done!") is outside the loop body so it executes once.

**Code check:** confirmed by execution

*Also touches: indentation, loop-body-scope*

### Q3. At the end of this code, what will appear on the terminal?

**Source:** `03_loops.pptx` slide 16 - worked answer in `03_loops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(6):
	print(i,i*i,end='')
```

- **A.** 1 1 2 4 3 9 4 16 5 25
- **B.** 0 0 1 1 2 4 3 9 4 16
- **C.** 0 0 1 1 2 4 3 9 4 16 5 25
- **D.** 0 0 1 1 2 4 3 9 4 16 5 25 6 36
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C - run code; PDF has C circled; range(6) is equivalent to range(0,6) so i runs 0 through 5.

**Code check:** confirmed by execution

*Also touches: range, single-argument-range, loop-tracing*

### Q4. At the end of this code, what will appear on the terminal?

**Source:** `03_loops.pptx` slide 18 - worked answer in `03_loops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(1,6,2):
	print(i,end='')
```

- **A.** 1 3 5
- **B.** 2 4 6
- **C.** 1 3 5 7
- **D.** 1 2 3 4 5
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A - run code; PDF has A circled with a handwritten trace i=1,3,5 then i=7 done, so the step-2 loop stops before reaching 6.

**Code check:** confirmed by execution

*Also touches: range, step-argument, loop-tracing*

### Q5. At the end of this code, what will appear on the terminal?

**Source:** `03_loops.pptx` slide 19 - worked answer in `03_loops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(12,6,-2):
	print(i,end='')
```

- **A.** 10 8
- **B.** 10 8 6
- **C.** 12 10 8
- **D.** 12 10 8 6
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C - run code; PDF has C circled; range(12,6,-2) counts down 12,10,8 and stops before 6.

**Code check:** confirmed by execution

*Also touches: range, negative-step, loop-tracing*

### Q6. To print numbers 1 through n

**Source:** `04_moreloops.pptx` slide 3 - worked answer in `04_moreloops.pdf`

To print numbers 1 through n

- **A.** for i in range(1,i):
- **B.** for i in range(1,n):
- **C.** for i in range(1,n+1):
- **D.** for i in range(i,n):
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say C; range(1,n+1) yields 1 through n. The annotated PDF shows a variant slide with prompt 'i through n' where the instructor crossed out E and wrote 'None of the above', so the PDF cannot verify this pptx version.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: range*

### Q7. Add up the numbers 1 through 4

**Source:** `04_moreloops.pptx` slide 4 - worked answer in `04_moreloops.pdf`

Add up the numbers 1 through 4

- **A.** for i in range(1,5):
	sum = 0
	sum = sum + i
- **B.** sum = 0
for i in range(1,5):
	sum = sum + 1
- **C.** sum = 0
for i in range(1,5):
	sum = sum + sum
- **D.** sum = 0
for i in range(1,5):
	sum = sum + i
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say D and the annotated PDF circles D; sum is initialized once before the loop and accumulates i each pass.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** 2x2 grid layout; label-code pairing (A top-left, B top-right, C bottom-left, D bottom-right) verified against shape positions and the annotated PDF.

*Also touches: accumulator, variables-and-assignment*

### Q8. will print

**Source:** `04_moreloops.pptx` slide 6 - worked answer in `04_moreloops.pdf`

will print

```python
n = 4
for i in range(1,n):
	print(i,n,end='')
	n = 6
```

- **A.** 1 4 2 4 3 4
- **B.** 1 4 2 6 3 6
- **C.** 1 4 2 6 3 6 4 6 5 6
- **D.** This will cause an error
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B and the annotated PDF circles B; range(1,n) is evaluated once with n=4, so i runs 1-3 and n prints as 4 then 6 6.

**Code check:** confirmed by execution

**Extraction note:** Untitled slide: the prompt is the code box followed by 'will print'. Option letters are not in the text dump; A-E ordering confirmed against the annotated PDF.

*Also touches: range, loop-variable-semantics*

### Q9. Generate this pattern for any n

**Source:** `04_moreloops.pptx` slide 8 - worked answer in `04_moreloops.pdf`

Generate this pattern for any n

*****
*****
*****
*****
*****

n=5

- **A.** for i in range(0,n):
	print("*"*i)
- **B.** for i in range(0,n):
	print("*"*n)
- **C.** for i in range(1,n):
	print("*"*i)
- **D.** for i in range(1,n):
	print("*"*n)
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B and the annotated PDF circles B; each of the n passes prints a full row of n stars.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** 2x2 grid layout; label-code pairing verified against the annotated PDF.

*Also touches: strings, string-repetition*

### Q10. For each row r, we should print

**Source:** `04_moreloops.pptx` slide 10 - worked answer in `04_moreloops.pdf`

For each row r, we should print

*
***
*****
*******
*********

n=5

- **A.** Front Spaces: (n-r)/2, *'s: r
- **B.** Front Spaces: n-r, *'s: 2r
- **C.** Front Spaces: n-r, *'s: 2r-1
- **D.** Front Spaces: r, *'s: n-r
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C and the annotated PDF circles C in the option table; row r has n-r leading spaces and 2r-1 stars.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options A-D are rows of an on-slide table with columns 'Front Spaces' and *'s (table text missing from the dump, recovered via python-pptx); option text reformatted as 'Front Spaces: ..., *'s: ...'.

*Also touches: pattern-printing, algebraic-reasoning*

### Q11. At the end of this code, what will appear?

**Source:** `05_nestedloops.pptx` slide 8 - worked answer in `05_nestedloops.pdf`

At the end of this code, what will appear?

```python
for i in range(10):
	pic.drawCircleFill(200+50*i,200+20*i,50)
```

- **A.** [image] a horizontal row of overlapping red circles, all the same size
- **B.** [image] a vertical column of overlapping red circles
- **C.** [image] a diagonal line of overlapping same-size red circles running down and to the right
- **D.** [image] red circles stacked almost on top of each other in one tight cluster
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say 'C - run code' and C is circled in the annotated PDF; both x and y grow with i so the circles march diagonally.

**Code check:** confirmed by execution

**Extraction note:** Options are images with no slide text; option texts are my descriptions of the pictures. Annotated PDF shows range(5) where the pptx has range(10) - earlier deck version, answer unaffected.

*Also touches: graphics, loop-variable-in-expressions*

### Q12. At the end of this code, what will appear?

**Source:** `05_nestedloops.pptx` slide 9 - worked answer in `05_nestedloops.pdf`

At the end of this code, what will appear?

```python
for i in range(10):
	pic.drawCircleFill(200+50*i,200+20*i,50-5*i)
```

- **A.** [image] a horizontal row of red circles shrinking from left to right
- **B.** [image] a vertical stack of red circles shrinking downward into a cone shape
- **C.** [image] a diagonal line of overlapping same-size red circles running down and to the right
- **D.** [image] a diagonal line of red circles that shrink as they run down and to the right
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say 'D' and D is circled in the annotated PDF; x and y grow with i while the radius 50-5*i shrinks.

**Code check:** confirmed by execution

**Extraction note:** Options are images with no slide text; option texts are my descriptions of the pictures. Annotated PDF shows range(5) where the pptx has range(10) - earlier deck version, answer unaffected.

*Also touches: graphics, loop-variable-in-expressions*

### Q13. At the end of this code, what will appear?

**Source:** `05_nestedloops.pptx` slide 10 - worked answer in `05_nestedloops.pdf`

At the end of this code, what will appear?

```python
for i in range(10):
	pic.setFillColor(0,0,50*i)
	pic.drawCircleFill(200+50*i,200,50)
```

- **A.** [image] a horizontal row of same-size circles fading from black to bright green
- **B.** [image] a horizontal row of same-size circles fading from black to bright blue
- **C.** [image] a diagonal line of circles, running down and to the right, fading from black to blue
- **D.** [image] a horizontal row of circles fading from black to green while shrinking from left to right
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'B'; consistent with the code - the blue channel 50*i increases while y and the radius stay fixed, so a horizontal row fading black to blue. This slide is missing from the annotated PDF, so no handwriting check was possible.

**Code check:** confirmed by execution

**Extraction note:** Options are images with no slide text; option texts are my descriptions of images extracted from the pptx, paired to labels by shape position. Slide absent from the annotated PDF (it has only 10 pages).

*Also touches: graphics, rgb-color-channels*

### Q14. How do we print row r of this pattern? Skip rows with 2 stars, assume rows start from 0...

**Source:** `06_conditionals.pptx` slide 14 - worked answer in `06_conditionals.pdf`

How do we print row r of this pattern? Skip rows with 2 stars, assume rows start from 0. (n=3)

- **A.** Spaces before *: r, Spaces after *: r
- **B.** Spaces before *: r, Spaces after *: n-r
- **C.** Spaces before *: n-r, Spaces after *: r
- **D.** Spaces before *: r, Spaces after *: n-r-1

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D; PDF circles table row D and its entries, with a worked before/after table in the margin - middle row r has r spaces before the diagonal star and n-r-1 after it.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options come from a table (columns: Clicker, Spaces before *, Spaces after *) that the plain text dump missed; the table has exactly options A-D, with no E / 'I don't know' row. The letter-N pattern is an image labeled n=3. The annotated PDF's version of this slide omits the phrase 'assume rows start from 0' present in the pptx.

*Also touches: index-arithmetic, pattern-printing, expressions*

### Q15. Assume we have a for loop

**Source:** `14_Review.pptx` slide 9 - worked answer in `14_Review.pdf`

Assume we have a for loop
for i in range(n):
How many spaces will we print before the star on each line, ignoring the top and bottom line?

- **A.** i
- **B.** n
- **C.** n - i
- **D.** n - i - 1
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and D is circled in the annotated PDF, with handwritten scaffolding showing print("."*(n-1)) for the top line and a for (0, n-i) style inner loop for the spaces.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Prompt refers to a star-pattern figure shown as an image on the slide (diamond-like patterns of dots and stars for n=2, n=3, n=4); the figure has no extractable text. En dashes in options normalized to hyphens.

*Also touches: nested-loops, star-patterns, index-arithmetic*

#### Practice exercises (For loops)

### Q16. Write code to generate this pattern for any n

**Source:** `04_moreloops.pptx` slide 7 - worked answer in `04_moreloops.pdf` (practice exercise, no answer options)

Write code to generate this pattern for any n

*
**
***
****
*****

n = 5

Hint:  Recall that print("x"*3) generates "xxx"

**Answer:** not recorded in the source materials

**Detail:** Speaker notes say only 'Go over answer'; no written solution appears in the deck or the annotated PDF.

*Also touches: strings, string-repetition*

### Q17. Write code for the Fibonaccis using a for loop (NOT recursion). Spec given: f(x) = f(x-...

**Source:** `16_morerecursion.pptx` slide 5 - worked answer in `16_morerecursion.pdf` (practice exercise, no answer options)

Write code for the Fibonaccis using a for loop (NOT recursion). Spec given: f(x) = f(x-1) + f(x-2); if (x < 2) then f(x) = 1.

```python
def fibs(n):


	for i in range(          ):



	return
```

**Answer:** def fibs(n):
	if n < 2:
		return 1
	prev = 1
	cur = 1
	for i in range(n - 1):
		prev, cur = cur, prev + cur
	return cur (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes and the PDF page is unannotated; model solution written by the extractor to fit the given skeleton (track the previous two values, iterate n-1 times).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Slide provides a fill-in skeleton (blank range argument and return), not a blank-page problem.

*Also touches: fibonacci, accumulator-pattern, functions*

## Nested loops

### Q18. At the end of this code, what will appear on the terminal?

**Source:** `04_moreloops.pptx` slide 11 - worked answer in `04_moreloops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(1,4):
	for j in range(1,4):
			print(i,j,end='')
```

- **A.** 1 1 2 2 3 3
- **B.** 1 2 3 1 2 3 1 2 3
- **C.** 1 1 1 2 1 3 2 1 2 2 2 3 3 1 3 2 3 3
- **D.** 1 1 2 1 3 1 2 1 2 2 2 3 3 1 3 2 3 3
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'C - run code'; slides 11-13 are missing from the annotated PDF. Independent trace confirms all (i,j) pairs in outer-then-inner order.

**Code check:** confirmed by execution

**Extraction note:** Untitled slide; a small 'Code' caption labels the code box.

*Also touches: for-loops*

### Q19. Generate the times table for any n

**Source:** `04_moreloops.pptx` slide 13 - worked answer in `04_moreloops.pdf`

Generate the times table for any n

1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16

n=4

- **A.** for i in range(0,n):
	for j in range(0,n):
		 print(i*j,end=' ')
print()
- **B.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
- **C.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
	print()
- **D.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
print()
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say c; no PDF page exists for this slide. C is the only version that starts from 1 and prints a newline inside the outer loop after each row.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** 2x2 grid layout; label-code pairing (A top-left, B top-right, C bottom-left, D bottom-right) verified via shape positions with python-pptx.

*Also touches: for-loops, print-formatting*

### Q20. At the end of this code, what will appear on the terminal?

**Source:** `05_nestedloops.pptx` slide 2 - worked answer in `05_nestedloops.pdf`

At the end of this code, what will appear on the terminal?

```python
for i in range(1,4):
	for j in range(1,4):
			print(i,j,end=' ')
```

- **A.** 1 1 2 2 3 3
- **B.** 1 2 3 1 2 3 1 2 3
- **C.** 1 1 1 2 1 3 2 1 2 2 2 3 3 1 3 2 3 3
- **D.** 1 1 2 1 3 1 2 1 2 2 2 3 3 1 3 2 3 3
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say 'C - run code' and C is circled in the annotated PDF; slide 3 traces the iteration table (i,j pairs 1,1 through 3,3) confirming it.

**Code check:** confirmed by execution

*Also touches: for-loops, print-output, code-tracing*

### Q21. Generate the times table for any n

**Source:** `05_nestedloops.pptx` slide 4 - worked answer in `05_nestedloops.pdf`

Generate the times table for any n

n=4
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16

- **A.** for i in range(0,n):
	for j in range(0,n):
		 print(i*j,end=' ')
print()
- **B.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
- **C.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
	print()
- **D.** for i in range(1,n+1):
	for j in range(1,n+1):
		 print(i*j,end=' ')
print()
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'c'; the annotated PDF circles C, marks C's print() as the per-row newline, and labels D's print() as 'outside loop'.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option label-code pairing verified against pptx shape positions (A top-left, B top-right, C bottom-left, D bottom-right).

*Also touches: for-loops, range-bounds, print-formatting*

### Q22. At the end of this code, what will appear?

**Source:** `05_nestedloops.pptx` slide 11 - worked answer in `05_nestedloops.pdf`

At the end of this code, what will appear?

```python
for i in range(0,5):
	for j in range(0,5):
  			pic.drawCircleFill(200+50*i,100+50*j,20)
```

- **A.** [image] a 5x5 grid of small red circles
- **B.** [image] a diagonal line of 5 red circles running down and to the right
- **C.** [image] a horizontal row of 5 red circles
- **D.** [image] clusters of overlapping red circles growing larger toward the right
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'A'; consistent with the code - every (i,j) combination is drawn, giving a 5x5 grid. This slide is missing from the annotated PDF, so no handwriting check was possible.

**Code check:** confirmed by execution

**Extraction note:** Options are images with no slide text; option texts are my descriptions of images extracted from the pptx, paired to labels by shape position. Slide absent from the annotated PDF (it has only 10 pages).

*Also touches: for-loops, graphics, cartesian-product*

### Q23. Will this print the right thing?

**Source:** `06_conditionals.pptx` slide 15 - worked answer in `06_conditionals.pdf`

Will this print the right thing?

```python
for row in range(n+2):
    for col in range(n+2):
        if (row == col or col == 0 or col == n+1):
            print("*", end='')
        else:
            print(" ",end='')
    print()
```

- **A.** Yes
- **B.** No
- **C.** Sometimes
- **D.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A; PDF circles A (Yes) with a hand-traced star grid in the margin - the code correctly prints the letter-N pattern.

**Code check:** confirmed by execution

**Extraction note:** 'The right thing' refers to the letter-N star pattern introduced on slide 13. Option letters recovered from the annotated PDF (the pptx text box lists only the option bodies). Indentation reconstructed to the logical structure shown in the PDF; the raw pptx text box has garbled whitespace.

*Also touches: conditionals, booleans-and-logic, pattern-printing*

#### Practice exercises (Nested loops)

### Q24. How do we print this pattern? (n=3)

**Source:** `06_conditionals.pptx` slide 13 - worked answer in `06_conditionals.pdf` (practice exercise, no answer options)

How do we print this pattern? (n=3)

**Answer:** Break the problem into sections: print the top row, then the middle rows one at a time (star, some spaces, the diagonal star, more spaces, star), then the last row; the finished nested-loop solution appears on slide 15. (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes give the intended decomposition (top row, middle chunk, last row - the point is breaking the problem into sections); the annotated PDF page shows handwritten pseudocode using front/back space counts per row.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** The pattern exists only as an image: the letter N drawn in asterisks (stars in the first and last column of every row plus the main diagonal), labeled n=3.

*Also touches: for-loops, conditionals, problem-decomposition, pattern-printing*

### Q25. Write a function tree(n), which takes in a number and draws a lovely tree like the ones...

**Source:** `36_review.pptx` slide 12 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Write a function tree(n), which takes in a number and draws a lovely tree like the ones pictured below.

**Answer:** for i in range(n + 1): print(" " * (n - i) + "*" * (2 * i + 1)) for the triangular top (rows of width 1, 3, ..., 2n+1), then for i in range(n): print(" " * n + "*") for a trunk of n centered single stars. (inferred during extraction - not marked in the source materials)

**Detail:** Slide omitted from the annotated PDF and no notes; solution derived by the extractor from the example pictures, which show ASCII trees of asterisks for tree(3) and tree(5).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** The example trees are an image on the slide, extracted from the pptx: tree(3) shows star rows of widths 1, 3, 5, 7 above a trunk of 3 single stars; tree(5) shows widths 1 through 11 above a trunk of 5 stars.

*Also touches: for-loops, strings, ascii-art, string-repetition*

## While loops

### Q26. will print

**Source:** `07_whileloops.pptx` slide 7 - worked answer in `07_whileloops.pdf`

will print

```python
x = 6

while(x > 4):
	print(x, end=' ')
	x = x - 1
```

- **A.** 6 5
- **B.** 6 5 4
- **C.** 6 5 4 3
- **D.** 5 4 3
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A; PDF circles A and works the iterations (1st prints 6, 2nd prints 5, then x is 4 and the loop exits).

**Code check:** confirmed by execution

*Also touches: code-tracing, loop-conditions*

### Q27. will print

**Source:** `07_whileloops.pptx` slide 8 - worked answer in `07_whileloops.pdf`

will print

```python
i=0

while(i<3):
	print(i, end=' ')
```

- **A.** 0 0 0
- **B.** 0 1 2
- **C.** 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . .
- **D.** 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 . . . .
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF circles C and annotates 'i never changes' and 'infinite loop'.

**Code check:** confirmed by execution

*Also touches: infinite-loops, loop-update*

### Q28. How can we translate this code to a while loop?

**Source:** `07_whileloops.pptx` slide 9 - worked answer in `07_whileloops.pdf`

How can we translate this code to a while loop?

```python
for i in range(n):
	<body>
```

- **A.** i=0
while(i<n):
	<body>
- **B.** i=0
while(i<n):
	<body>
	i = i + 1
- **C.** i = 1
while(i<n):
	<body>
	i = i +1
- **D.** i = 0
while(i<n):
	<body>
	n = n + 1
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF circles the i=0 with i = i + 1 snippet and marks the no-increment option 'infinite loop'.

**Code check:** confirmed by execution

**Extraction note:** Label-option pairing recovered from pptx shape positions (labels A-D sit beneath the four code boxes left to right). The annotated PDF is a slightly different edition whose options C and D differ, but its circled answer B is identical to the pptx option B.

*Also touches: for-loops, loop-equivalence, range*

### Q29. Which number will get us out of the loop?

**Source:** `07_whileloops.pptx` slide 11 - worked answer in `07_whileloops.pdf`

Which number will get us out of the loop?

```python
valid = False
while not valid:
	x = eval(input ("Enter a number: "))
	valid = (x%2 == 1 and x%3 == 0)
```

- **A.** 2
- **B.** 6
- **C.** 9
- **D.** None of the above
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF circles C with 'odd' and 'multiples of 3' worked in ink - 9 is odd and divisible by 3, so valid becomes True.

**Code check:** confirmed by execution

*Also touches: booleans-and-logic, modulo, input-validation*

### Q30. Which of these will exit on 9?

**Source:** `07_whileloops.pptx` slide 13 - worked answer in `07_whileloops.pdf`

Which of these will exit on 9?

- **A.** x = eval(input ("Enter a number: "))
while (x%2 == 1 and x%3 == 0):
	x = eval(input ("Enter a number: "))
- **B.** x = eval(input ("Enter a number: "))
while True:
	if (x%2 == 1 and x%3 == 0):
			break;
	x = eval(input ("Enter a number: "))
- **C.** Both
- **D.** Neither
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'B - a will only keep going if its 9' (A loops while the condition holds, so 9 keeps it running); PDF circles B and marks the break as 'exit'.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: break, booleans-and-logic, loop-conditions*

### Q31. What does this print?

**Source:** `14_Review.pptx` slide 6 - worked answer in `14_Review.pdf`

What does this print?

```python
s = 'pirate ship'
i=0
while(len(s) > i ):
	s=s[i:]
	i=i+1
	print (s , i )
```

- **A.** pirate ship 1
irate ship 2
rate ship 3
ate ship 4
te ship 5
e ship 6
- **B.** pirate ship 1
irate ship 2
ate ship 3
 ship 4
p 5
- **C.** pirate ship 1
irate ship 2
rate ship 3
ate ship 4
te ship 5
e ship 6
 ship 7
ship 8
hip 9
ip 10
p 11
- **D.** None of the above
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the annotated PDF shows a handwritten line-by-line trace producing exactly option B's output (pirate 1, irate 2, ate 3, ship 4, p 5).

**Code check:** confirmed by execution

**Extraction note:** Option-letter pairing verified via pptx shape positions and the annotated PDF (labels interleaved with option bodies in the text dump).

*Also touches: strings, slicing, code-tracing*
