# Peer Instruction Questions: General and Miscellaneous

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

### Q1. How long will my line be in terms of width?

**Source:** `17_fractals.pptx` slide 10 - worked answer in `17_fractals.pdf`

How long will my line be in terms of width?

- **A.** 1/3 w
- **B.** 1/2 w
- **C.** 2/3 w
- **D.** w
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF (page 12) has C circled, with the canvas width w marked under the triangle image.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Refers to an image on the slide: a triangle drawn on a canvas of width w. Option B was a curly one-half glyph, normalized to 1/2.

*Also touches: fractals, geometry, graphics*

### Q2. How much will I rotate?

**Source:** `17_fractals.pptx` slide 13 - worked answer in `17_fractals.pdf`

How much will I rotate?

- **A.** 60, 60, 60
- **B.** 60, 30, 60
- **C.** 60, 240, 60
- **D.** 120, 240, 120
- **E.** I don't know

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Notes say D; the corresponding PDF page (15) has no handwritten annotation to confirm.

**Concept check:** DISCREPANCY - the notes say D (120, 240, 120), but the Koch bump turns are 60, then -120 (i.e. 240), then 60 - option C - under either rotation direction; D leaves a net 120-degree heading change and cannot close the bump. The deck's own slide-2 code uses signed pic.rotate(), and the annotated PDF has no circled answer to break the tie. VERIFY THE ANSWER BEFORE USING THIS QUESTION.

**Extraction note:** Refers to the rotations between segments when drawing the pointy bit of the Koch snowflake side (star image on slide); depends on the course graphics library's rotation convention.

*Also touches: fractals, geometry, graphics*
