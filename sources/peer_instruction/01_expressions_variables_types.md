# Peer Instruction Questions: Expressions, Variables, and Types

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Expressions and types

### Q1. At the end of this code, what will appear on the terminal?

**Source:** `02_statements.pptx` slide 12 - worked answer in `02_statements.pdf`

At the end of this code, what will appear on the terminal?

```python
print(3*5)
print("3*5")
```

- **A.** 3*5
3*5
- **B.** 15
15
- **C.** 15
3*5
- **D.** 3*5
15
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C (draw memory); PDF has C circled with annotations marking the first argument as evaluated and the quoted one as a literal string.

**Code check:** confirmed by execution

*Also touches: strings, print-statements, string-literal-vs-expression*

### Q2. At the end of this code, what will appear on the terminal?

**Source:** `02_statements.pptx` slide 17 - worked answer in `02_statements.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 10-2*3
print(x)
```

- **A.** 4
- **B.** 6
- **C.** 24
- **D.** This will cause an error
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A (run code); PDF (page 20) has A circled with "order of operations" and the working 2*3 then 10-6 handwritten.

**Code check:** confirmed by execution

*Also touches: order-of-operations, operator-precedence*

### Q3. We want to get the last 4 digits of a 10 digit number, x

**Source:** `03_loops.pptx` slide 8 - worked answer in `03_loops.pdf`

We want to get the last 4 digits of a 10 digit number, x

- **A.** x%4
- **B.** x%1000
- **C.** x%10000
- **D.** x%100000
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF has C circled with worked examples 112%10=2 and 112%100=12 showing mod extracts trailing digits.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: mod-operator, operators*

### Q4. Select the correct type for each variable

**Source:** `10_typesexceptions.pptx` slide 6 - worked answer in `10_typesexceptions.pdf`

Select the correct type for each variable

```python
a = 7+3
b = 3.1415
c = 7 < 3
```

- **A.** a: int, b: int, c: int
- **B.** a: int, b: float, c: boolean
- **C.** a: int, b: float, c: int
- **D.** a: float, b: real, c: boolean
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says B and B is circled in the annotated PDF; 7+3 is int, 3.1415 is float, 7 < 3 is boolean.

**Code check:** confirmed by execution

**Extraction note:** Options were a table (columns: a = 7+3, b = 3.1415, c = 7 < 3; one type per column per row), flattened here to 'variable: type' lists; the code field holds the three column-header assignments.

*Also touches: booleans-and-logic, type-of-literal*

### Q5. What type will this print?

**Source:** `10_typesexceptions.pptx` slide 7 - worked answer in `10_typesexceptions.pdf`

What type will this print?

```python
def add(x,y):
	z = x+y
	return z

print(type(add(5,1)))
```

- **A.** int
- **B.** function
- **C.** real
- **D.** This will cause an error
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says A and A is circled in the PDF, with 'evaluate' written under add(5,1) - the call returns 6, so type() reports int.

**Code check:** confirmed by execution

*Also touches: functions, return-values*

### Q6. We want to print the value of i, i times.  Which code will do that?

**Source:** `10_typesexceptions.pptx` slide 9 - worked answer in `10_typesexceptions.pdf`

We want to print the value of i, i times.  Which code will do that?

- **A.** i = 5
print(i*i)
- **B.** i = 5
print(str(i)*str(i))
- **C.** i = 5
print(str(i)*i)
- **D.** None of the above
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says C and C is circled in the PDF; handwriting shows A prints 25, B is an error (str * str), and C prints "55555".

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options A-C are code snippets laid out in two columns; label-text pairing reconstructed from the dump and confirmed against the PDF layout.

*Also touches: strings, casting, string-repetition*

### Q7. Variable Types: what type should each of these variables be - Number of Pirates, Fracti...

**Source:** `14_Review.pptx` slide 2 - worked answer in `14_Review.pdf`

Variable Types: what type should each of these variables be - Number of Pirates, Fraction of Booty, Ship is Sinking, Captain's Name?

- **A.** Number of Pirates: int, Fraction of Booty: int, Ship is Sinking: string, Captain's Name: string
- **B.** Number of Pirates: float, Fraction of Booty: float, Ship is Sinking: int, Captain's Name: string
- **C.** Number of Pirates: int, Fraction of Booty: float, Ship is Sinking: boolean, Captain's Name: string
- **D.** Number of Pirates: float, Fraction of Booty: int, Ship is Sinking: int, Captain's Name: boolean
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and C is circled in the annotated PDF, with handwritten example captain names in quotes to reinforce that names are strings.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options are rows of a table on the slide; prompt reconstructed from the slide title plus the table's column headers (Clicker, Number of Pirates, Fraction of Booty, Ship is Sinking, Captain's Name).

*Also touches: variables-and-assignment*

### Q8. Recall that when we wanted to cut off all but two decimal places of a float, we multipl...

**Source:** `14_Review.pptx` slide 11 - worked answer in `14_Review.pdf`

Recall that when we wanted to cut off all but two decimal places of a float, we multiplied it by 100, cast it as a integer, and then divided it by 100 using float division. Why did we cast it as an int?

- **A.** Ints only have 2 decimal places
- **B.** Ints don't have any decimals
- **C.** It's easier to multiply ints
- **D.** Funsies
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Notes say B; the corresponding annotated PDF page has no handwriting to confirm or contradict.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: type-casting, floats*

## Variables and assignment

### Q9. At the end of this code, y will have what value assigned to it in memory?

**Source:** `02_statements.pptx` slide 7 - worked answer in `02_statements.pdf`

At the end of this code, y will have what value assigned to it in memory?

```python
y = 3 + 2 + 1
y = y + 2
```

- **A.** 2
- **B.** 6
- **C.** 8
- **D.** This code will cause an error.
- **E.** I don't know.

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF has C circled with worked steps y = 6 then y = 6 + 2 = 8.

**Code check:** confirmed by execution

*Also touches: expressions-and-types, code-tracing*

### Q10. At the end of this code, what will memory look like?

**Source:** `02_statements.pptx` slide 10 - worked answer in `02_statements.pdf`

At the end of this code, what will memory look like?

```python
y = 3
x = 7
y = 3 + 2 + 1
```

- **A.** [memory table] y: 6
- **B.** [memory table] y: 6, x: 7
- **C.** [memory table] y: 3, x: 7, y: 6
- **D.** [memory table] y: 3, x: 7
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF has B circled with a hand-drawn memory table showing y overwritten to 6 and x staying 7.

**Code check:** confirmed by execution

**Extraction note:** Options A-D are name/value memory-table diagrams with no slide text; table contents transcribed from the annotated PDF rendering.

*Also touches: memory-model, reassignment*

### Q11. At the end of this code, what will appear on the terminal?

**Source:** `02_statements.pptx` slide 13 - worked answer in `02_statements.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 7
print(x)
x = x + 1
print(x)
y = x - 3
print(x)
print(y)
```

- **A.** 7
8
5
5
- **B.** 7
8
8
5
- **C.** 7
7
7
4
- **D.** This will cause an error
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B (run code); PDF has B circled with hand-drawn memory boxes x:7, x:8, y:5 traced alongside the code.

**Code check:** confirmed by execution

**Extraction note:** Slide text used an en dash in "y = x - 3"; normalized to a plain hyphen. Trailing whitespace in the dumped code removed.

*Also touches: code-tracing, print-statements*

### Q12. At the end of this code, what will appear on the terminal?

**Source:** `02_statements.pptx` slide 14 - worked answer in `02_statements.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 3
y = 7
x = y
y = x
print(x)
print(y)
```

- **A.** 3
7
- **B.** 7
3
- **C.** 3
3
- **D.** 7
7
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D (run code); PDF has D circled with memory tables traced showing the original x value 3 is lost, leaving x = 7 and y = 7.

**Code check:** confirmed by execution

*Also touches: code-tracing, swap, value-overwrite*

### Q13. At the end of this code, what will appear on the terminal?

**Source:** `02_statements.pptx` slide 15 - worked answer in `02_statements.pdf`

At the end of this code, what will appear on the terminal?

```python
x = 3
y = 7
temp = x
x = y
y = temp
print(x)
print(y)
```

- **A.** 3
7
- **B.** 7
3
- **C.** 3
3
- **D.** 7
7
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B (run code); PDF has B circled with memory tables traced showing temp preserving 3 so the swap succeeds (x = 7, y = 3).

**Code check:** confirmed by execution

*Also touches: code-tracing, swap, temp-variable*
