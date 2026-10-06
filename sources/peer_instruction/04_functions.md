# Peer Instruction Questions: Functions

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. This code will print:

**Source:** `08_Functions.pptx` slide 7 - worked answer in `08_Functions.pdf`

This code will print:

```python
def foo():
	print("Raaarrr I'm a bear")

def bar():
	print("Eeek a bear!")

foo()
```

- **A.** Raaarrr I'm a bear
- **B.** Eeek a bear!
- **C.** Both
- **D.** Neither
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says A and the PDF circles A, with handwriting noting we never call bar().

**Code check:** confirmed by execution

*Also touches: function-calls, defining-vs-calling*

### Q2. What will the output be?

**Source:** `08_Functions.pptx` slide 10 - worked answer in `08_Functions.pdf`

What will the output be?

```python
def first(a):
	a=8

a = 20
first(a)
print(a)
```

- **A.** 0
- **B.** 8
- **C.** 20
- **D.** Error, because a cannot be assigned in two places
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says C and the PDF circles C with a memory diagram showing the function's local a=8 is separate from main's a=20.

**Code check:** confirmed by execution

*Also touches: parameter-passing, variable-scope*

### Q3. What will the output be?

**Source:** `08_Functions.pptx` slide 12 - worked answer in `08_Functions.pdf`

What will the output be?

```python
def calculate(w, x, y):
	a=x
	b=w+1
	return a + b + 3

print(calculate(3, 2, 5))
```

- **A.** 5
- **B.** 9
- **C.** 0
- **D.** 3
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says B and the PDF circles B; a=x=2, b=w+1=4, return 2+4+3=9.

**Code check:** confirmed by execution

**Extraction note:** Options were laid out in a multi-column box layout; label pairing (A=5, B=9, C=0, D=3) confirmed via pptx shape positions and the PDF. The annotated PDF shows an earlier version calling calculate(3, 2, 0) instead of (3, 2, 5); y is unused so the answer is 9 either way.

*Also touches: return-values, parameter-passing*

### Q4. Which assigns x to 5?

**Source:** `08_Functions.pptx` slide 13 - worked answer in `08_Functions.pdf`

Which assigns x to 5?

```python
def f1():
	return 5

def f2():
	print(5)

def f3():
	return print(5)
```

- **A.** x = f1()
- **B.** x = f2()
- **C.** x = f3()
- **D.** All of the above
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says A and the PDF circles A, with handwriting noting f2 returns None (it only prints 5) and f3 is weirdness.

**Code check:** confirmed by execution

*Also touches: return-vs-print, return-values*

### Q5. What are the bugs in the following code?

**Source:** `08_Functions.pptx` slide 14 - worked answer in `08_Functions.pdf`

What are the bugs in the following code?

```python
def add_one(x):
return x + 1

x = 2
x = x + add_one(x)
```

- **A.** No bugs.  The code is fine.
- **B.** The function body is not indented.
- **C.** We use x as both a parameter and a variable, but we are not allowed to do that
- **D.** B and C
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says B and the PDF circles B, with an arrow at the unindented return line; the handwritten memory diagram shows reusing x as parameter and variable is legal.

**Code check:** confirmed by execution

**Extraction note:** The unindented return line is intentional (it is the bug); code transcription verified against the PDF because the dump lost a soft line break in x = 2 / x = x + add_one(x).

*Also touches: indentation, debugging, variable-scope*

### Q6. What will the output be?

**Source:** `08_Functions.pptx` slide 15 - worked answer in `08_Functions.pdf`

What will the output be?

```python
def odd(y,x):
	y = y +1
	x = x + 1
	print(x*y)

def main():
	x = 2
	y = 4
	odd(x,y)
	print(x*y)
```

- **A.** 8
8
- **B.** 15
15
- **C.** 8
15
- **D.** 15
8
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says D and the PDF circles D; odd(x,y) binds y=2 and x=4 (swapped names), prints 5*3=15, then main prints its unchanged x*y=8.

**Code check:** confirmed by execution

**Extraction note:** Each option is a two-line output shown in a box; label pairing (A=8/8, B=15/15, C=8/15, D=15/8) confirmed via pptx shape positions and the PDF.

*Also touches: parameter-passing, argument-order, variable-scope*

### Q7. What will the output be?

**Source:** `09_morefunctions.pptx` slide 4 - worked answer in `09_morefunctions.pdf`

What will the output be?

```python
def calculate(w, x, y):
	a=x
	b=w+1
	return a + b - y

w = 1
x = 2
y = 3

print(calculate(x,y,w))
```

- **A.** 1
- **B.** 3
- **C.** 5
- **D.** 7
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and the PDF circles C (5) with a worked memory diagram: calculate(2,3,1) gives a=3, b=3, returns 3+3-1=5.

**Code check:** confirmed by execution

*Also touches: parameter-passing, argument-order, tracing*

### Q8. What will the output be?

**Source:** `09_morefunctions.pptx` slide 5 - worked answer in `09_morefunctions.pdf`

What will the output be?

```python
def a(num):
	num = 4
	return 2

def b(val):
	num = 8
	print(a(1))

b(2)
```

- **A.** 1
- **B.** 2
- **C.** 4
- **D.** Error because of an undefined variable
- **E.** I don't know

**Answer:** B (from her handwritten in-class annotations (PDF))

**Detail:** PDF circles B (2) with a worked memory diagram; speaker notes say C, but a(1) returns 2 so b(2) prints 2 - PDF preferred.

**Code check:** confirmed by execution

**Extraction note:** Notes ('C') and annotated PDF (B circled) disagree; PDF matches actual code behavior and is preferred. Option layout A=1, B=2, C=4, D=Error verified via pptx shape positions.

*Also touches: scope, local-variables, return-values*

### Q9. Which code prints the correct output?

**Source:** `09_morefunctions.pptx` slide 19 - worked answer in `09_morefunctions.pdf`

Which code prints the correct output?

- **A.** def isFib(n):
	for i in range(n):
		if fib(i) == n:
			return True
		if fib(i) > n:
			return False
	return False
- **B.** def isFib(n):
	i = 1
	f = fib(i)
	isFib = False
	while (f < n):
			i = i + 1
			f = fib(i)
			if f == n:
				return True
	return False
- **C.** def isFib(n):
	i = 1
	while (fib(i) < n):
			i = i + 1
	return fib(i) == n
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'D - All of them'; slide absent from the annotated PDF so no handwritten confirmation.

**Concept check:** DISCREPANCY - the notes say D (all of them), but tested against a working fib, option A returns False for the Fibonacci numbers 2 and 3, and option B returns False for 1; only C is correct for every input, under either fib indexing convention. No slide typo explains the gap. VERIFY THE ANSWER BEFORE USING THIS QUESTION.

**Extraction note:** Not in the annotated PDF (PDF ends before this slide). Depends on fib(n) from slide 17 and the task posed on slide 18. Option-label pairing (A=for-loop, B=flag-while, C=short-while) verified via pptx shape positions. Option indentation reproduced as shown on the slide, including the over-indented while bodies.

*Also touches: while-loops, for-loops, fibonacci, code-evaluation*

### Q10. Which code prints the correct output?

**Source:** `09_morefunctions.pptx` slide 21 - worked answer in `09_morefunctions.pdf`

Which code prints the correct output?

- **A.** def notFib(n):
	return not isFib(n)
- **B.** def notFib(n):
	i = 1
	while(fib(i) < n):
			i = i + 1
	return fib(i) == n
- **C.** def notFib(i):
	answer = not isFib(n)
	return answer
- **D.** More than one of the above
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; consistent with the code - B is just isFib again and C's parameter is i so n is undefined inside it.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Not in the annotated PDF (PDF ends before this slide). Option-label pairing (A=not isFib(n), B=while-loop, C=mis-parameterized version) verified via pptx shape positions.

*Also touches: booleans-and-logic, scope, parameter-naming*

### Q11. Write a Python function called min(a,b,c) that takes in integers a,b,c and returns the...

**Source:** `14_Review.pptx` slide 5 - worked answer in `14_Review.pdf`

Write a Python function called min(a,b,c) that takes in integers a,b,c and returns the smallest.

- **A.** def min(a,b,c):
	smallest = a
	if (b < smallest):
		smallest = b
	if (c < smallest)
		smallest = c
	return smallest
- **B.** def min(a,b,c):
	min = a
	if (b < min):
		min = b
	if (c < smallest)
		min = c
- **C.** def min(a,b,c):
	smallest = a
	if (b < smallest):
		smallest = b
	if (c < smallest)
		smallest = c
min()
- **D.** def min(a,b,c):
	smallest = a
	if (b > smallest):
		smallest = b
	if (c > smallest)
		smallest = c
	return smallest
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A and A is circled in the annotated PDF; the instructor annotated B with the missing return and its stray smallest reference, and D's > comparisons compute the largest.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** All code options print 'if (c < smallest)' (or the > variant) without a trailing colon exactly as shown on the slide; transcribed verbatim. Option-letter pairing verified via pptx shape positions and the annotated PDF.

*Also touches: conditionals, return-values*

### Q12. What does this print?

**Source:** `14_Review.pptx` slide 8 - worked answer in `14_Review.pdf`

What does this print?

```python
def woot(x):
	print (x)
	yar(x + 1)
	print (x)
	yar(x+2)

def yar(y):
	if y>5:
		print (y*2)
	else :
		foo(y+1)

def foo(z):
	print (z-1)
	yar(z+1)

def main():
	woot (3)

main()
```

- **A.** 3
4
12
3
10
- **B.** 3
4
12
3
5
14
- **C.** 3
4
10
10
24
- **D.** None of the above
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; the annotated PDF omits this options slide but the instructor's worked call trace on the preceding setup slide's page ends in the handwritten answer 3, 4, 12, 3, 5, 14, which is option B.

**Code check:** confirmed by execution

**Extraction note:** Unicode asterisk and minus signs in the slide code (y*2, z-1) normalized to ASCII. Annotated PDF has 12 pages and skips this slide; answer verified from the handwriting on the slide 7 page. Option-letter pairing verified via pptx shape positions.

*Also touches: code-tracing, conditionals, call-stack*

#### Practice exercises (Functions)

### Q13. What will this print?

**Source:** `09_morefunctions.pptx` slide 14 - worked answer in `09_morefunctions.pdf` (practice exercise, no answer options)

What will this print?

```python
def er(x):
	print(x)
	mah(x-1)
	mah(x-2)
	print(x)

def gerd(z):
	print("!")
	print(z*10)

def mah(x):
	print("?")
	gerd(x-2)
	print(x*x)
	gerd(x)

def main():
	er(5)
```

**Answer:** 5, ?, !, 20, 16, !, 40, ?, !, 10, 9, !, 30, 5 (each on its own line, assuming main() is called) (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes or PDF (slide absent from the annotated PDF); traced by hand: er(5) prints 5, mah(4) prints ? ! 20 16 ! 40, mah(3) prints ? ! 10 9 ! 30, then er prints 5.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Trace exercise with no multiple-choice options; slide 15 (not captured) is the worked in-class memory-diagram repeat of this problem.

*Also touches: tracing, function-calls*

### Q14. Use the fib function to create a isFib(n) function that takes a number, and returns Tru...

**Source:** `09_morefunctions.pptx` slide 18 - worked answer in `09_morefunctions.pdf` (practice exercise, no answer options)

Use the fib function to create a isFib(n) function that takes a number, and returns True if it is a Fibonacci number, and False if not

**Answer:** def isFib(n):
	i = 1
	while (fib(i) < n):
		i = i + 1
	return fib(i) == n (from Dr. Taylor's speaker notes)

**Detail:** No answer on this slide itself; slide 19 presents three implementations and its speaker notes confirm all three work - the simplest (option C there) is shown here.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Relies on the fib(n) function live-coded on slide 17 (solution in that slide's speaker notes).

*Also touches: while-loops, fibonacci, booleans-and-logic*

### Q15. Use the functions we've created to create a function notFib(n) that returns True if n i...

**Source:** `09_morefunctions.pptx` slide 20 - worked answer in `09_morefunctions.pdf` (practice exercise, no answer options)

Use the functions we've created to create a function notFib(n) that returns True if n is NOT a Fibonacci number, and False otherwise

**Answer:** def notFib(n):
	return not isFib(n) (from Dr. Taylor's speaker notes)

**Detail:** No answer on this slide itself; slide 21's speaker notes confirm option A there (return not isFib(n)) as the correct implementation.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: booleans-and-logic, function-composition*
