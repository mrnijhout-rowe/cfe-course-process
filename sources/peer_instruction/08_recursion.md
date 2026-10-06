# Peer Instruction Questions: Recursion

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. This code will return

**Source:** `15_recursion.pptx` slide 4 - worked answer in `15_recursion.pdf`

This code will return

```python
def fact(n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)

fact(3)
```

- **A.** 1
- **B.** 3
- **C.** 6
- **D.** This code will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C and the PDF has C (6) circled; fact(3) = 3*2*1 = 6.

**Code check:** confirmed by execution

*Also touches: functions, factorial, base-case*

### Q2. This code will print

**Source:** `15_recursion.pptx` slide 6 - worked answer in `15_recursion.pdf`

This code will print

```python
def num(x):
    print(x)
    num(x-1)
    print(x)

num(4)
```

- **A.** 4, 3, 2, 1
- **B.** 4, 3, 2, 1, 2, 3, 4
- **C.** 4, 3, 2, 1, 1, 2, 3, 4
- **D.** This code will cause an error / there is something wrong with this code
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say 'D - run num.py' and the PDF has D circled; there is no base case, so the recursion never stops and errors out.

**Code check:** confirmed by execution

*Also touches: base-case, infinite-recursion, functions*

### Q3. This code will print

**Source:** `15_recursion.pptx` slide 9 - worked answer in `15_recursion.pdf`

This code will print

```python
def num(x):
    if x > 0:
        print(x)
        num(x-1)
        num(x-2)
        print(x)

num(4)
```

- **A.** 4 3 2 1 3 2 1 1 2 3 4
- **B.** 4 3 2 1 3 2 1 1 2 3 1 2 3 4
- **C.** 4 3 2 1 1 2 1 1 3 2 1 1 2 4
- **D.** This code will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C and the PDF has C circled; the annotated memory trace on the following page writes out 4,3,2,1,1,2,1,1,3,2,1,1,2,4.

**Code check:** confirmed by execution

*Also touches: multiple-recursive-calls, tracing, functions*

### Q4. This code will return

**Source:** `15_recursion.pptx` slide 11 - worked answer in `15_recursion.pdf`

This code will return

```python
def noob(x):
    if x < 2:
        return 1
else:
        a = noob(x-1)
        b = noob(x-2)
        return a+b

y = noob(4)
```

- **A.** 1
- **B.** 2
- **C.** 5
- **D.** This code will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C, and the handwritten memory trace on the next PDF page works noob(4) out to a boxed 5 (option C); treating the code as correctly indented, noob is Fibonacci-style and noob(4) = 5.

**Code check:** confirmed by execution - caveat: The code as printed on the slide (else: flush at the left margin) is literally a SyntaxError, i.e. option D; answer C holds only under the intended indentation where the else belongs to the if, making noob a Fibonacci function so noob(4) returns 5.

**Extraction note:** The slide (confirmed in the PDF image) prints 'else:' flush at column 0, transcribed verbatim; taken literally that mis-indentation would be a syntax error, but the intended answer C treats the else as part of the if. No option is circled on the question's own PDF page (only a handwritten edit replacing 'y =' with print(noob(?))); PDF confirmation comes from the worked trace on the following page.

*Also touches: fibonacci, multiple-recursive-calls, functions*

### Q5. Which code is correct?

**Source:** `16_morerecursion.pptx` slide 3 - worked answer in `16_morerecursion.pdf`

Which code is correct?

- **A.** def fac(x):
	return x*fac(x-1)
- **B.** def fac(x):
	if x == 0:
		return 1
	return x*fac(x-1)
- **C.** def fac(x):
	if x == 0:
		return 1
	else:
		return x*fac(x-1)
- **D.** Both B and C
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Notes say 'D - why not A? Draw memory for B/C'; the PDF page writes 'no base case' next to A and 'exit function' at B's return 1, consistent with D, but no answer letter is circled or written.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option labels matched to code blocks via shape positions in the pptx: A top-left (no base case), B top-right, C bottom-left.

*Also touches: base-case, factorial, conditionals*

### Q6. Will This Code Return Palindromes?

**Source:** `16_morerecursion.pptx` slide 10 - worked answer in `16_morerecursion.pdf`

Will This Code Return Palindromes?

```python
def pal(x):
	if x[0] != x[len(x)-1]:
		return False
	else return pal(x[1:len(x)-1])
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF circles B (No) with 'what about True?' written beside it - the function has no base case and can never return True.

**Code check:** confirmed by execution

**Extraction note:** Slide code prints 'else return pal(...)' on one line without a colon (verbatim from the slide); the defect discussed in class is the missing base case, not the syntax. Option letters A/B/C are explicit on the PDF though the text dump shows only the bodies.

*Also touches: base-case, strings, palindrome, booleans-and-logic*

### Q7. Which code is correct?

**Source:** `16_morerecursion.pptx` slide 11 - worked answer in `16_morerecursion.pdf`

Which code is correct?

- **A.** def pal(x):
	if len(x) <=1:
		return True
	elif x[0] != x[len(x)-1]:
		return False
	else return pal(x)
- **B.** def pal(x):
	if x[0] != x[len(x)-1]:
		return False
	else return pal(x[1:len(x)-1])
- **C.** def pal(x):
	if len(x) <=0:
		return True
	elif x[0] != x[len(x)-1]:
		return False
	else return pal(x[1:len(x)-1])
- **D.** def pal(x):
	if len(x) <=1:
		return True
	elif x[0] != x[len(x)-1]:
		return False
	else return pal(x[1:len(x)-1])
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF circles D; annotations underline A's pal(x) call (argument never shrinks), write 'no True' next to B (no base case), and trace test words (racecar, tacocat) on C and D.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option labels matched to code blocks via pptx shape positions (A top-left, B top-right, C bottom-left, D bottom-right) because the dump interleaves them out of order; confirmed against the PDF layout. All options print 'else return' without a colon (verbatim). Note: option C (base case len(x)<=0) also behaves correctly in Python since slicing a 1-character string yields '', but the instructor's recorded answer is D only.

*Also touches: base-case, strings, palindrome*

### Q8. Base Case (for the snowflake function: what should the base case do?)

**Source:** `17_fractals.pptx` slide 9 - worked answer in `17_fractals.pdf`

Base Case (for the snowflake function: what should the base case do?)

- **A.** Draw nothing
- **B.** Draw a line
- **C.** Draw a triangle
- **D.** Draw a line with a pointy bit
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF (page 11) has B circled.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide text is only the title "Base Case"; the question context (designing the Koch snowflake side function for the lab) is implicit from surrounding slides - parenthetical added to the prompt for clarity.

*Also touches: fractals, base-case, program-design*

### Q9. How many times will I call snowflake when I recur?

**Source:** `17_fractals.pptx` slide 11 - worked answer in `17_fractals.pdf`

How many times will I call snowflake when I recur?

- **A.** 1
- **B.** 3
- **C.** 4
- **D.** 12
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF (page 13) has C circled with the worked call sequence snowflake-rotate-snowflake-rotate-snowflake-rotate-snowflake written out.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide shows a star (one-level Koch snowflake) image annotated in the PDF.

*Also touches: fractals, recursive-case*

### Q10. How long will each new segment be in terms of the original line?

**Source:** `17_fractals.pptx` slide 12 - worked answer in `17_fractals.pdf`

How long will each new segment be in terms of the original line?

- **A.** 1/6
- **B.** 1/4
- **C.** 1/3
- **D.** 1/2
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF (page 14) has C circled, with a parameter sketch (pic, depth then depth-1, width) written beside it.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options B and D were curly one-quarter and one-half glyphs, normalized to 1/4 and 1/2.

*Also touches: fractals, self-similarity, geometry*

### Q11. What Parameters Should Our Function Take? (for drawing Sierpinski's carpet)

**Source:** `17_fractals.pptx` slide 15 - worked answer in `17_fractals.pdf`

What Parameters Should Our Function Take? (for drawing Sierpinski's carpet)

- **A.** Recursion Depth
- **B.** XY coordinates
- **C.** Size of Canvas
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Notes say "D - all", i.e. the function needs all of depth, coordinates, and size; slide absent from the annotated PDF (carpet section not included), so notes only.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Carpet-section context added to the prompt in parentheses (slide follows the Sierpinski's carpet title slide).

*Also touches: functions, fractals, program-design*

### Q12. The base case for carpet(pic, d, x, y, size) should

**Source:** `17_fractals.pptx` slide 16 - worked answer in `17_fractals.pdf`

The base case for carpet(pic, d, x, y, size) should

- **A.** Draw a size square at coordinate x,y
- **B.** Draw a size//3 square at coordinates x,y
- **C.** Draw a size//3 square at coordinates x + x//3, y + y//3
- **D.** Draw a size//4 square at coordinates x + x//4, y - y//4
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Notes say C; slide absent from the annotated PDF (carpet section not included), so notes only.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option C's offsets read "x + x//3, y + y//3" verbatim on the slide (likely intended as size//3 offsets); transcribed as written. Slide absent from annotated PDF.

*Also touches: fractals, base-case, integer-division*

### Q13. The recursive case for carpet(pic, d, x, y, size) should

**Source:** `17_fractals.pptx` slide 17 - worked answer in `17_fractals.pdf`

The recursive case for carpet(pic, d, x, y, size) should

- **A.** Call carpet(pic, d-1, x,y, size//3) 3 times, with appropriate x,y coordinates
- **B.** Draw a square in the center, and then call carpet recursively 3 times
- **C.** Draw a square in the center, and then call carpet recursively 8 times
- **D.** Draw a square in the center, and then call carpet recursively 9 times
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Notes say C (Sierpinski's carpet recurses on the 8 sub-squares around the center); slide absent from the annotated PDF (carpet section not included), so notes only.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide absent from annotated PDF.

*Also touches: fractals, recursive-case*

### Q14. What will the output & return value of this code be?

**Source:** `25_review.pptx` slide 10 - worked answer in `25_review.pdf`

What will the output & return value of this code be?

```python
def A(x) :
    print(x)
    if (x == 0) :
        return 1
    else :
        r = x//2
        return 1 + A(r)

A(5)
```

- **A.** 5 2 1 0, 5
- **B.** 5 2 1 0, 4
- **C.** 5 2 1, 4
- **D.** 5 2 1, 3
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; calls print 5, 2, 1, 0 and returns 1 + 1 + 1 + 1 = 4; PDF has no handwriting.

**Code check:** confirmed by execution

**Extraction note:** Options are laid out in two columns on the slide (A-C left, D-E right); pairing confirmed against the PDF render. A lost newline between 'else :' and 'r = x//2' in the text dump was restored from the PDF.

*Also touches: functions, integer-division, tracing*

### Q15. What will this print?

**Source:** `35_review.pptx` slide 2 - worked answer in `35_review.pdf`

What will this print?

```python
def R(s) :
	if len(s) == 0 :
		return ""
	else :
		return s[0] + R(s[1:]) + s[0]

print(R("cat"))
```

- **A.** taccat
- **B.** tacat
- **C.** cattac
- **D.** catac
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF circles D, but executing the code as shown prints cattac (option C); the handwritten 'base case 1' note indicates D is the output only if the base case is len(s) == 1 returning s.

**Code check:** confirmed by execution - caveat: Answer D is correct for the intended function (base case len(s)==1 returning s); the code as printed on the slide has a base-case bug (len 0 returning "") that doubles the middle letter and actually prints "cattac" (option C).

**Extraction note:** Recorded answer D contradicts actual execution of the transcribed code, which prints 'cattac' (option C); the slide's base case (len 0, return "") doubles the innermost character. PDF annotation 'base case 1' and a sketched s[-1]+R(s[:-1])+s[-1] variant show the class discussed this. Likely a bug in the slide's base case.

*Also touches: strings, code-tracing*

#### Practice exercises (Recursion)

### Q16. Write code for the Fibonaccis using recursion. Spec given: f(x) = f(x-1) + f(x-2); if (...

**Source:** `16_morerecursion.pptx` slide 6 - worked answer in `16_morerecursion.pdf` (practice exercise, no answer options)

Write code for the Fibonaccis using recursion. Spec given: f(x) = f(x-1) + f(x-2); if (x < 2) then f(x) = 1.

```python
def fibs(n):
	if (                    ):
				return

	return
```

**Answer:** def fibs(n):
	if (n < 2):
		return 1
	else:
		return fibs(n-1) + fibs(n-2) (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes and the PDF page is unannotated, but slide 8 of this same deck displays this completed recursive version, so the solution is taken from there.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Slide provides a fill-in skeleton (blank if condition and returns).

*Also touches: fibonacci, base-case, functions*

### Q17. What will this code draw?

**Source:** `17_fractals.pptx` slide 2 - worked answer in `17_fractals.pdf` (practice exercise, no answer options)

What will this code draw?

```python
def boop(pic, x, d) :
    if x == 0 :
        pic.drawForward(d)
        pic.display()
    else :
        boop(pic,x-1,d)
        pic.rotate(90)
        boop(pic,x-1,d)
        pic.rotate(-90)
        boop(pic,x-1,d)
        pic.rotate(-90)
        boop(pic,x-1,d)
        boop(pic,x-1,d)
        pic.rotate(90)
        boop(pic,x-1,d)
        pic.rotate(90)
        boop(pic,x-1,d)
        pic.rotate(-90)
        boop(pic,x-1,d)

boop(pic,4,4)
```

**Answer:** A fractal - the quadratic Koch curve (Minkowski sausage): each line is recursively replaced by 8 smaller segments with 90-degree turns (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes or PDF (PDF page 4 only underlines the d parameter and the matching 4 argument in the call); inferred - the 8 recursive calls with turn pattern +90, -90, -90, 0, +90, +90, -90 are the quadratic Koch curve generator, and the deck immediately pivots to defining fractals.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Opening hook slide, not in the candidate list; poses a prediction question with no multiple-choice options, captured as an exercise.

*Also touches: fractals, code-tracing, graphics*

### Q18. Write a function sum(A) that takes a list of integers and RECURSIVELY adds together all...

**Source:** `25_review.pptx` slide 11 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Write a function sum(A) that takes a list of integers and RECURSIVELY adds together all the integers, returning a single integer value.

**Answer:** def sum(A):
    if len(A) == 0:
        return 0
    return A[0] + sum(A[1:]) (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (empty-list base case, first element plus recursive sum of the rest).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: lists, functions*

### Q19. Write a recursive function lessThan(L,e) that takes a list L and an element e, and retu...

**Source:** `35_review.pptx` slide 3 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Write a recursive function lessThan(L,e) that takes a list L and an element e, and returns True if all of the elements of L are less than e, and False otherwise. You cannot make any assumptions about what type of objects e and the elements of L are, but you can assume that <, >, = etc work. Do not use loops.

**Answer:** not recorded in the source materials

*Also touches: lists, booleans-and-logic*

### Q20. Write a function tree(n), which takes in a number and draws a lovely tree like the ones...

**Source:** `35_review.pptx` slide 14 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Write a function tree(n), which takes in a number and draws a lovely tree like the ones pictured below.

**Answer:** not recorded in the source materials

**Extraction note:** The referenced tree pictures are images with no extractable text; the classic intent is a recursive (turtle-style) tree drawing.

*Also touches: turtle-graphics*
