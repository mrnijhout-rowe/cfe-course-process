# Peer Instruction Questions: Type Errors and Exceptions

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. This will print

**Source:** `10_typesexceptions.pptx` slide 12 - worked answer in `10_typesexceptions.pdf`

This will print

```python
try:
	x = 1/0
	print("Math is lame!")
except Exception as e:
	print("Algebraic!")
```

- **A.** "Math is lame"
- **B.** "Algebraic!"
- **C.** Nothing, this will cause an error
- **D.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says B and B is circled in the PDF, with 'error!' marked at x = 1/0 and an arrow showing control jumping to the except block.

**Code check:** confirmed by execution

**Extraction note:** Only four options (D is the 'I don't know' choice on this slide).

*Also touches: try-except, division-by-zero*
