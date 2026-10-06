# Peer Instruction Questions: Binary and Digital Logic

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Binary representation

### Q1. Note the value of the last two bits ranges from 0-3.  If we want to get that value from...

**Source:** `20_binary.pptx` slide 4

Note the value of the last two bits ranges from 0-3.  If we want to get that value from an arbitrary number, we should mod by

- **A.** 2
- **B.** 3
- **C.** 4
- **D.** 8
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state C; taking a number mod 4 yields the value of its last two binary digits (0-3).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: modulo, expressions-and-types*

### Q2. 110_2

**Source:** `20_binary.pptx` slide 9

110_2

- **A.** 3_10
- **B.** 6_10
- **C.** 11_10
- **D.** 12_10
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state B; 110 in binary is 4 + 2 + 0 = 6 in base 10.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide shows only the number; the implied task is converting binary to base 10. Base subscripts on the slide are rendered here with underscore notation (verified in pptx).

*Also touches: base-conversion*

### Q3. 99_10

**Source:** `20_binary.pptx` slide 13

99_10

- **A.** 1011011
- **B.** 1100011
- **C.** 1110011
- **D.** 1100101
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state B; 1100011 = 64 + 32 + 2 + 1 = 99.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide shows only the number; the implied task is converting base 10 to binary. Base subscript on the slide is rendered here with underscore notation (verified in pptx).

*Also touches: base-conversion*

### Q4. To shift a binary number over by 6 digits

**Source:** `20_binary.pptx` slide 16

To shift a binary number over by 6 digits

- **A.** Add 2^6
- **B.** Multiply by 6
- **C.** Multiply by 2^6
- **D.** Multiply by 2^12
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state C; shifting left by n binary digits multiplies the value by 2^n.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Exponents are superscripts on the slide, rendered here with caret notation (verified in pptx).

*Also touches: bit-shifting*

### Q5. 110 + 011 = ?

**Source:** `21_boolean.pptx` slide 6

110 + 011 = ?

- **A.** 111
- **B.** 1001
- **C.** 1011
- **D.** 1111
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; 110 (6) + 011 (3) = 1001 (9), consistent with binary addition with carries.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: binary-addition*

### Q6. 1001_2 in decimal is

**Source:** `25_review.pptx` slide 2 - worked answer in `25_review.pdf`

1001_2 in decimal is

- **A.** 6
- **B.** 9
- **C.** 10
- **D.** 18
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; binary 1001 = 8 + 1 = 9; PDF has no handwriting to check against.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide title renders the 2 as a subscript base indicator (1001 base 2); transcribed here as 1001_2.

*Also touches: base-conversion*

### Q7. 53 in binary is

**Source:** `25_review.pptx` slide 3 - worked answer in `25_review.pdf`

53 in binary is

- **A.** 10101
- **B.** 110101
- **C.** 110100
- **D.** 1101010
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; 53 = 110101, and the slide's typed repeated-division table (53, 26, 13, 6, 3, 1 with remainders 1 0 1 0 1 1) works this out; PDF has no handwriting.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Slide includes a division-by-2 remainder table (visible in the PDF render) that builds the answer, likely revealed by animation.

*Also touches: base-conversion*

#### Practice exercises (Binary representation)

### Q8. Write a program to convert from a string representing the number in binary to an integer

**Source:** `20_binary.pptx` slide 10 (practice exercise, no answer options)

Write a program to convert from a string representing the number in binary to an integer

**Answer:** not recorded in the source materials

**Detail:** No solution appears on the slide or in the speaker notes; worked live in class.

*Also touches: strings, for-loops, base-conversion*

### Q9. Write a program to convert to binary. Find biggest power of two that is less than the n...

**Source:** `21_boolean.pptx` slide 3 (practice exercise, no answer options)

Write a program to convert to binary. Find biggest power of two that is less than the number, subtract it out, repeat until you reach 2^0

**Answer:** not recorded in the source materials

**Detail:** No solution in slide text or notes; likely live-coded in class.

**Extraction note:** On the slide '2^0' is 2 with a superscript 0; the text dump flattened it to '20'.

*Also touches: while-loops, number-conversion*

### Q10. Write a program to convert to binary. Divide by 2, take remainder, repeat until you rea...

**Source:** `21_boolean.pptx` slide 4 (practice exercise, no answer options)

Write a program to convert to binary. Divide by 2, take remainder, repeat until you reach 1 or 0

**Answer:** not recorded in the source materials

**Detail:** No solution in slide text or notes; likely live-coded in class.

**Extraction note:** Second of two conversion exercises; same task as slide 3 but using the divide-by-2 remainder method.

*Also touches: while-loops, number-conversion*

## Digital logic

### Q11. We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What w...

**Source:** `21_boolean.pptx` slide 15

We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What will give us the SUM (not the carry)?

```python
    1111
+  1011
----------
```

- **A.** Parity(a,b,c)
- **B.** not Parity(a,b,c)
- **C.** Parity(a,b)
- **D.** None of the above
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; the sum bit of a full adder is a XOR b XOR c, which is 1 exactly when an odd number of the three bits are 1 (parity).

**Code check:** confirmed by execution

**Extraction note:** The slide shows the binary addition 1111 + 1011 (carried over from slide 14) as context for the question.

*Also touches: binary-representation, full-adder, parity*

### Q12. We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What w...

**Source:** `21_boolean.pptx` slide 16

We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What will give us the carry-out?

```python
    1111
+  1011
----------
```

- **A.** Majority(a,b,c)
- **B.** not Majority(a,b,c)
- **C.** Majority(a,b)
- **D.** None of the above
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; the carry-out of a full adder is 1 exactly when at least two of the three bits are 1, i.e. Majority(a,b,c).

**Code check:** confirmed by execution

**Extraction note:** The slide shows the binary addition 1111 + 1011 (carried over from slide 14) as context for the question.

*Also touches: binary-representation, full-adder, majority-function*

### Q13. And and Not: [logic diagram] Two inputs, 0 and 1, feed an AND gate; the AND gate's outp...

**Source:** `22_digitalLogic.pptx` slide 5

And and Not: [logic diagram] Two inputs, 0 and 1, feed an AND gate; the AND gate's output feeds a NOT gate whose output is labeled "?". What is the value of the output "?"

- **A.** 0
- **B.** 1
- **C.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; 0 AND 1 = 0, then NOT 0 = 1.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Question is posed as a gate diagram with no question text on the slide; the diagram was reconstructed from shape positions in the pptx (AND-gate shape then NOT-gate triangle). Only the input/output labels 0, 1, and ? appear as text.

*Also touches: logic-gates, booleans-and-logic*

### Q14. We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What w...

**Source:** `22_digitalLogic.pptx` slide 12

We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What will give us the SUM (not the carry)?

```python
1111
+  1011
----------
```

- **A.** Parity(a,b,c)
- **B.** not Parity(a,b,c)
- **C.** Majority(a,b,c)
- **D.** not Majority(a,b,c)
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; the sum bit of a full adder is 1 exactly when an odd number of the three input bits are 1, which is Parity(a,b,c).

**Code check:** confirmed by execution

*Also touches: binary-addition, binary-representation, full-adder*

### Q15. We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What w...

**Source:** `22_digitalLogic.pptx` slide 13

We have 3 bits, 2 from our numbers and a carry bit.  Call these bits a,b and c.  What will give us the carry-out?

```python
1111
+  1011
----------
```

- **A.** Parity(a,b,c)
- **B.** not Parity(a,b,c)
- **C.** Majority(a,b,c)
- **D.** not Majority(a,b,c)
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say C; the carry-out of a full adder is 1 exactly when at least two of the three input bits are 1, which is Majority(a,b,c).

**Code check:** confirmed by execution

*Also touches: binary-addition, binary-representation, full-adder*

#### Practice exercises (Digital logic)

### Q16. Recall we defined Majority as 

**Source:** `22_digitalLogic.pptx` slide 9 (practice exercise, no answer options)

Recall we defined Majority as 
(A and (B or C)) or (B and C)
Draw a logic diagram for majority.

**Answer:** not recorded in the source materials

**Detail:** The expected answer is a drawn circuit diagram; no solution appears in the slide text or notes.

**Extraction note:** Answer is a diagram (worked on the board or a later slide), not recoverable from text.

*Also touches: logic-diagrams, booleans-and-logic*

### Q17. We defined Parity as 

**Source:** `22_digitalLogic.pptx` slide 10 (practice exercise, no answer options)

We defined Parity as 
A xor B xor C
Draw a logic diagram for Parity

**Answer:** not recorded in the source materials

**Detail:** The expected answer is a drawn circuit diagram; no solution appears in the slide text or notes.

**Extraction note:** Answer is a diagram, not recoverable from text; a stray "xor" text on the slide is likely a gate label in a partial diagram.

*Also touches: logic-diagrams, xor*
