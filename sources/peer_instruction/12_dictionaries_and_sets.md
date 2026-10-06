# Peer Instruction Questions: Dictionaries and Sets

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. After this code, d will be

**Source:** `30_DictionariesSets.pptx` slide 8 - worked answer in `30_dictionaries.pdf`

After this code, d will be

```python
d = {"a":1,"b":2}
d["c"] = 3
d["b"] = 4
```

- **A.** {"a":1, "b":2, "c":3}
- **B.** {"a":1, "b":4, "c":3}
- **C.** {"a":1, "b":2, "b":4, "c":3}
- **D.** This will cause an error
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF shows B circled with the dict states worked in the margin; assigning to existing key "b" overwrites its value.

**Code check:** confirmed by execution

*Also touches: key-assignment, overwriting-values*

### Q2. What is d at the end of this code?

**Source:** `30_DictionariesSets.pptx` slide 10 - worked answer in `30_dictionaries.pdf`

What is d at the end of this code?

```python
d = {3:4}
d[5] = d.get(4, 8)
d[4] = d.get(3, 9)
```

- **A.** {3:4, 5:8, 4:9}
- **B.** {3:4, 5:8, 4:4}
- **C.** {3:4, 5:4, 4:3}
- **D.** Error caused by get
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF shows B circled with worked states {3:4, 5:8} then {3:4, 5:8, 4:4}; get(4, 8) returns the default 8 and get(3, 9) returns the existing value 4.

**Code check:** confirmed by execution

*Also touches: dict-get, default-values*

### Q3. After this code, alpha will be

**Source:** `30_DictionariesSets.pptx` slide 14 - worked answer in `30_dictionaries.pdf`

After this code, alpha will be

```python
alpha = {"a"}
alpha.add("b")
alpha.add("c")
alpha.add("d")
alpha.remove("b")
alpha.remove("c")
alpha.add("b")
alpha.add("d")
```

- **A.** {"b","d"}
- **B.** {"a","b","d"}
- **C.** {"a","b","c","d"}
- **D.** {"a","b","d","d"}
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF shows B circled with the set traced step by step to {a, b, d}; re-adding "d" to a set has no effect since sets hold no duplicates.

**Code check:** confirmed by execution

**Extraction note:** Two-column option layout on the slide (A-C left, D-E right); label pairing verified via python-pptx paragraph order and the PDF render.

*Also touches: sets, set-add-remove, no-duplicates*
