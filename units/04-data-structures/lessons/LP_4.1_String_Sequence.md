# Lesson 4.1: A string is a sequence

## Overview

You live-code a `for` loop that walks through a string one character
at a time, then turn it into a counter with `+=`. Students write a
vowel counter on their own, then pairs build a small letter counter of
their own design. The comparison table of data structures starts today
with its string column.

## Objectives

Students will be able to:

- write a `for` loop that visits every character of a string
- count the characters that pass a test, with a counter that starts at
  0 and grows with `+=`
- use `len` to measure a string and `in` to test whether a piece of
  text is inside it
- predict what a loop over a string prints before running it

## Preparation

- [ ] Put the three 4.1 questions from
  `materials/PLICKERS_4_Questions.md` into Plickers; have the cards
  out.
- [ ] Import Codio U6.L4 String Iteration into the class. Set it due
  before lesson 4.4 (see the Codio section for why).
- [ ] Open the two Python Tutor links in browser tabs: one in the
  Concept section, one with the peer instruction reveal in Extras.
- [ ] Draw the comparison table frame, all four columns, on a wall
  whiteboard (end of the Concept section), or plan to project it.

## Reading

Due today: nothing.
Assign tonight: Think Python chapter 7, "Iteration and Search." Students
skip the "Doctest" section. Reading quiz at the next lesson; chapter 8
is assigned then too.

## Agenda

### Reading quiz (none today)

No reading was due. The chapter 7 quiz is at lesson 4.2. Give the five
minutes to the Concept or the partner challenge.

### Concept (10 min)

**Fall 2026:** this is the first `for` loop students have seen that is
not over `range`. `+=`, `len`, and `print(x, end=' ')` are new as well;
each needs one sentence.

Type each step in Thonny and run it.

**1. Start from the loop they know.**

```python
for i in range(3):
    print(i, end=' ')
```

```text
0 1 2
```

Say: "You've written this loop all semester. `end=' '` tells `print`
to put a space after the value instead of starting a new line."

**2. Put a string where `range(3)` was.**

```python
for letter in 'Gadsby':
    print(letter, end=' ')
```

```text
G a d s b y
```

Say: "No `range` and no numbers. A string is a sequence of characters,
and `for` hands you each character in turn, first to last. I called the
loop variable `letter` because that's what it holds." *Gadsby* is the
novel without an "e"; chapter 7, assigned tonight, opens with it.

**3. Count, and forget to start the counter.** Type this without a
`count = 0` line. The error is on purpose.

```python no-run
word = 'Mississippi'
for letter in word:
    if letter == 's':
        count += 1
print(count)
```

```text
Traceback (most recent call last):
  File "program.py", line 4, in <module>
    count += 1
    ^^^^^
NameError: name 'count' is not defined. Did you mean: 'round'?
```

Say: "`count += 1` is short for `count = count + 1`. Python works out
the right side first, and there is no `count` yet. Ignore the 'Did you
mean' part: Python is suggesting a name it knows that looks similar,
and `round` has nothing to do with this." Add `count = 0` above the
loop and run again.

```python
word = 'Mississippi'
count = 0
for letter in word:
    if letter == 's':
        count += 1
print(count)
```

```text
4
```

[Open in Python Tutor](https://pythontutor.com/visualize.html#code=word%20%3D%20%27Mississippi%27%0Acount%20%3D%200%0Afor%20letter%20in%20word%3A%0A%20%20%20%20if%20letter%20%3D%3D%20%27s%27%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%201%0Aprint%28count%29%0A&mode=display&py=311&curInstr=0)

Step through it and stop on each `s`. Say: "A variable that starts at
0 and goes up by one each time something happens is called a
counter."

**4. `len` and `in`.**

```python
word = 'Mississippi'
print(len(word))
print('s' in word)
print('ss' in word)
print('S' in word)
```

```text
11
True
True
False
```

Say: "`len` counts the characters. `in` answers yes or no, for one
character or a longer piece of the string. A capital S is a different
character from a lowercase s."

**Peer instruction, three questions.** Run them in this order. For
each: vote, argue with a partner, revote, then reveal.

**Question 1.** Source: written for CS4120.

What does this print?

```python
total = 0
for ch in 'abcab':
    if ch in 'ab':
        total += 1
print(total)
```

- A. 0
- B. 2
- C. 4
- D. 5

Answer: **C.** Run it to reveal:

```text
4
```

- A catches thinking `ch` holds the whole string `'abcab'`, so the
  loop runs once and `'abcab' in 'ab'` is `False`.
- B catches thinking `in 'ab'` looks for the pair "ab", which appears
  twice in `'abcab'`.
- D catches skipping the `if` and counting every character.

**Question 2.** Source: written for CS4120.

What does this print?

```python
s = 'banana'
print(len(s), 'nan' in s, 'ab' in s)
```

- A. 6 True True
- B. 5 True False
- C. 6 False False
- D. 6 True False

Answer: **D.** Run it to reveal:

```text
6 True False
```

- A catches reading `'ab' in s` as "are a and b both somewhere in s,"
  one character at a time, instead of as the piece "ab" in that order.
- B catches thinking `len` gives the last position, 5, instead of the
  count.
- C catches thinking `in` works for one character only, so a longer
  piece is never found.

**Question 3.** Source: Cynthia Taylor, `11_strings` slide 12.
Changes: tabs shown as four spaces; her "I don't know" option dropped.

What does this code do?

```python
def mystery(s):
    new_s = ""
    for c in s:
        new_s = c + new_s
    return new_s
```

- A. Return a copy of s
- B. Return the reverse of s
- C. Return a string with only the last character of s
- D. Return a string with only the first character of s

Answer: **B.** To reveal, run it on `'dog'` (it prints `god`) or step
through it in Python Tutor; the reveal program and its link are in
Extras.

- A catches reading `c + new_s` as `new_s + c`, so each character goes
  on the end.
- C catches thinking each assignment throws away everything but the
  current character.
- D catches reading `return new_s` as inside the loop, so the function
  stops after one character.

**The comparison table** (project this). Students copy the whole
frame, all four columns, into their journals, on a page turned
sideways. Tell them the three empty columns are for things the unit
has not taught yet: lists in 4.5, dictionaries in 4.9, tuples in 4.12.
Today fills two rows of the String column; the rest fills in over the
coming lessons.

| | String | List | Dictionary | Tuple |
|---|---|---|---|---|
| How you write one | `'abc'` | | | |
| How you reach one element | | | | |
| Has an order | | | | |
| Can be changed in place | | | | |
| `len`, `in`, `for` | all three; `in` finds a piece of the string; `for` gives each character | | | |

### Try it (10 min)

Project this:

> Write a function `num_vowels(s)` that returns the number of vowels
> in the string `s`. Count capital vowels too. The vowels are a, e, i,
> o, and u. Test it: `num_vowels('Gadsby')` should give 1, and
> `num_vowels('EDUCATION')` should give 5.

Source: Cynthia Taylor, `11_strings` slide 11 (a practice exercise).

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

For students who finish: `count_letter(word, letter)`, which counts
one chosen letter; counting the spaces in a sentence; counting digits
with `'0123456789'`. Keys are in Extras.

### Mini-project (15 min)

<!-- Partner challenge: today the mini-project takes this slot, as the
unit plan marks for lesson 4.1. -->

Pairs, as in a partner challenge: sketch the steps on the table
whiteboard first, then type in Thonny.

Project this:

> **Letter counter.** Write a program that asks the user to type a
> sentence and then reports something about its characters. Pick one:
>
> - **Letter hunt.** Also ask for a letter. Print how many times that
>   letter appears, counting capitals too.
> - **Sentence report.** Print how many characters, letters, vowels,
>   and spaces the sentence has.
> - **Gadsby check.** Print how many e's the sentence has. If there
>   are none, print a message saying it could go in *Gadsby*.
>
> Your prompt should tell the user what to type.

While you walk the room, look for:

- the counter set to 0 above the loop, not inside it
- the `print` lined up with `for`, not inside the loop
- capitals handled, with `.lower()` on the input or both cases in the
  test string
- a prompt that says what to type, as in the text adventure

Sample solution, sentence report:

<!-- plan_check input: ["Gadsby is a novel without the letter E"] -->
```python
# Sentence report: counts the letters, vowels, and spaces in a sentence.
sentence = input('Type a sentence: ').lower()   # lowercase, so capitals count

letters = 0                                     # three counters, all start at 0
vowels = 0
spaces = 0

for c in sentence:                              # visit every character
    if c in 'abcdefghijklmnopqrstuvwxyz':       # a letter?
        letters += 1
    # A vowel is also a letter, so both counters go up.
    if c in 'aeiou':                            # a vowel?
        vowels += 1
    if c == ' ':                                # a space?
        spaces += 1

# The report is built in two steps to keep each line short.
report = f'{len(sentence)} characters, {letters} letters, '
report = report + f'{vowels} vowels, {spaces} spaces'
print(report)
```

```text
Type a sentence: Gadsby is a novel without the letter E
38 characters, 31 letters, 12 vowels, 7 spaces
```

### Codio (10 min)

Students start **U6.L4 String Iteration** (Codio Unit 6, lesson 4).
Tonight they do Learning Objectives, Concept Overview, "Iteration -
For Loop," and Formative Assessment 1; those are due before lesson 4.2.
The Concept Overview (page 324 of the export) also shows a `while` loop
that reaches each character with `word[index]`, and the "Iteration -
While Loop" page and Formative Assessment 2 depend on it. Indexing is
lesson 4.3, so students skim that example tonight and finish the
`while` page and the second check after 4.3. The whole assignment is
due before lesson 4.4.

## Pitfalls

- **No starting value.** `NameError: name 'count' is not defined`
  (Concept step 3). Say: "Where does the counter start?"
- **`count = 0` inside the loop.** No error; the count comes out 0 or
  1, because the counter is reset on every pass. Ask: "When does that
  line run?"
- **`print(count)` inside the loop.** The program prints a running
  count, one number per character. Ask: "How many times should this
  print?"
- **`count =+ 1`.** No error. Python reads it as `count = +1`, so the
  count is 1 forever. Read the line aloud with the student.
- **Capitals.** `'S' == 's'` is `False`, so "Sam" has no s. Use
  `.lower()` first, or test both cases.
- **`return count` inside the loop** (try it). The function answers
  after the first character. That shape is the next lesson's topic, so
  a quick "line it up with `for`" is enough.

## Quick check

Four choices, so the deck runs it as a fingers-up vote.

How many times does the body of this loop run?

```python
for c in 'Hi there':
    print(c)
```

1. 7
2. 8
3. 2
4. 1

Answer: 2, eight times. The space is a character too, so the loop
visits H, i, the space, t, h, e, r, e. `len('Hi there')` is 8 for the
same reason.

- 1 catches skipping the space.
- 3 catches counting the words.
- 4 catches thinking `c` holds the whole string, so the body runs once.

## Extras

**Peer instruction reveal.** The `mystery` function from the Concept
section, run on `'dog'`.

```python
def mystery(s):
    new_s = ""
    for c in s:
        new_s = c + new_s
    return new_s

print(mystery('dog'))
```

```text
god
```

[Open in Python Tutor](https://pythontutor.com/visualize.html#code=def%20mystery%28s%29%3A%0A%20%20%20%20new_s%20%3D%20%22%22%0A%20%20%20%20for%20c%20in%20s%3A%0A%20%20%20%20%20%20%20%20new_s%20%3D%20c%20%2B%20new_s%0A%20%20%20%20return%20new_s%0A%0Aprint%28mystery%28%27dog%27%29%29%0A&mode=display&py=311&curInstr=0)

**Try it variants, keys.**

```python
# count_letter: how many times one chosen letter appears, any case.
def count_letter(word, letter):
    count = 0
    for c in word.lower():            # lowercase the word once
        if c == letter.lower():       # and the letter, so 'S' matches 's'
            count += 1
    return count

print(count_letter('Mississippi', 'S'))
```

```text
4
```

```python
# Spaces in a sentence. One step further: there is one more word than
# there are spaces (as long as the sentence has single spaces and no
# space at either end).
sentence = 'the quick brown fox jumps over the lazy dog'
spaces = 0
for c in sentence:
    if c == ' ':
        spaces += 1
print(spaces, 'spaces')
print(spaces + 1, 'words')
```

```text
8 spaces
9 words
```

```python
# count_digits: characters that are digits.
def count_digits(s):
    count = 0
    for c in s:
        if c in '0123456789':
            count += 1
    return count

print(count_digits('Room 2104, 3rd floor'))
```

```text
5
```

**Connections.** The counter is the first accumulator pattern of the
unit: in lesson 4.4 the same loop builds a string, and later in the
unit it fills a list and then a dictionary of counters.
