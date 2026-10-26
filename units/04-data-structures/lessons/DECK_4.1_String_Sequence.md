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
Pairs. Each pair takes a "Before you type" card from the table, works
through its steps on the whiteboard, then types. A pair that is stuck
says which step of the card they're on. It's the card's first use:
hold one up and say the answers go on the whiteboard, not on the card.
While you walk the room, look for: the counter set to 0 above the
loop; the print lined up with for; capitals handled with .lower() or
both cases in the test string; a prompt that says what to type. Key
for the sentence report in the lesson plan.
-->

Pairs. Work through the "Before you type" card on your whiteboard,
then type.

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

## Before you type
<!-- pipeline: reveal -->
<!-- pipeline: notes
Pairs work the card on the whiteboard first. The pieces appear on
click, after pairs have tallied their sentence by hand.
-->

Write a short sentence on your whiteboard, like "I see a bee." Draw a
box around each character, spaces too. Go along the boxes one at a
time and keep a tally of what your option counts. What do you check at
each box, and what do you print at the end?

You have written every piece of this before:

- Asking the user is the text adventure: `input()` with a prompt that
  says what to type, and `.lower()` so capitals count.
- Letter hunt: the counter is the loop that counted the s's in
  "Mississippi," with the user's letter in place of `'s'`.
- Sentence report: `num_vowels` from Try it, with more counters in the
  same loop, one for each thing you report, and `len` for the
  characters.
- Gadsby check: the "Mississippi" counter looking for `'e'`, then an
  `if` and `else` after the loop, like a decision in the text
  adventure.

## Finished? Try the next step of your option
<!-- pipeline: notes
First-level ceilings, one per option. Keys in the lesson plan's
Extras. Letter hunt: a while loop that asks again until len(letter) is
1; on "Mississippi River" it turns down "ss" and a bare Enter, then
reports 4 for "S". Sentence report: consonants are letters minus
vowels; "Gadsby is a novel without the letter E" has 19 consonants and
is 38.7 percent vowels. Gadsby check: a for loop over 'aeiou';
"Rhythm and blues" uses a, e, and u, and never i or o.
-->

- Letter hunt: if the user types more than one character, or nothing,
  say so and ask again, the way the text adventure asked again when it
  didn't understand an answer.
- Sentence report: also count the consonants, and print what percent
  of the letters are vowels, to one decimal place.
- Gadsby check: check every vowel, not only e. For each of a, e, i, o,
  and u, print whether the sentence uses it.

## Still going?
<!-- pipeline: notes
Second-level ceilings; each needs an idea students haven't been shown.
Pair count: a variable that remembers the last character; "Mississippi"
has "ss" twice. The common bug is previous = c above the if, which
gives 4. Word count: a True or False variable that changes as the loop
runs; "  Gadsby   is a  novel" has 4 words, where spaces plus one gives
9. The common bug is never setting it to True, which gives 14. Vowel
table: a loop inside a loop; "The quick brown fox jumps over the lazy
dog" has a 1, e 3, i 1, o 4, u 2. The common bug is count = 0 above
the outer loop, so the counts run on: a 1, e 4, i 5, o 9, u 11. Keys
in the lesson plan's Extras.
-->

Each of these needs an idea you haven't been shown.

- Letter hunt: count a pair of letters the user types, like "ss" in
  "Mississippi," which has two. Hint: keep the character from the last
  pass in a variable; `previous + c` is the two characters that end
  here.
- Sentence report: count the words, even when the user types extra
  spaces between words or at the start. Hint: keep a `True` or `False`
  variable that says whether you are inside a word. A word starts at a
  character that isn't a space when that variable is `False`.
- Gadsby check: print how many times each vowel appears, one line per
  vowel, like `a 3`. Hint: a loop inside a loop. The outer loop goes
  through `'aeiou'`, and the inner loop counts that vowel in the
  sentence.

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
