# Peer Instruction Questions: Strings

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. What is the value of s after the following code runs?

**Source:** `11_strings.pptx` slide 3 - worked answer in `11_strings.pdf`

What is the value of s after the following code runs?

```python
s = "abc"
s = "d" * 3 + s
s = s + ""*3
s = s + "q"
```

- **A.** "abcddd   q"
- **B.** "abcddd" "" "" "q"
- **C.** "qdddabc"
- **D.** "dddabcq"
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D; PDF circles D and hand-traces the string as ddd, dddabc, dddabc (empty string times 3 adds nothing), dddabcq.

**Code check:** confirmed by execution

*Also touches: string-concatenation, string-repetition, variables-and-assignment*

### Q2. At the end of this code, y will be

**Source:** `11_strings.pptx` slide 5 - worked answer in `11_strings.pdf`

At the end of this code, y will be

```python
s = "Cats"
y = s[len(s)-1]
```

- **A.** C
- **B.** t
- **C.** s
- **D.** Nothing, this will cause an error
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF circles C with worked len(s)=4 so s[4-1]=s[3] is 's'.

**Code check:** confirmed by execution

*Also touches: indexing, len*

### Q3. will print

**Source:** `11_strings.pptx` slide 7 - worked answer in `11_strings.pdf`

will print

```python
s = "bats"
print(s[0:len(s)])
```

- **A.** ats
- **B.** bat
- **C.** bats
- **D.** This will throw an exception
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF circles C with len(s)=4 noted, so the slice 0:4 is the whole string.

**Code check:** confirmed by execution

*Also touches: slicing, len*

### Q4. This will print

**Source:** `11_strings.pptx` slide 9 - worked answer in `11_strings.pdf`

This will print

```python
s = "Vampires"
print(s[3:-1]
```

- **A.** mpire
- **B.** pires
- **C.** pire
- **D.** pir
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF circles the third option 'pire', with a hand-drawn index trace showing indices 3 through 6 (last character excluded by -1).

**Code check:** confirmed by execution

**Extraction note:** Slide's printed option letters misprint as A, B, A, B, C; normalized here to A-E in slide order. Code is transcribed verbatim and is missing the closing parenthesis on the print call.

*Also touches: slicing, negative-indexing*

### Q5. What does this code do?

**Source:** `11_strings.pptx` slide 12 - worked answer in `11_strings.pdf`

What does this code do?

```python
def mystery(s):
	new_s = ""
	for c in s:
		new_s = c + new_s
	return new_s
```

- **A.** Return a copy of s
- **B.** Return the reverse of s
- **C.** Return a string with only the last character of s
- **D.** Return a string with only the first character of s
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF circles B and hand-traces s='dog' building new_s as d, od, god.

**Code check:** confirmed by execution

*Also touches: for-loops, functions, string-building*

### Q6. We want a program that removes all spaces from strings.  Which is correct?

**Source:** `11_strings.pptx` slide 14 - worked answer in `11_strings.pdf`

We want a program that removes all spaces from strings.  Which is correct?

```python
A:
def space_remove(s):
	for c in s:
		if c == " ":
			c = ""

B:
def space_remove(s):
	new_s =""
	for c in s:
		if c != " ":
			new_s = new_s +c

C:
def space_remove(s):
	for i in range(len(s)):
		if s[i] == " ":
			s[i] = ""
```

- **A.** def space_remove(s):
	for c in s:
		if c == " ":
			c = ""
- **B.** def space_remove(s):
	new_s =""
	for c in s:
		if c != " ":
			new_s = new_s +c
- **C.** def space_remove(s):
	for i in range(len(s)):
		if s[i] == " ":
			s[i] = ""
- **D.** More than one of the above
- **E.** I don't know

**Answer:** B (from Dr. Taylor's speaker notes)

**Detail:** Notes say B; B builds a new string from non-space characters, A only rebinds the loop variable, and C attempts item assignment on an immutable string; the annotated PDF omits this slide so no handwriting verification was possible.

**Code check:** confirmed by execution - caveat: Option B is the correct approach, but as shown it lacks a `return new_s` line and so literally returns None - a missing-return truncation shared by all three options, not a flaw unique to B.

**Extraction note:** Annotated PDF (16 pages) does not include this slide; answer rests on speaker notes only.

*Also touches: for-loops, conditionals, immutability, string-building*

### Q7. We want a program that removes all spaces from strings.  Which is correct?

**Source:** `12_lists.pptx` slide 2 - worked answer in `12_lists.pdf`

We want a program that removes all spaces from strings.  Which is correct?

- **A.** def space_remove(s):
	for c in s:
		if c == " ":
			c = ""
- **B.** def space_remove(s):
	new_s =""
	for c in s:
		if c != " ":
			new_s = new_s +c
- **C.** def space_remove(s):
	for i in range(len(s)):
		if s[i] == " ":
			s[i] = ""
- **D.** More than one of the above
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B and the instructor circled B in the annotated PDF, marking A wrong and crossing out C; only B builds a new string, since strings are immutable.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** The annotated PDF shows an older variant of this slide with different C, D, and E options (its C uses slicing s = s[:i]+s[i+1:], its E is More than one of the above), but the circled answer B matches the pptx version and the notes.

*Also touches: string-immutability, for-loops, functions*

#### Practice exercises (Strings)

### Q8. Write the following function that returns the number of vowels in string s. Both upperc...

**Source:** `11_strings.pptx` slide 11 - worked answer in `11_strings.pdf` (practice exercise, no answer options)

Write the following function that returns the number of vowels in string s. Both uppercase and lowercase vowels should be counted. (The vowels are a, e, i, o, and u.)

```python
def num_vowels(s):
```

**Answer:** def num_vowels(s):
    count = 0
    for c in s:
        if c in "aeiouAEIOU":
            count = count + 1
    return count (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes or the annotated PDF; sample solution written by the extractor: loop over s counting characters that appear in 'aeiouAEIOU'.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: for-loops, functions, conditionals*
