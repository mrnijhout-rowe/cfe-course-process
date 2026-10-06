# Peer Instruction Questions: Lists

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. print(C) will result in:

**Source:** `12_lists.pptx` slide 8 - worked answer in `12_lists.pdf`

print(C) will result in:

```python
A = [2,3,5]
B = ["pirate"]
C = A + B
```

- **A.** [2,3,5]
- **B.** [2,3,5,"pirate"]
- **C.** ["2","3","5","pirate"]
- **D.** This will cause an error
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the option [2,3,5,"pirate"] is circled in the annotated PDF; + concatenates the two lists, keeping element types.

**Code check:** confirmed by execution

**Extraction note:** Options are unlabeled on the slide; letters A-E assigned by reading order. The PDF render's second column restarts its auto-numbering at A/B, but the circled option is unambiguously the second one overall.

*Also touches: list-concatenation, heterogeneous-lists*

### Q2. What will this output?

**Source:** `12_lists.pptx` slide 10 - worked answer in `12_lists.pdf`

What will this output?

```python
def inc(A,x):
	x = x + 1
	for i in range(len(A)):
			A[i] = A[i] + 1

A = [2,6,7]
x = 5
inc(A,x)
print(A,x,sep=" ")
```

- **A.** [2,6,7] 5
- **B.** [3,7,8] 6
- **C.** [3,7,8] 5
- **D.** [2,6,7] 6
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and C is circled in the PDF's clicker table; the list is mutated inside inc but reassigning the int parameter x does not affect the caller's x.

**Code check:** confirmed by execution

**Extraction note:** Options live in a PowerPoint table not captured by the text dump; recovered from the pptx. The dump shows a triple tab before A[i] = A[i] + 1, preserved verbatim.

*Also touches: functions, mutability, parameter-passing*

### Q3. What will this output?

**Source:** `12_lists.pptx` slide 12 - worked answer in `12_lists.pdf`

What will this output?

```python
A = [2,3,5]
B = A
B[0] = 100
C = B+A
print(C)
```

- **A.** [2,3,5,100,3,5]
- **B.** [100,3,5,100,3,5]
- **C.** [102,6,10]
- **D.** [2,3,5,2,3,5]
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Notes say B; B aliases A, so B[0] = 100 changes A to [100,3,5] and C = B+A is [100,3,5,100,3,5]. Tracing the code confirms this.

**Code check:** confirmed by execution

**Extraction note:** Options live in a PowerPoint table not captured by the text dump; recovered from the pptx. The annotated PDF (12 pages) is missing this slide, so no handwriting verification was possible.

*Also touches: aliasing, references, list-concatenation*

### Q4. At the end of this code, A will be

**Source:** `12_lists.pptx` slide 15 - worked answer in `12_lists.pdf`

At the end of this code, A will be

```python
A = [1,2,3]
B = A
C = []
for e in A:
	C = C + [e]
B[1] = "pirate"
C[2] = "scurvy"
```

- **A.** [1, 2, 3]
- **B.** [1, "pirate", 3]
- **C.** [1, "pirate", "scurvy"]
- **D.** ["pirate", "scurvy"]
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Notes say B; B aliases A so B[1] = "pirate" changes A, while C is an element-by-element copy so C[2] = "scurvy" does not. Tracing the code confirms this.

**Code check:** confirmed by execution

**Extraction note:** Options are unlabeled on the slide; letters A-E assigned by reading order. The annotated PDF is missing this slide, so no handwriting verification was possible.

*Also touches: aliasing, list-copying, mutability*

### Q5. At the end of this code, A will be

**Source:** `12_lists.pptx` slide 16 - worked answer in `12_lists.pdf`

At the end of this code, A will be

```python
A = [1,2,3]
A = A*3
```

- **A.** [1, 2, 3]
- **B.** [3, 6, 9]
- **C.** [1, 2, 3, 1, 2, 3, 1, 2, 3]
- **D.** [3,6,9,3,6,9,3,6,9]
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Notes say C; * on a list repeats it, so A*3 is the list concatenated with itself three times, not element-wise multiplication. Tracing the code confirms this.

**Code check:** confirmed by execution

**Extraction note:** Options are unlabeled on the slide; letters A-E assigned by reading order. The annotated PDF is missing this slide, so no handwriting verification was possible.

*Also touches: list-repetition, operators*

### Q6. What will this output?

**Source:** `13_morelists.pptx` slide 2 - worked answer in `13_morelists.pdf`

What will this output?

```python
A = [2,3,5]
B = A
B[0] = 100
C = B+A
print(C)
```

- **A.** [2,3,5,100,3,5]
- **B.** [100,3,5,100,3,5]
- **C.** [102,6,10]
- **D.** [2,3,5,2,3,5]
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state B and the PDF circles B; B = A aliases the list, so B[0] = 100 also changes A and C = B+A is [100,3,5,100,3,5].

**Code check:** confirmed by execution

*Also touches: aliasing, references, list-concatenation*

### Q7. At the end of this code, A will be

**Source:** `13_morelists.pptx` slide 5 - worked answer in `13_morelists.pdf`

At the end of this code, A will be

```python
A = [1,2,3]
B = A
C = []
for e in A:
	C = C + [e]
B[1] = "pirate"
C[2] = "scurvy"
```

- **A.** [1, 2, 3]
- **B.** [1, "pirate", 3]
- **C.** [1, "pirate", "scurvy"]
- **D.** ["pirate", "scurvy"]
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state B and the PDF circles B with a memory diagram; B aliases A so B[1] = "pirate" changes A, while C is an element-by-element copy so C[2] = "scurvy" does not.

**Code check:** confirmed by execution

*Also touches: aliasing, copying-lists, for-loops*

### Q8. At the end of this code, A will be

**Source:** `13_morelists.pptx` slide 6 - worked answer in `13_morelists.pdf`

At the end of this code, A will be

```python
A = [1,2,3]
A = A*3
```

- **A.** [1, 2, 3]
- **B.** [3, 6, 9]
- **C.** [1, 2, 3, 1, 2, 3, 1, 2, 3]
- **D.** [3,6,9,3,6,9,3,6,9]
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state C and the PDF circles C; list * int repeats the list, and the instructor also hand-wrote the element-wise alternative (for i in range(len(A)): A[i] = A[i]*3) as contrast.

**Code check:** confirmed by execution

*Also touches: list-repetition, operators*

### Q9. What will this output?

**Source:** `13_morelists.pptx` slide 7 - worked answer in `13_morelists.pdf`

What will this output?

```python
A = [5,10,15]
for i in range(0,len(A)):
	A[i] = A[i]+1
print("1: ",A, end=" ")

A = [5,10,15]
for e in A:
	e = e + 1
print("2: ",A)
```

- **A.** 1: [5,10,15] 2: [5,10,15]
- **B.** 1: [6,11,16] 2: [6,11,16]
- **C.** 1: [5,10,15] 2: [6,11,16]
- **D.** 1: [6,11,16] 2: [5,10,15]
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state D; no letter is circled on the PDF page but the handwriting shows [6,11,16] for the first loop and the slide 8 memory trace shows A unchanged by the second loop, since assigning to the loop variable e does not mutate the list.

**Code check:** confirmed by execution

*Also touches: for-loops, mutation, index-vs-element-loop*

### Q10. This will print

**Source:** `13_morelists.pptx` slide 9 - worked answer in `13_morelists.pdf`

This will print

```python
A = [2,3,5]
for e in A[1:]:
	print(e, end=" ")
```

- **A.** 2,3,5
- **B.** 2,3
- **C.** 3,5
- **D.** This will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state C and the PDF circles C; A[1:] is the slice [3, 5].

**Code check:** confirmed by execution

*Also touches: slicing, for-loops*

### Q11. This will print

**Source:** `13_morelists.pptx` slide 10 - worked answer in `13_morelists.pdf`

This will print

```python
B = [[1,2,3][5,10,20]]
print(B[1])
```

- **A.** 2
- **B.** [1,2,3]
- **C.** [5,10,20]
- **D.** This will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state C and the PDF circles C, treating the code as the nested list [[1,2,3],[5,10,20]] whose B[1] is [5,10,20]; notes add a follow-up: what will print(B[1][0]) do?

**Code check:** confirmed by execution - caveat: The slide code is missing a comma between the two inner lists, so run exactly as printed it raises a TypeError (option D); answer C is correct only for the intended code [[1,2,3],[5,10,20]] with the comma inserted, as the instructor's PDF annotation does.

**Extraction note:** Slide code is missing the comma between the inner lists (transcribed verbatim); run literally it would raise TypeError, but the instructor's PDF annotation inserts the comma and the intended code [[1,2,3],[5,10,20]] gives C.

*Also touches: nested-lists, indexing*

### Q12. This will print

**Source:** `13_morelists.pptx` slide 11 - worked answer in `13_morelists.pdf`

This will print

```python
def nicePrint(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j],end=" ")
        print()

A = [[2,5,10],[1,17,0]]
nicePrint(A)
```

- **A.** 2 5 10
1 17 0
- **B.** 2 1
17 5
0 10
- **C.** 2 5
10 1
17 0
- **D.** This will cause an error
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes state A and the PDF circles A with a full i/j trace; nicePrint prints each row of the 2D list on its own line.

**Code check:** confirmed by execution

**Extraction note:** The PDF-era version of this slide called colPrint(A), hand-corrected in class to nicePrint; the current pptx reads nicePrint(A), which is what is transcribed here.

*Also touches: nested-lists, nested-loops, functions*

### Q13. This will print

**Source:** `13_morelists.pptx` slide 12 - worked answer in `13_morelists.pdf`

This will print

```python
def colPrint(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[j][i],end=" ")
        print()

A = [[2,5,10],[1,17,0]]
colPrint(A)
```

- **A.** 2 5 10
1 17 0
- **B.** 2 1
17 5
0 10
- **C.** 2 5
10 1
17 0
- **D.** This will cause an error
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Notes state D; this slide is not in the annotated PDF, but tracing confirms it: colPrint indexes A[j] with j up to 2 while A has only 2 rows, so A[2] raises IndexError.

**Code check:** confirmed by execution

**Extraction note:** Not present in the annotated PDF (PDF skips slides 12-13).

*Also touches: nested-lists, nested-loops, index-error*

### Q14. This will print

**Source:** `13_morelists.pptx` slide 13 - worked answer in `13_morelists.pdf`

This will print

```python
B = [[0]*5]*3
B[1][3] = 7
nicePrint(B)
```

- **A.** 0 0 0 7 0
0 0 0 0 0
0 0 0 0 0
- **B.** 0 0 0 0 0
0 0 0 7 0
0 0 0 0 0
- **C.** 0 0 0 7 0
0 0 0 7 0
0 0 0 7 0
- **D.** This will cause an error
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Notes state C (with "draw memory"); this slide is not in the annotated PDF, but [[0]*5]*3 makes three references to the same inner row, so setting B[1][3] = 7 shows in every row.

**Code check:** confirmed by execution

**Extraction note:** Not present in the annotated PDF (PDF skips slides 12-13). Uses nicePrint defined on slide 11.

*Also touches: aliasing, nested-lists, list-repetition*

### Q15. Is [5,"squid",7] a valid list? How about [4]?

**Source:** `14_Review.pptx` slide 12 - worked answer in `14_Review.pdf`

Is [5,"squid",7] a valid list? How about [4]?

- **A.** Both are
- **B.** Both aren't
- **C.** [4] is, but not [5,"squid", 7]
- **D.** [5,"squid", 7] is, but not [4]
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A and A is circled in the annotated PDF; lists may mix types and may have a single element.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: expressions-and-types*

### Q16. What will the output of this code be?

**Source:** `25_review.pptx` slide 4 - worked answer in `25_review.pdf`

What will the output of this code be?

```python
A = [1,2,3]
B = A + [4]
C = A.append(5)
print(A, B, C)
```

- **A.** [1,2,3] [1,2,3,4] [1 2 3 5]
- **B.** [1 2 3 4 5] [1 2 3 4 5] [1 2 3 4 5]
- **C.** [1 2 3 5] [1 2 3 4] [1 2 3 5]
- **D.** [1 2 3 5] [1 2 3 4] None
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say D; + makes a new list while append mutates A in place and returns None; PDF has no handwriting.

**Code check:** confirmed by execution

**Extraction note:** Option list element separators (commas vs spaces) transcribed exactly as on the slide.

*Also touches: mutability, append-returns-none, list-concatenation*

### Q17. Adding a new bird sighting

**Source:** `30_DictionariesSets.pptx` slide 5 - worked answer in `30_dictionaries.pdf`

Adding a new bird sighting

```python
def new_sighting(birds, counts, new_bird):
    if new_bird not in birds:
        birds.append(new_bird)
        missing code
    ind = birds.index(new_bird)
    counts[ind] = counts[ind] + 1
```

- **A.** counts.append(0)
- **B.** counts.append(1)
- **C.** counts.append(new_bird)
- **D.** No code necessary
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say A and the PDF shows A circled; appending 0 keeps counts parallel with birds so the increment line then sets the new bird's count to 1.

**Code check:** confirmed by execution

**Extraction note:** Question asks which line replaces the italicized 'missing code' placeholder inside the if block.

*Also touches: parallel-lists, dictionaries-motivation, append, index*

#### Practice exercises (Lists)

### Q18. Write a Python function called min(A) which takes in a list A, and returns the smallest...

**Source:** `25_review.pptx` slide 9 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Write a Python function called min(A) which takes in a list A, and returns the smallest element in that list. (Do not use the built in min list function.) You can not assume the list elements are any particular type, but you can assume that <, <=, ==, ! =, =>, > work.

**Answer:** def min(A):
    smallest = A[0]
    for x in A:
        if x < smallest:
            smallest = x
    return smallest (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (track the smallest seen while looping over the list).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Operator list transcribed verbatim from the slide, including its nonstandard '! =' and '=>' spellings.

*Also touches: for-loops, functions, accumulator-pattern*

### Q19. Write a Python function called diagFlip(L) that takes in a 2-dimensional n x n list L a...

**Source:** `35_review.pptx` slide 15 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Write a Python function called diagFlip(L) that takes in a 2-dimensional n x n list L and flips it around the diagonal. For example, if the list L was
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
then n = 4 and the function should update the list to
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16

**Answer:** not recorded in the source materials

**Extraction note:** Slide text uses a multiplication sign in 'n x n'; normalized to ASCII 'x'.

*Also touches: nested-loops, 2d-lists*

### Q20. Write a Python function called diagFlip(L) that takes in a 2-dimensional n x n list L a...

**Source:** `36_review.pptx` slide 13 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Write a Python function called diagFlip(L) that takes in a 2-dimensional n x n list L and flips it around the diagonal. For example, if the list L was 
1  2  3  4 
5  6  7  8 
9 10 11 12 
13 14 15 16 
then n = 4 and the function should update the list to 
1 5 9 13 
2 6 10 14 
3 7 11 15 
4 8 12 16

**Answer:** In-place transpose with nested loops over the upper triangle: for i in range(len(L)): for j in range(i + 1, len(L)): L[i][j], L[j][i] = L[j][i], L[i][j]. (inferred during extraction - not marked in the source materials)

**Detail:** Slide omitted from the annotated PDF and no notes; standard in-place transpose solution supplied by the extractor.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: nested-loops, 2d-lists, in-place-mutation*
