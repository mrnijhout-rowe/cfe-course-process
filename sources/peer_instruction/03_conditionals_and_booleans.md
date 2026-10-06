# Peer Instruction Questions: Conditionals and Boolean Logic

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Conditionals

### Q1. At the end of this code, what will appear on the terminal?

**Source:** `06_conditionals.pptx` slide 4 - worked answer in `06_conditionals.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 1
if (x < 3):
    print(x)
    x = x + 4
    print(x)
```

- **A.** Nothing
- **B.** 1
- **C.** 5
- **D.** 1
5
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D; annotated PDF circles option D (1 then 5) - x < 3 is true so the whole body runs, printing 1 and then 5.

**Code check:** confirmed by execution

*Also touches: variables-and-assignment, program-tracing*

### Q2. At the end of this code, what will appear on the terminal?

**Source:** `06_conditionals.pptx` slide 6 - worked answer in `06_conditionals.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 1
if (x < 3):
    print(x)
else:
    print(x+7)
```

- **A.** Nothing
- **B.** 1
- **C.** 8
- **D.** 1
8
- **E.** I don't know

**Answer:** B (from her handwritten in-class annotations (PDF))

**Detail:** Annotated PDF circles option B ('1') and marks the condition true with the else branch crossed out; speaker notes say A, but B matches actual execution (x=1, x<3 is true, print(x) outputs 1).

**Code check:** confirmed by execution

**Extraction note:** Notes and PDF disagree: notes say A, PDF circles B; PDF preferred and also matches running the code, so the notes letter appears to be an error.

*Also touches: if-else, program-tracing*

### Q3. At the end of this code, what will appear on the terminal?

**Source:** `06_conditionals.pptx` slide 10 - worked answer in `06_conditionals.pdf`

At the end of this code, what will appear on the terminal?

```python
grade = 98
if (grade >= 90):
    print("You got an A!")
if (grade >= 80):
    print("You got a B!")
else:
    print("You got something else")
```

- **A.** You got an A!
- **B.** You got a B!
- **C.** You got something else!
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - A and B'; PDF circles D and brackets options A and B together - both ifs are independent, so both messages print.

**Code check:** confirmed by execution

*Also touches: if-else, sequential-ifs, program-tracing*

### Q4. At the end of this code, what will appear on the terminal?

**Source:** `06_conditionals.pptx` slide 11 - worked answer in `06_conditionals.pdf`

At the end of this code, what will appear on the terminal?

```python
grade = 98
if (grade >= 90):
    print("You got an A!")
if (grade >= 80 and grade < 90):
    print("You got a B!")
else:
    print("You got something else")
```

- **A.** You got an A!
- **B.** You got a B!
- **C.** You got something else!
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - A and C'; PDF circles D (with A and C also circled) - the first if prints the A message, the and-condition is false so the else prints the something-else message.

**Code check:** confirmed by execution

*Also touches: booleans-and-logic, if-else, program-tracing*

### Q5. Which code prints the correct output?

**Source:** `06_conditionals.pptx` slide 12 - worked answer in `06_conditionals.pdf`

Which code prints the correct output?

- **A.** grade = 98
if (grade >= 90):
    print("You got an A!")
if (grade >= 80 and grade < 90):
    print("You got a B!")
if (grade < 80):
    print("You got something else")
- **B.** grade = 98
if (grade >= 90):
    print("You got an A!")
elif (grade >= 80):
    print("You got a B!")
else:
    print("You got something else")
- **C.** grade = 98
if (grade >= 90):
    print("You got an A!")
elif (grade >= 80):
    print("You got a B!")
elif(grade < 80):
    print("You got something else")
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - All of them'; PDF circles D (A, B, and C are each also circled) - every version prints only 'You got an A!' for grade = 98.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Follows slides 10-11: 'the correct output' means printing only 'You got an A!' for grade = 98. Option labels were paired with the three code blocks using pptx shape positions and the annotated PDF layout (top-left A, top-right B, bottom-right C).

*Also touches: booleans-and-logic, if-elif-else, code-comparison*

### Q6. This will output

**Source:** `07_whileloops.pptx` slide 2 - worked answer in `07_whileloops.pdf`

This will output

```python
x = 5
if (x < 3):
	x = 1
	print("A")
	if(x>100):
			print("B")
	else:
			print("C")
	print("D")
print("E")
if (x>2):
	print("F")
	if(x%3==2):
			print("G")
	if (x%3==1):
			print("H")
	else:
			print("I")
```

- **A.** C D E F G I
- **B.** D E F G
- **C.** E F G I
- **D.** E F H
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C; PDF shows C circled with the trace worked in ink (x < 3 is False so the first block is skipped, then E F G I print).

**Code check:** confirmed by execution

*Also touches: nested-conditionals, code-tracing, modulo*

### Q7. What code can be removed without changing the meaning?

**Source:** `09_morefunctions.pptx` slide 13 - worked answer in `09_morefunctions.pdf`

What code can be removed without changing the meaning?

```python
age = int(input("Enter your age: "))
if age < 18:
	print("Youngin")
elif age >= 18 and age < 35:
	print("Grown up")
elif age >= 35:
	print("Older than Cynthia")
else:
	print("ageless")
```

- **A.** The red can be removed
- **B.** The blue can be removed
- **C.** Both red and blue can be removed
- **D.** Nothing can be removed
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and the PDF circles C, striking out the redundant age >= 18 test and the unreachable else clause.

**Code check:** confirmed by execution

**Extraction note:** Options refer to slide colors: red = 'age >= 18' in the first elif condition, blue = the else clause with print("ageless").

*Also touches: booleans-and-logic, code-simplification*

### Q8. Rewrite this code using Elif

**Source:** `14_Review.pptx` slide 3 - worked answer in `14_Review.pdf`

Rewrite this code using Elif

```python
grade = 98
if (grade >= 90):
	print('You got an A!')
if (grade >= 80 and grade < 90):
	print('You got a B!')
if (grade < 80):
	print ( 'You got something else ')
```

- **A.** grade = 98
if (grade >= 90):
	print('You got an A!')
elif (grade < 90):
	print('You got a B!')
elif (grade >= 80):
	print('You got a B!')
elif (grade < 80):
	print ( 'You got somethin')
- **B.** grade = 98
if (grade >= 90):
	print('You got an A!')
elif (grade >= 80):
	print('You got a B!')
else:
	print ( 'You got somethin')
- **C.** grade = 98
elif (grade >= 90):
	print('You got an A!')
elif (grade >= 80):
	print('You got a B!')
elif (grade < 80):
	print ( 'You got somethin')
- **D.** grade = 98
if (grade >= 90):
	print('You got an A!')
elif (grade >= 80) and (grade < 90):
	print('You got a B!')
else:
	print ( 'You got somethin')
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and B is circled in the annotated PDF; the instructor marked A's elif (grade < 90) branch as redundant, C as missing its initial if, and D's extra and (grade < 90) condition as unnecessary.

**Code check:** confirmed by execution

**Extraction note:** Option-letter pairing verified via pptx shape positions and the annotated PDF (two-column layout with interleaved labels in the text dump).

*Also touches: elif, code-rewriting*

#### Practice exercises (Conditionals)

### Q9. Change to a Z

**Source:** `06_conditionals.pptx` slide 16 - worked answer in `06_conditionals.pdf` (practice exercise, no answer options)

Change to a Z

**Answer:** Keep the nested loops from slide 15 and change the condition to print "*" when (row == 0 or row == n+1 or row + col == n+1), giving the top row, bottom row, and anti-diagonal of a Z. (inferred during extraction - not marked in the source materials)

**Detail:** No usable recorded answer - inferred by adapting the slide-15 N code to the Z image on the slide; the speaker notes contain only the letter 'C' with no options anywhere to match it against.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Slide contains only the title and an image of a Z star pattern (top row, anti-diagonal, bottom row; n=3); it is a follow-up modifying the slide-15 code. Speaker notes say 'C', suggesting it ran as a clicker with options given verbally or on the board, but no options are recoverable; the annotated PDF omits this slide entirely, replacing it with a blank 'Write Code' page.

*Also touches: nested-loops, booleans-and-logic, pattern-printing*

## Booleans and logic

### Q10. After this code, y is equal to

**Source:** `07_whileloops.pptx` slide 4 - worked answer in `07_whileloops.pdf`

After this code, y is equal to

```python
x = 7

y = (x > 4) and ((not (x > 8)) or (x == 5))
```

- **A.** True
- **B.** False
- **C.** It depends
- **D.** This will cause an error
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A; PDF circles option A with T/F values worked over each subexpression (True and (True or False) -> True).

**Code check:** confirmed by execution

**Extraction note:** Annotated PDF edition words options A/B as 'y = true' / 'y = false'; the pptx slide text has 'True' / 'False'. Same options, same answer.

*Also touches: and-or-not, expression-evaluation*

### Q11. Which parts will be evaluated?

**Source:** `09_morefunctions.pptx` slide 9 - worked answer in `09_morefunctions.pdf`

Which parts will be evaluated?

```python
(7>2) or ((9<2) and (8>3))
```

- **A.** Only the red code
- **B.** Only the green code
- **C.** The red code and the green code
- **D.** All of the code is evaluated
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A and the PDF circles A, crossing out the right side: (7>2) is True so or short-circuits.

**Code check:** confirmed by execution

**Extraction note:** Options refer to slide colors: red = (7>2), green = (9<2), blue = (8>3).

*Also touches: short-circuit-evaluation*

### Q12. Which parts will be evaluated?

**Source:** `09_morefunctions.pptx` slide 10 - worked answer in `09_morefunctions.pdf`

Which parts will be evaluated?

```python
((7>2) and (9<2)) or (8>3)
```

- **A.** Only the red code
- **B.** Only the green code
- **C.** The red code and the green code
- **D.** All of the code is evaluated
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF circles D with T/F annotations: the left and is False, so the right side of or must also be evaluated.

**Code check:** confirmed by execution

**Extraction note:** Options refer to slide colors: red = (7>2), green = (9<2), blue = (8>3).

*Also touches: short-circuit-evaluation*

### Q13. Which of the following does exactly the same thing?

**Source:** `09_morefunctions.pptx` slide 11 - worked answer in `09_morefunctions.pdf`

Which of the following does exactly the same thing?

```python
def is_odd(x):
	if x%2 == 1:
		return True
	else:
		return False
```

- **A.** def is_odd(x):
	return x%2
- **B.** def is_odd(x):
	return x%2 == 1
- **C.** def is_odd(x):
	return x%2 == 0
- **D.** None of the above
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF boxes B; handwriting notes A returns a number (0/1) not a boolean and C tests even.

**Code check:** confirmed by execution

*Also touches: functions, return-values, modulus*

### Q14. Write a boolean expression that will evaluate to False if and only if y is equal to 11.

**Source:** `14_Review.pptx` slide 10 - worked answer in `14_Review.pdf`

Write a boolean expression that will evaluate to False if and only if y is equal to 11.

- **A.** y == 11
- **B.** y != 11
- **C.** y >= 11
- **D.** y and 11
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and B is circled in the annotated PDF with 'False' written beside it.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** The annotated PDF's rendering of the prompt reads 'evaluate to False if y is equal to 11' (without 'and only if'); the pptx text, transcribed here, includes 'if and only if'.

*Also touches: comparison-operators*

### Q15. A XOR B

**Source:** `21_boolean.pptx` slide 10

A XOR B

- **A.** A OR B
- **B.** NOT (A AND B) AND (A OR B)
- **C.** ((NOT A) OR (NOT B)) AND NOT (A AND B)
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'D - B & C', i.e. options B and C were both intended to be equivalent to XOR.

**Concept check:** caveat - as printed, only B is equivalent to XOR (option C simplifies by De Morgan to NAND, differing at A=B=0); the recorded D holds only under the intended XOR reading of C (likely slide typo, see extraction note).

**Extraction note:** Likely slide typo, verified verbatim against the pptx: option C as printed simplifies by De Morgan to NOT (A AND B) (NAND, not XOR). It was probably meant to be '((NOT A) OR (NOT B)) AND (A OR B)', which is XOR and would make the notes' answer D correct.

*Also touches: digital-logic, xor, boolean-algebra*

### Q16. Majority of A,B,C are True

**Source:** `21_boolean.pptx` slide 12

Majority of A,B,C are True

- **A.** A or (B and C)
- **B.** (A and B) or (A and C) or (A and C)
- **C.** (A and (B or C)) or (B and C)
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'D - B and C', i.e. options B and C were both intended to express the majority function.

**Concept check:** caveat - as printed, only C expresses the majority function (option B repeats "(A and C)" and reduces to A and (B or C), failing at A=0, B=1, C=1); the recorded D holds only under the intended "(B and C)" reading of B (likely slide typo, see extraction note).

**Extraction note:** Likely slide typo, verified verbatim against the pptx: option B repeats '(A and C)' and was almost certainly meant to be '(A and B) or (A and C) or (B and C)'. As printed, B reduces to A and (B or C), which is not majority; only C is correct as printed, but the notes treat B and C as both correct.

*Also touches: digital-logic, majority-function, boolean-algebra*

### Q17. A AND (B OR C) = (A AND C) OR (A AND B)

**Source:** `25_review.pptx` slide 5 - worked answer in `25_review.pdf`

A AND (B OR C) = (A AND C) OR (A AND B)

- **A.** True
- **B.** False
- **C.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; this is the distributive law, and slide 6 sets up the truth-table verification; PDF has no handwriting.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide 6 is the worked truth-table follow-up for this question.

*Also touches: boolean-identities, truth-tables, distributive-law*

### Q18. NOT (A OR B) = (NOT A) AND (NOT B)

**Source:** `25_review.pptx` slide 7 - worked answer in `25_review.pdf`

NOT (A OR B) = (NOT A) AND (NOT B)

- **A.** True
- **B.** False
- **C.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; De Morgan's law, and slide 8's completed truth table shows LHS = RHS on all four rows; PDF has no handwriting.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide 8 is the worked truth-table follow-up for this question.

*Also touches: de-morgans-law, truth-tables*

### Q19. Suppose A, B and C are boolean variables. Write a boolean expression that evaluates to...

**Source:** `35_review.pptx` slide 5 - worked answer in `35_review.pdf`

Suppose A, B and C are boolean variables. Write a boolean expression that evaluates to true if and only if one or more of these variables are False.

- **A.** (not A) and (not B) and (not C)
- **B.** (not A) or (not B) or (not C)
- **C.** not (A and B and C)
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - B and C'; PDF circles B, C, and D, with a note beside A that it requires all to be False. B and C are equivalent by De Morgan's law, so D.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: de-morgans-law*
