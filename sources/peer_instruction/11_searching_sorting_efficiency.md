# Peer Instruction Questions: Searching, Sorting, and Efficiency

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Searching

### Q1. We've found the middle element, and created variables newstart and newend for our new e...

**Source:** `23_searching.pptx` slide 8

We've found the middle element, and created variables newstart and newend for our new ending and starting points.  Now we should set:

- **A.** newstart = start, newend = end
- **B.** start = newstart, end = newend
- **C.** list = list[newstart:newend]
- **D.** More than one of these would work
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'B' - update start and end to the newly computed bounds before the next loop iteration.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options carried no letter labels on the slide; A-E assigned in top-to-bottom order. Question refers to the find() skeleton shown on slide 7.

*Also touches: binary-search, variables-and-assignment, while-loops*

### Q2. Assume we're looking at an element halfway between indices start and end.  If the middl...

**Source:** `23_searching.pptx` slide 9

Assume we're looking at an element halfway between indices start and end.  If the middle item is smaller than our target, we should look between indices

- **A.** (end-start)//2, end
- **B.** (start+end)//2 + 1, end
- **C.** start, (start+end)//2 + 1
- **D.** start, (end-start)//2
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'B' - middle smaller than target means search the upper half, from one past the midpoint (start+end)//2 + 1 up to end; slide 10 walks it through with Find 55.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options carried no letter labels on the slide; A-E assigned in top-to-bottom order.

*Also touches: binary-search, lists, integer-division*

### Q3. We know the item is not in the list when

**Source:** `23_searching.pptx` slide 12

We know the item is not in the list when

- **A.** end == 0
- **B.** middle == start
- **C.** middle == end
- **D.** end == start
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say 'D' - when the search window collapses to end == start the target is absent; slide 13 adds this as the return -1 check.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options carried no letter labels on the slide; A-E assigned in top-to-bottom order. Refers to the find() code shown on slide 11.

*Also touches: binary-search, while-loops, booleans-and-logic*

#### Practice exercises (Searching)

### Q4. Implement a function that takes a list and an element as parameters, and returns either...

**Source:** `23_searching.pptx` slide 3 (practice exercise, no answer options)

Implement a function that takes a list and an element as parameters, and returns either the element's index in the list, or -1 if the element does not appear in the list

**Answer:** not recorded in the source materials

**Detail:** No solution for this linear-search version appears in the slides or notes; the deck moves on to the sorted-list (binary search) case.

**Extraction note:** Slide title is 'Sorting' but the task is linear search; context from slide 2 is the unsorted list A = [17,3,100,19,25,255,-3,...].

*Also touches: linear-search, lists, functions*

### Q5. Write pseudo code to search the list

**Source:** `23_searching.pptx` slide 6 (practice exercise, no answer options)

Write pseudo code to search the list

**Answer:** def find(list, target):
    start = 0
    end = len(list)-1
    while (True):
        middle = list[(start+end)//2]
        if (middle > target):
            end = (start+end)//2
        elif (middle < target):
            start = (start+end)//2 + 1
        elif (middle == target):
            return (start+end)//2
        if end == start:
            return -1 (inferred during extraction - not marked in the source materials)

**Detail:** Not in notes or a PDF; the completed binary search code shown on deck slides 11 and 13 is the intended solution (slide 13 has a stray extra open parenthesis in list[(start+end)//2], corrected here).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** One-line prompt; context is the sorted list halving demo on slide 5 (A = [2,4,6,8,10,11,17,24,34,55,85], target 97), i.e. write binary search.

*Also touches: binary-search, pseudocode, while-loops*

### Q6. Write pseudocode to do a binary search over a sorted list.

**Source:** `35_review.pptx` slide 10 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Write pseudocode to do a binary search over a sorted list.

**Answer:** not recorded in the source materials

*Also touches: lists*

### Q7. Write pseudocode to do a binary search over a sorted list.

**Source:** `36_review.pptx` slide 8 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Write pseudocode to do a binary search over a sorted list.

**Answer:** Handwritten sketch: def binSearch(L, e): m = len(L)//2; if e < L[m]: return binSearch(L[:m], e); if e > L[m]: return binSearch(L[m:], e); if e == L[m]: return m; base case noted at the side: if len(L) == 1 and e != L[m]: return -1. (from her handwritten in-class annotations (PDF))

**Detail:** Worked handwritten recursive-halving pseudocode on the annotated PDF page for this slide (PDF page 9).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: binary-search, recursion, pseudocode*

## Sorting

### Q8. Which of the following is true for selection sort?

**Source:** `27_sorting.pptx` slide 6 - worked answer in `27_sorting.pdf`

Which of the following is true for selection sort?

- **A.** Once a value is placed in the sorted part, it will never move again
- **B.** All values in the sorted part are always less than or equal to all values in the unsorted part
- **C.** Both of the above are true
- **D.** None of the above is true
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say C; no handwritten mark on the PDF page. Both invariants hold for selection sort: placed values never move, and every sorted value is <= every unsorted value.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: selection-sort, algorithm-invariants*

### Q9. Which is true of Insertion Sort?

**Source:** `27_sorting.pptx` slide 10 - worked answer in `27_sorting.pdf`

Which is true of Insertion Sort?

- **A.** Once a value is placed in the sorted part, it will never move again
- **B.** All values in the sorted part are always less than or equal to all values in the unsorted part
- **C.** Both of the above are true
- **D.** None of the above is true
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say D and D is circled on the annotated PDF; in insertion sort sorted values can shift when later elements are inserted, and the sorted part can hold values larger than unsorted ones.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: insertion-sort, algorithm-invariants*

### Q10. [10, 20, 30, 40, 16, 94, 8, 22]

**Source:** `27_sorting.pptx` slide 11 - worked answer in `27_sorting.pdf`

[10, 20, 30, 40, 16, 94, 8, 22]
The list above reflects the state of the list after 3 passes of insertion sort. What will be the list after the next (fourth) pass?

- **A.** [8, 20, 30, 40, 16, 94, 10, 22]
- **B.** [10, 16, 20, 30, 40, 94, 8, 22]
- **C.** [10, 16, 30, 40, 20, 94, 8, 22]
- **D.** [8, 10, 20, 30, 40, 16, 94, 22]
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B and B is circled on the annotated PDF; the fourth pass inserts 16 into the sorted prefix [10, 20, 30, 40], giving [10, 16, 20, 30, 40, 94, 8, 22].

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: insertion-sort, trace-execution, lists*

### Q11. Which of the following is true of bubble sort?

**Source:** `28_bubbleandmerge.pptx` slide 7 - worked answer in `28_moresorting.pdf`

Which of the following is true of bubble sort?

- **A.** Once a value is placed in the sorted part, it will never move again
- **B.** There is never a value in the sorted part that is smaller than some value in the unsorted part
- **C.** Both of the above are true
- **D.** None of the above is true

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and the PDF shows C circled.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: bubble-sort, loop-invariants*

### Q12. [5, 9, 0, 4, 6, 8, 2] What will be the list after one pass of bubble sort?

**Source:** `28_bubbleandmerge.pptx` slide 8 - worked answer in `28_moresorting.pdf`

[5, 9, 0, 4, 6, 8, 2] What will be the list after one pass of bubble sort?

- **A.** [5,0,9,6,4,2,8]
- **B.** [5,9,0,4,6,2,8]
- **C.** [5,0,9,4,6,8,2]
- **D.** [5,0,4,6,8,2,9]
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF shows D circled; the 9 bubbles all the way to the right end in one pass.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: bubble-sort, algorithm-tracing*

### Q13. Which will perform best on a sorted list?

**Source:** `29_mergesort.pptx` slide 5 - worked answer in `30_mergesort.pdf`

Which will perform best on a sorted list?

```python
def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		j = i
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swapped = True
```

- **A.** Bubble sort
- **B.** Insertion sort
- **C.** Selection sort
- **D.** A and B
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say D and the annotated PDF (page 6 of the variant deck) circles D, with handwritten work showing bubble and insertion sort run in O(n) on an already sorted list while selection sort stays n^2.

**Code check:** confirmed by execution

*Also touches: runtime-and-big-o, best-case-analysis*

### Q14. We have two sorted lists, B and C.  What is the MOST EFFICIENT way to combine them into...

**Source:** `29_mergesort.pptx` slide 6 - worked answer in `30_mergesort.pdf`

We have two sorted lists, B and C.  What is the MOST EFFICIENT way to combine them into one sorted list?

- **A.** Add C to the end of B, Bubblesort the new list
- **B.** Insertion sort, treating B as the sorted part and C as the unsorted part
- **C.** Create a new list, insert the smallest element from either list in the new list until you have inserted all the elements
- **D.** Something else
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C and the annotated PDF (page 7 of the variant deck) circles C, annotating A and B as roughly n^2 and C as n.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: runtime-and-big-o, merge, lists*

### Q15. Which has the best big O run time?

**Source:** `35_review.pptx` slide 7 - worked answer in `35_review.pdf`

Which has the best big O run time?

- **A.** Selection Sort
- **B.** Insertion Sort
- **C.** Bubble Sort
- **D.** They are all the same
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF circles D; handwritten annotations sketch the nested-loop structure and note mergesort is O(n log n) by contrast.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: runtime-and-big-o*

### Q16. Which will perform better on a mostly sorted list?

**Source:** `35_review.pptx` slide 8 - worked answer in `35_review.pdf`

Which will perform better on a mostly sorted list?

- **A.** Selection Sort
- **B.** Insertion Sort
- **C.** They will perform the same
- **D.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; this slide is absent from the annotated PDF so no handwritten confirmation exists.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Not present in the annotated PDF (PDF omits slides 8-15).

*Also touches: runtime-and-big-o, best-worst-case*

### Q17. Which will perform better on a mostly sorted list?

**Source:** `36_review.pptx` slide 7 - worked answer in `36_review.pdf`

Which will perform better on a mostly sorted list?

- **A.** Selection Sort
- **B.** Insertion Sort
- **C.** They will perform the same
- **D.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state B; the annotated PDF page for this slide (PDF page 8) has no handwriting. Insertion sort's inner while loop exits almost immediately on a nearly sorted list, giving close to linear time, while selection sort always scans the full remainder.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: runtime-and-big-o, insertion-sort, selection-sort*

#### Practice exercises (Sorting)

### Q18. Write Code for Selection Sort

**Source:** `27_sorting.pptx` slide 7 - worked answer in `27_sorting.pdf` (practice exercise, no answer options)

Write Code for Selection Sort

**Answer:** not recorded in the source materials

**Extraction note:** Title-only live-coding slide; the slide body is blank and no solution code appears in notes or the annotated PDF.

*Also touches: selection-sort, lists, nested-loops*

### Q19. Write Code for Insertion Sort

**Source:** `27_sorting.pptx` slide 13 - worked answer in `27_sorting.pdf` (practice exercise, no answer options)

Write Code for Insertion Sort

**Answer:** not recorded in the source materials

**Extraction note:** Title-only live-coding slide; the annotated PDF shows only the process note 'write shift code' (write the element-shifting code first), no full solution.

*Also touches: insertion-sort, lists, nested-loops*

### Q20. Write Code for Bubble Sort

**Source:** `28_bubbleandmerge.pptx` slide 9 - worked answer in `28_moresorting.pdf` (practice exercise, no answer options)

Write Code for Bubble Sort

**Answer:** not recorded in the source materials

**Extraction note:** Bare title slide used for live coding; the algorithm description is on slide 5 and the resulting code appears on slides 11-13; the PDF page for this slide has no written solution.

*Also touches: bubble-sort, while-loops, code-writing*

### Q21. Write Code for Merge

**Source:** `29_mergesort.pptx` slide 7 - worked answer in `30_mergesort.pdf` (practice exercise, no answer options)

Write Code for Merge

**Answer:** not recorded in the source materials

**Detail:** No solution on the slide or in notes; the annotated PDF only adds the handwritten clarification 'sorted lists' (merge takes two sorted lists), with the code presumably developed live elsewhere.

**Extraction note:** Slide contains only the title prompt; the task (following slide 6) is to write the merge function that combines two sorted lists into one sorted list.

*Also touches: lists, while-loops, merge*

### Q22. Write Code for Mergesort

**Source:** `29_mergesort.pptx` slide 10 - worked answer in `30_mergesort.pdf` (practice exercise, no answer options)

Write Code for Mergesort

**Answer:** not recorded in the source materials

**Detail:** No solution on the slide, in notes, or in the annotated PDF (its matching page 11 is unannotated); code was developed live.

**Extraction note:** Slide contains only the title prompt; context (slides 8-9) is the recursive split-then-merge algorithm, using the merge function from slide 7.

*Also touches: recursion, mergesort, lists*

## Runtime and Big O

### Q23. Is This Function Linear Time?

**Source:** `26_MeasuringProgramTime.pptx` slide 8 - worked answer in `26_MeasuringProgramTime.pdf`

Is This Function Linear Time?

```python
def mystery(n):
	total = 0
	for i in range(n):
		total += 1
	for i in range(n):
		total += 1
	return total
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; two sequential loops over n do 2n steps, which is still linear. PDF page 8 has no handwritten annotation.

**Code check:** confirmed by execution

*Also touches: for-loops, linear-time*

### Q24. This algorithm is:

**Source:** `26_MeasuringProgramTime.pptx` slide 11 - worked answer in `26_MeasuringProgramTime.pdf`

This algorithm is:

```python
def mystery(n):
	total = 0
	for i in range(n):
		for j in range(10000):
			for k in range(50):
				total += 1
	return total
```

- **A.** Linear (n)
- **B.** Quadratic (n^2)
- **C.** Cubic (n^3)
- **D.** Something else
- **E.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; the inner loop bounds (10000 and 50) are constants, so the work is a constant times n. PDF page 11 has no handwritten annotation.

**Code check:** confirmed by execution

*Also touches: nested-loops, constant-factors*

### Q25. This algorithm is:

**Source:** `26_MeasuringProgramTime.pptx` slide 12 - worked answer in `26_MeasuringProgramTime.pdf`

This algorithm is:

```python
def mystery(n):
	total = 0
	for i in range(n):
		for j in range(n):
			for k in range(50):
				total += 1
	return total
```

- **A.** Linear (n)
- **B.** Quadratic (n^2)
- **C.** Cubic (n^3)
- **D.** Something else
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; two loops over n with a constant-bound inner loop give 50 * n^2 steps, quadratic. PDF page 12 has no handwritten annotation.

**Code check:** confirmed by execution

*Also touches: nested-loops, constant-factors*

### Q26. This algorithm is:

**Source:** `26_MeasuringProgramTime.pptx` slide 13 - worked answer in `26_MeasuringProgramTime.pdf`

This algorithm is:

```python
def f(n):
	sum = 0
	while n > 0:
		sum = sum + n ** 2
		n = n // 2
	return sum
```

- **A.** Better than linear
- **B.** Linear (n)
- **C.** Quadratic (n^2)
- **D.** Worse than quadratic
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say A; PDF page 13 carries a worked trace (N=4: 4,2,1,0; N=8: 8,4,2,1,0; N=16: 16,8,4,2,1,0; log n) present only in the PDF, showing n halves each iteration, so O(log n), better than linear.

**Code check:** confirmed by execution

*Also touches: while-loops, logarithmic-time*

### Q27. Your coworker tells you he's found a way to change your algorithm so it does HALF as mu...

**Source:** `26_MeasuringProgramTime.pptx` slide 15 - worked answer in `26_MeasuringProgramTime.pdf`

Your coworker tells you he's found a way to change your algorithm so it does HALF as much work. Knowing that the algorithm is currently O(n^2), you say:

- **A.** That's great. This reduces our runtime to O(n) so it will take less time to run.
- **B.** That's great. Our runtime stays the same, but it will finish in around half the time.
- **C.** That doesn't do anything; our runtime stays the same, so it takes the same amount of time to run.
- **D.** That doesn't do anything; it does reduce our runtime to O(n) but that doesn't mean it runs faster.

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; halving the work changes only the constant factor, so the big-O class stays O(n^2) but the wall-clock time roughly halves. PDF page 15 has no handwritten annotation.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Missed by the candidate heuristic; only four options and no I-don't-know choice.

*Also touches: constant-factors, conceptual*

### Q28. The problem size is len(s). This algorithm is:

**Source:** `26_MeasuringProgramTime.pptx` slide 16 - worked answer in `26_MeasuringProgramTime.pdf`

The problem size is len(s). This algorithm is:

```python
def f(s):
	num = 0
	for c1 in s:
		for c2 in s:
			if c1 == c2:
				num = num + 1
	return num
```

- **A.** Better than linear
- **B.** Linear (n)
- **C.** Quadratic (n^2)
- **D.** Worse than quadratic
- **E.** I don't know

**Answer:** C (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say C; two nested loops each over all of s give len(s)^2 comparisons, quadratic. PDF page 16 has no handwritten annotation.

**Code check:** confirmed by execution

*Also touches: nested-loops, strings*

### Q29. The problem size is len(s). This algorithm is:

**Source:** `26_MeasuringProgramTime.pptx` slide 17 - worked answer in `26_MeasuringProgramTime.pdf`

The problem size is len(s). This algorithm is:

```python
def f(s):
	num = 0

	for c1 in s:
		s2 = s
		while len(s2) > 0:
			s2 = s2[:len(s2)//2]
```

**Answer:** O(n log n) (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes record the letter C (likely stale, matching slide 16); the slide's own reveal text box works out the answer as O(n log n) (outer for loop O(n) times halving while loop O(log n)).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** No lettered options appear on the slide (verified in the pptx); likely posed aloud, possibly reusing the previous slide's option list, but O(n log n) matches none of those letters exactly, so the notes letter C cannot be mapped to a visible option; the substantive answer O(n log n) is recorded instead. PDF page 17 shows the same reveal box and no handwriting.

*Also touches: while-loops, for-loops, logarithmic-time, strings*

### Q30. What is the Big O of this code?

**Source:** `28_bubbleandmerge.pptx` slide 10 - worked answer in `28_moresorting.pdf`

What is the Big O of this code?

```python
def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp
```

- **A.** O(n)
- **B.** O(n2)
- **C.** Worse than O(n2)
- **D.** Between O(n) and O(n2)
- **E.** I don't knpw

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; O(n2) means O(n squared) with the superscript lost in text extraction, and the nested loops give quadratic time; this slide is not in the annotated PDF.

**Code check:** confirmed by execution

**Extraction note:** Slide typos preserved verbatim: 'O(n2)' is O(n^2) with superscript formatting lost, and option E reads 'I don't knpw' on the slide.

*Also touches: sorting, selection-sort, nested-loops*

### Q31. Do all these sorts have the same Big O?

**Source:** `28_bubbleandmerge.pptx` slide 11 - worked answer in `28_moresorting.pdf`

Do all these sorts have the same Big O?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swap = True
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** A (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say A; all three sorts are O(n^2); this slide is not in the annotated PDF.

**Code check:** confirmed by execution

**Extraction note:** Slide code transcribed verbatim including bugs from the live-coding session (insertionSort never initializes j; bubbleSort assigns L[i+1] = L[i] after overwriting and sets swap instead of swapped); en dash in 'j = j - 1' normalized to a hyphen.

*Also touches: sorting, insertion-sort, selection-sort, bubble-sort*

### Q32. Will they have the same execution time on every list?

**Source:** `28_bubbleandmerge.pptx` slide 12 - worked answer in `28_moresorting.pdf`

Will they have the same execution time on every list?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swap = True
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; insertion and bubble sort exit early on already-sorted input while selection sort always does the full scan; this slide is not in the annotated PDF.

**Code check:** confirmed by execution

**Extraction note:** Same verbatim code blocks (with the same live-coding bugs) as slide 11; en dash in code normalized to a hyphen.

*Also touches: sorting, best-case-vs-worst-case*

### Q33. Which will perform best on a sorted list?

**Source:** `28_bubbleandmerge.pptx` slide 13 - worked answer in `28_moresorting.pdf`

Which will perform best on a sorted list?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swap = True
```

- **A.** Bubble sort
- **B.** Insertion sort
- **C.** Selection sort
- **D.** A and B
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say D; bubble sort with the swapped flag and insertion sort both finish in linear time on a sorted list; this slide is not in the annotated PDF.

**Code check:** confirmed by execution

**Extraction note:** Same verbatim code blocks (with the same live-coding bugs) as slides 11-12; en dash in code normalized to a hyphen.

*Also touches: sorting, best-case-behavior*

### Q34. What is the Big O run time?

**Source:** `29_mergesort.pptx` slide 2 - worked answer in `30_mergesort.pdf`

What is the Big O run time?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		j = i
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e
```

- **A.** n
- **B.** n2
- **C.** n3
- **D.** Between n and n2
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes say B; insertion sort is O(n^2) in the worst case.

**Code check:** confirmed by execution

**Extraction note:** Options B, C, and D use superscripts on the slide (n^2, n^3) that the text extraction flattened to n2/n3. The annotated PDF is a later deck variant that omits this slide, so no handwritten verification was possible.

*Also touches: sorting, insertion-sort*

### Q35. Do all these sorts have the same Big O run time?

**Source:** `29_mergesort.pptx` slide 3 - worked answer in `30_mergesort.pdf`

Do all these sorts have the same Big O run time?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		j = i
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swapped = True
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say A and the annotated PDF (page 4 of the variant deck) circles Yes, with O(n^2) worked out in the margins for all three sorts.

**Code check:** confirmed by execution

**Extraction note:** Slide shows the three sorts in separate code boxes (selectionSort left, insertionSort and bubbleSort right); concatenated here in dump order.

*Also touches: sorting*

### Q36. Will they have the same execution time on every list?

**Source:** `29_mergesort.pptx` slide 4 - worked answer in `30_mergesort.pdf`

Will they have the same execution time on every list?

```python
def insertionSort(L):
	for i in range(len(L)):
		e = L[i]
		j = i
		while (j > 0 and L[j-1] > e):
			L[j] = L[j-1]
			j = j - 1
		L[j] = e

def selectionSort(L):
	for i in range(len(L)):
		min_index = i
		for j in range (i,len(L)):
			if L[j] < L[min_index]:
				min_index = j
	temp = L[i]
	L[i] = L[min_index]
	L[min_index]  = temp

def bubbleSort(L):
	swapped = True
	while (swapped):
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = L[i]
				swapped = True
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B and the annotated PDF (page 5 of the variant deck) circles No; same Big O does not mean same actual execution time on every input.

**Code check:** confirmed by execution

*Also touches: sorting, best-vs-worst-case*

### Q37. What is the Big O run time?

**Source:** `35_review.pptx` slide 6 - worked answer in `35_review.pdf`

What is the Big O run time?

```python
def s(L) :
	x=0
	for i in range(len(L)) :
		for j in range(50) :
			L[i] = L[i] + j
	for i in range(len(L)) :
		print(L[i])
```

- **A.** O(1)
- **B.** O(n)
- **C.** O(n^2)
- **D.** O(n^3)
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF circles B, with annotations marking the inner range(50) loop as O(1) constant, so both outer loops are O(n).

**Code check:** confirmed by execution

**Extraction note:** Options C and D use superscripts on the slide (O(n squared), O(n cubed)); transcribed here with caret notation.

*Also touches: nested-loops*
