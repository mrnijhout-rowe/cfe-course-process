# Peer Instruction Question Bank (Dr. Cynthia Taylor, CS1)

Multiple-choice Peer Instruction ("clicker") questions extracted from
Dr. Cynthia Taylor's CS 150 intro Python slide decks (Oberlin College,
via peerinstruction4cs.org). Her README grants blanket permission to use
and adapt these materials; the decks themselves carry a Creative Commons
BY-NC-SA 4.0 license. If any of these appear in materials shared beyond
class, credit "Cynthia Taylor, Oberlin College" and keep the license.

## Where these came from

- Originals: `~/Documents/projects/external_sources/peer_instruction_for_cs/`
  (IntroPython1-5 archives), each deck a .pptx with a matching .pdf of the same slides
  carrying her handwritten in-class work (answers circled, examples worked).
- Extraction: question text pulled from the .pptx files; answers taken from
  her speaker notes and cross-checked against the handwritten PDFs, then
  independently verified a second time. Each answer line names its evidence.
- Code is Python 3 as written on the slides (circa 2014); smart quotes were
  normalized to straight quotes and indentation reconstructed.

## What is (and is not) in here

- 222 questions across 14 topic files, categorized by
  what each question actually tests (review-day questions are filed under
  their real topic, not "review").
- "Practice exercises" sections hold slides that pose a problem without
  multiple-choice options (mostly from review days).
- Answers with runnable code were additionally tested against actual
  Python execution; each such question carries a "Code check" line, and
  [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md) summarizes the results
  (including the few places where literal execution disagrees with the
  recorded answer, usually because the slide code contains a deliberate
  or accidental typo).
- Every remaining recorded answer (conceptual clickers and answered
  practice exercises) was verified by an independent blind re-solve with
  the recorded answer withheld; those questions carry a "Concept check"
  line. Two caveats and two unresolved discrepancies (where the speaker
  notes conflict with analysis) are detailed in the report.
- The "I don't know" option is part of the Peer Instruction format and was
  kept where present.
- Not included: 6 survey/logistics polls (e.g.
  "have you programmed before?") and worked-solution slides that restate
  a question.

## Files

| File | Topics | Clicker | Exercises |
|---|---|---:|---:|
| [01_expressions_variables_types.md](01_expressions_variables_types.md) | Expressions, Variables, and Types | 13 | 0 |
| [02_loops.md](02_loops.md) | Loops (for, nested, while) | 27 | 4 |
| [03_conditionals_and_booleans.md](03_conditionals_and_booleans.md) | Conditionals and Boolean Logic | 18 | 1 |
| [04_functions.md](04_functions.md) | Functions | 12 | 3 |
| [05_types_and_exceptions.md](05_types_and_exceptions.md) | Type Errors and Exceptions | 1 | 0 |
| [06_strings.md](06_strings.md) | Strings | 7 | 1 |
| [07_lists.md](07_lists.md) | Lists | 17 | 3 |
| [08_recursion.md](08_recursion.md) | Recursion | 15 | 5 |
| [09_classes_objects_inheritance.md](09_classes_objects_inheritance.md) | Classes, Objects, and Inheritance | 13 | 9 |
| [10_binary_and_digital_logic.md](10_binary_and_digital_logic.md) | Binary and Digital Logic | 12 | 5 |
| [11_searching_sorting_efficiency.md](11_searching_sorting_efficiency.md) | Searching, Sorting, and Efficiency | 28 | 9 |
| [12_dictionaries_and_sets.md](12_dictionaries_and_sets.md) | Dictionaries and Sets | 3 | 0 |
| [13_processes_and_concurrency.md](13_processes_and_concurrency.md) | Processes and Concurrency | 9 | 5 |
| [14_general.md](14_general.md) | General and Miscellaneous | 2 | 0 |

`pi_questions.json` holds the same content in machine-readable form
(one record per question, with deck, slide, topic tags, answer, and answer
provenance) for downstream tooling.
