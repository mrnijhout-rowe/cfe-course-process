---
title: "Lesson 4.1: A string is a sequence"
subtitle: "Unit 4: Data structures"
---

## Today you will be able to

- write a `for` loop that visits every character of a string
- count the characters that pass a test, with a counter that starts at
  0 and grows with `+=`
- use `len` to measure a string and `in` to test whether a piece of
  text is inside it
- predict what a loop over a string prints before running it

## Plickers cards out, please
<!-- pipeline: layout center -->
<!-- pipeline: notes
Three questions in Plickers, in this order. For each: vote, argue
with a partner, revote, then reveal by running the code in Thonny.
1. A counting loop over 'abcab' with "if ch in 'ab'". Answer C, 4.
2. len('banana'), 'nan' in it, 'ab' in it. Answer D: 6 True False.
3. Cynthia Taylor's mystery(s), which returns the reverse. Answer B.
   Reveal on 'dog', or step through it in Python Tutor.
-->

Find your card. The question is coming up on the Plickers screen.

## The comparison table
<!-- pipeline: notes
Students copy the whole frame, all four columns, into their journals.
Say that the empty columns are for things the unit has not taught yet:
List in 4.5, Dictionary in 4.9, Tuple in 4.12. A sideways page gives
the four columns room. The next slide fills in the two String cells
for today.
-->

Copy this whole frame into your journal, all four columns. Give it a
full page, turned sideways.

Today starts the String column. The other three fill in later in the
unit.

| | String | List | Dictionary | Tuple |
|---|---|---|---|---|
| How you write one | | | | |
| How you reach one element | | | | |
| Has an order | | | | |
| Can be changed in place | | | | |
| `len`, `in`, `for` | | | | |

---
<!-- pipeline: notes
Two cells today, both in the String column. "How you write one"
first, then the last row after the len and in demo. The other three
String rows wait for lessons 4.3 and 4.4. The List, Dictionary, and
Tuple columns stay empty until 4.5, 4.9, and 4.12.
-->

Two cells today.

| | String | List | Dictionary | Tuple |
|---|---|---|---|---|
| How you write one | `'abc'` | | | |
| How you reach one element | | | | |
| Has an order | | | | |
| Can be changed in place | | | | |
| `len`, `in`, `for` | all three; `in` finds a piece of the string; `for` gives each character | | | |

## Try it: count the vowels
<!-- pipeline: reveal -->
<!-- pipeline: notes
Individual, in Thonny, about 10 minutes. Click to show each stretch
goal as pairs finish. Keys for the stretch goals are in the lesson
plan's Extras.
-->

> Write a function `num_vowels(s)` that returns the number of vowels
> in the string `s`. Count capital vowels too. The vowels are a, e, i,
> o, and u. Test it: `num_vowels('Gadsby')` should give 1, and
> `num_vowels('EDUCATION')` should give 5.

### Finished? Try one of these

- `count_letter(word, letter)`: how many times one chosen letter appears
- count the spaces in a sentence
- count the digits in a string, using `'0123456789'`

## One way to write it
<!-- pipeline: notes
The counter starts at 0 before the loop. c is each character in
order. The return is lined up with for, so every character is checked
before the function answers.
-->

```python
def num_vowels(s):
    count = 0                     # the counter starts at 0, before the loop
    for c in s:                   # c is each character of s, in order
        if c in 'aeiouAEIOU':     # is this character one of the vowels?
            count += 1            # same as count = count + 1
    return count                  # after the loop: every character is checked

print(num_vowels('Gadsby'))
print(num_vowels('EDUCATION'))
print(num_vowels('rhythm'))
```

```text
1
5
0
```

## Mini-project: Letter counter
<!-- pipeline: notes
Pairs. Sketch the steps on the table whiteboard first, then type in
Thonny. While you walk the room, look for: the counter set to 0 above
the loop; the print lined up with for; capitals handled with .lower()
or both cases in the test string; a prompt that says what to type.
Sample solution for the sentence report is in the lesson plan.
-->

Pairs. Sketch the steps on your whiteboard before either of you types.

> Write a program that asks the user to type a sentence and then
> reports something about its characters. Pick one:
>
> - **Letter hunt.** Also ask for a letter. Print how many times that
>   letter appears, counting capitals too.
> - **Sentence report.** Print how many characters, letters, vowels,
>   and spaces the sentence has.
> - **Gadsby check.** Print how many e's the sentence has. If there
>   are none, print a message saying it could go in *Gadsby*.
>
> Your prompt should tell the user what to type.

## Quick check: how it works
<!-- pipeline: layout center -->

The next slide has a question with four choices, numbered 1 to 4.

Decide on your answer and keep it to yourself.

When you hear "show me," everyone holds up that many fingers at once.

## Quick check
<!-- pipeline: notes
Answer: 2, eight times. The space is a character too, so the loop
visits H, i, the space, t, h, e, r, e. len('Hi there') is 8 for the
same reason.
Choice 1 catches skipping the space. Choice 3 catches counting the
words. Choice 4 catches thinking c holds the whole string, so the
body runs once.
-->

How many times does the body of this loop run?

```python
for c in 'Hi there':
    print(c)
```

1. 7
2. 8
3. 2
4. 1

## Tonight
<!-- pipeline: notes
The Codio pages after Formative Assessment 1 use indexing, which is
lesson 4.3. Students skim the while loop example tonight and finish
the assignment after 4.3; the whole thing is due before lesson 4.4.
-->

- Read Think Python chapter 7, "Iteration and Search." Skip the
  "Doctest" section. Reading quiz next class.
- Codio U6.L4 String Iteration: Learning Objectives, Concept Overview,
  "Iteration - For Loop," and Formative Assessment 1.
