# Peer Instruction Questions: Classes, Objects, and Inheritance

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Classes and objects

### Q1. Which of the following is not a possible method for a Car class?

**Source:** `18_classesobjects.pptx` slide 9 - worked answer in `18_classesobjects.pdf`

Which of the following is not a possible method for a Car class?

- **A.** open_window
- **B.** accelerate
- **C.** num_wheels
- **D.** turn_right
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say C, and C is circled in the annotated PDF - num_wheels is something a car has (an attribute), not an action it does.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: methods-vs-attributes*

### Q2. What is the output of this code?

**Source:** `18_classesobjects.pptx` slide 13 - worked answer in `18_classesobjects.pdf`

What is the output of this code?

```python
p1 = Point()
p1.x = p1.x + 2
p1.y = p1.x + 3
p2 = Point()
p2.x = p2.x + 4
print(p2.x, p2.y)
```

- **A.** 0 0
- **B.** 4 0
- **C.** 2 3
- **D.** 7 3
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker notes say B, and B is circled in the annotated PDF with a worked trace: p1 ends at (2, 5), p2 is a separate object starting at (0, 0), so p2.x becomes 4 and p2.y stays 0, printing 4 0.

**Code check:** confirmed by execution

**Extraction note:** Depends on the Point class defined on slide 11, whose __init__ sets self.x = 0 and self.y = 0.

*Also touches: attribute-access, object-identity, variables-and-assignment*

### Q3. t is an object of class Thing and d, e, and f are defined. What is the proper way to ca...

**Source:** `19_methods.pptx` slide 4 - worked answer in `19_methods.pdf`

t is an object of class Thing and d, e, and f are defined. What is the proper way to call do_it?

```python
class Thing(object):
	def do_it(self, a, b, c):
		...
```

- **A.** do_it(d, e, f)
- **B.** do_it(self, d, e, f)
- **C.** do_it(t, d, e, f)
- **D.** t.do_it(d, e, f)
- **E.** t.do_it(t, d, e, f)

**Answer:** D (from Dr. Taylor's speaker notes)

**Detail:** Speaker notes state D; t.do_it(d, e, f) is the proper method-call syntax since self is passed implicitly.

**Code check:** confirmed by execution

**Extraction note:** PDF annotation circles the letter E and strikes out the extra first argument t inside E's call, apparently demonstrating why E is wrong (removing the explicit t turns E into D); read as consistent with the notes' answer D rather than a disagreement.

*Also touches: methods, calling-syntax, self-parameter*

### Q4. What is the output of this code?

**Source:** `19_methods.pptx` slide 6 - worked answer in `19_methods.pdf`

What is the output of this code?

```python
class Thing(object):
	def __init__(self, a, b):
		self.val = a * b

	def __str__(self):
		return '[' + str(self.val + 2) + ']'
t = Thing(4, 5)
print(t)
```

- **A.** 20
- **B.** [20]
- **C.** 22
- **D.** [22]
- **E.** A memory address

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D and the PDF circles D, with handwritten working showing a=4, b=5, self.val=20, so __str__ returns [22].

**Code check:** confirmed by execution

*Also touches: special-methods, str-method, constructors*

### Q5. Which of the following would evaluate to True?

**Source:** `19_methods.pptx` slide 8 - worked answer in `19_methods.pdf`

Which of the following would evaluate to True?

```python
class Account(object):
	def __init__(self, val):
		self.gold = val
	def __eq__(self, other):
		return self.gold==0 and other.gold==5
```

- **A.** Account(50) == Account(50)
- **B.** Account(80) == Account(90)
- **C.** Account(0) == Account(5)
- **D.** Account(0) == Account(0)
- **E.** More than one of the above

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and the PDF circles C; a == b calls a.__eq__(b), which is True only when self.gold is 0 and other.gold is 5.

**Code check:** confirmed by execution

*Also touches: operator-overloading, eq-method, booleans-and-logic*

### Q6. Which code for __ne__ is correct?

**Source:** `19_methods.pptx` slide 11 - worked answer in `19_methods.pdf`

Which code for __ne__ is correct?

- **A.** def __ne__(self, p):
	return not self == p
- **B.** def __ne__(self, p):
	return self.x == p.x and self.y == p.y
- **C.** def __ne__(self, p):
	if self.x =! p.x or self.y != p.y:
		return True
	return False
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D = A and C' and the PDF circles options A and C, so D (more than one) was the in-class answer.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option C contains '=!' verbatim from the slide, which is a syntax error as written (clearly intended as '!='); the instructor counted C as correct anyway. Strictly as written, only A is valid Python.

*Also touches: operator-overloading, ne-method, booleans-and-logic*

### Q7. We want the point closer to the origin to be the lesser point.  Which code is correct?

**Source:** `19_methods.pptx` slide 12 - worked answer in `19_methods.pdf`

We want the point closer to the origin to be the lesser point.  Which code is correct?

- **A.** def __lt__(self, p):
	if self.x < p.x and self.y < p.y:
		return True
	return False
- **B.** def __lt__(self, p):
	if self.magnitude() < p.magnitude():
		return True
	return False
- **C.** def __lt__(self, p):
	my_val = math.sqrt(self.x**2 + self.y**2)
	p_val = math.sqrt(p.x**2 + p.y**2)
	if my_val < p_val:
		return True
	return False
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - B and C' and the PDF circles B, C, and D; both magnitude-based versions implement distance-to-origin ordering, while A's componentwise comparison does not (PDF counterexample: (1,1) vs (5,5) and (-1,-1) vs (-7,-7)).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: operator-overloading, lt-method, conditionals*

### Q8. Implement <=

**Source:** `19_methods.pptx` slide 13 - worked answer in `19_methods.pdf`

Implement <=

- **A.** def __le__(self, p):
	if self < p or self == p:
		return True
	return False
- **B.** def __le__(self, p):
	if self.magnitude() =< p.magnitude():
		return True
	return False
- **C.** def __le__(self, p):
	if self.x <= p.x and self.y <= p.y:
		return True
	return False
- **D.** More than one of the above
- **E.** I don't know

**Answer:** A (from her handwritten in-class annotations (PDF))

**Detail:** Notes say B, but the annotated PDF marks only option A (red bracket beside A's box and underline under 'self == p'), and B as written uses the invalid operator '=<'; preferring the PDF, the answer is A, the only correct code as written.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Notes/PDF discrepancy: notes say B, PDF handwriting marks A. Option B contains '=<' verbatim (a typo for '<=', a syntax error as written); if read as '<=', both A and B would be correct, which would make D arguable. Recorded A per the PDF and per strict reading of the code.

*Also touches: operator-overloading, le-method, conditionals*

### Q9. What is the output of this code?

**Source:** `20_inheritance.pptx` slide 13 - worked answer in `20_inheritance.pdf`

What is the output of this code?

```python
class A:
    count = 0
    def __init__(self, x):
        self.x = x+1
        A.count= A.count+1

A1 = A(2)
A2 = A(4)
A3 = A(5)

print(A1.x, A1.count, A.count)
```

- **A.** 3, 1, 1
- **B.** 3, 1, 3
- **C.** 3, 3, 3
- **D.** 2, 1, 1
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C; PDF has C circled with "3" worked over each of A1.x, A1.count, and A.count - the class variable count is shared, so all three constructions increment it to 3.

**Code check:** confirmed by execution

**Extraction note:** Labels A-D absent from the text dump (only E labeled on slide); taken from the rendered PDF. Missing space in "A.count= A.count+1" is verbatim from the slide.

*Also touches: class-variables, instance-vs-class-attributes*

### Q10. Want to have 3 different stats, evenly distributed between my critters

**Source:** `28_bubbleandmerge.pptx` slide 2 - worked answer in `28_moresorting.pdf`

Want to have 3 different stats, evenly distributed between my critters

- **A.** num_critters = 0
....

def getStats(self):
	CynthiaT.num_critters += 1
	if CynthiaT.num_critters%3 == 0:
		return 90,10
	elif CynthiaT.num_critters%3 == 1:
		return 50,50
	else:
		return 10,90
- **B.** def __init__(self):
	self.num_critters = 0
....

def getStats(self):
	self.num_critters += 1
	if self.num_critters%3 == 0:
		return 90,10
	elif self.num_critters%3 == 1:
		return 50,50
	else:
		return 10,90
- **C.** def getStats(self):
	num_critters = 0
	num_critters += 1
	if num_critters%3 == 0:
		return 90,10
	elif num_critters%3 == 1:
		return 50,50
	else:
		return 10,90
- **D.** Something else
- **E.** I don't know

**Answer:** A (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say A and the PDF shows A circled; a class-level variable is shared across all critters, and the instructor circled C's num_critters = 0 line as the bug (local counter resets every call).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Options are three code blocks laid out in two columns; label-text pairing confirmed against the annotated PDF layout.

*Also touches: class-variables, instance-variables, variable-scope*

#### Practice exercises (Classes and objects)

### Q11. Write code for __eq__

**Source:** `19_methods.pptx` slide 10 - worked answer in `19_methods.pdf` (practice exercise, no answer options)

Write code for __eq__

**Answer:** def __eq__(self, p):
	return isinstance(p, Point) and self.x == p.x and self.y == p.y (inferred during extraction - not marked in the source materials)

**Detail:** No answer on the slide, notes, or PDF (the annotated page is blank); model solution inferred from slide 9's spec that Points are equal when both are Points and their x and y coordinates are equal.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Live-coding exercise slide (blank body). Context from slide 9: add __eq__ to the Point class; points are equal when they are both points and the x-coordinates and y-coordinates match.

*Also touches: operator-overloading, eq-method*

### Q12. Suppose you want to create a class called Pirate to represent pirates. Each instance of...

**Source:** `25_review.pptx` slide 12 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Suppose you want to create a class called Pirate to represent pirates. Each instance of Pirates should include fields to store the given pirate's name, how many gold doubloons he has, and a boolean value indicating whether or not he has a pegleg. The Pirate class should also keep track of how many pirates have been created.

Write a class definition for Pirate, with a constructor that takes in the name of the pirate, and if he has a peg leg. The constructor should also have an argument doubloons, with a default value of 0.

**Answer:** class Pirate:
    numPirates = 0
    def __init__(self, name, pegleg, doubloons=0):
        self.name = name
        self.pegleg = pegleg
        self.doubloons = doubloons
        Pirate.numPirates += 1 (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (class variable counts instances, constructor with a default argument).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** First of a five-part Pirate class sequence (slides 12-16).

*Also touches: constructors, class-variables, default-arguments*

### Q13. Write a function called rob that takes in another pirate p and takes away the doubloons...

**Source:** `25_review.pptx` slide 13 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Write a function called rob that takes in another pirate p and takes away the doubloons belonging to p and gives them to the pirate calling the method.

**Answer:** def rob(self, p):
    self.doubloons += p.doubloons
    p.doubloons = 0 (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (method inside the Pirate class transferring p's doubloons to self).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Continues the Pirate class from slide 12.

*Also touches: methods, self, object-state*

### Q14. Write a client program to do the following: Create a pirate named "Pegleg Pete" who has...

**Source:** `25_review.pptx` slide 14 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Write a client program to do the following: Create a pirate named "Pegleg Pete" who has a peg leg and 0 doubloons, and a pirate named "Hookhand Harry" who does not have a peg leg, and has 50 doubloons. Have Pegleg Pete rob Hookhand Harry.

**Answer:** pete = Pirate("Pegleg Pete", True)
harry = Pirate("Hookhand Harry", False, 50)
pete.rob(harry) (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (instantiate two Pirates, relying on the doubloons default for Pete, then call the rob method).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Depends on the Pirate class from slides 12-13.

*Also touches: instantiation, method-calls, client-code*

### Q15. Define a new Pirate function called attack that takes in another Captain seadog and sin...

**Source:** `25_review.pptx` slide 16 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Define a new Pirate function called attack that takes in another Captain seadog and sinks his ship.

**Answer:** def attack(self, seadog):
    seadog.sunk = True (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (method in Pirate that sets the Captain's sunk field to True).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Final part of the Pirate class sequence (slides 12-16).

*Also touches: inheritance, methods, object-state*

### Q16. What is wrong with this code?

**Source:** `35_review.pptx` slide 4 - worked answer in `35_review.pdf` (practice exercise, no answer options)

What is wrong with this code?

```python
def __init__(a,b,c):
	a = self.a
	b = self.b
	c = self.c
```

**Answer:** The __init__ is missing the self parameter, and the assignments are backwards: self.a, self.b, self.c are not yet defined, so it should be self.a = a, self.b = b, self.c = c. (from her handwritten in-class annotations (PDF))

**Detail:** PDF annotations insert 'self,' into the parameter list, circle the self.a/self.b/self.c right-hand sides as 'not defined', and write the corrected form self.a = a.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: variables-and-assignment, debugging*

## Inheritance

### Q17. In the following pairs of words, the first is the subclass and the second is the superc...

**Source:** `20_inheritance.pptx` slide 5 - worked answer in `20_inheritance.pdf`

In the following pairs of words, the first is the subclass and the second is the superclass. Which of them is a correct example of inheritance?

- **A.** dog, cat
- **B.** dog, animal
- **C.** animal, dog
- **D.** dog, tail
- **E.** None of the above

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF has B circled with handwritten "is-a" next to dog/animal and "has-a" next to dog/tail.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option letters absent from the text dump (plain list on slide); A-E labels taken from the rendered PDF.

*Also touches: is-a-vs-has-a, classes-and-objects*

### Q18. What is the output of this code?

**Source:** `20_inheritance.pptx` slide 7 - worked answer in `20_inheritance.pdf`

What is the output of this code?

```python
class A:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

class B(A):
    def __init__(self, x):
        self.x = x * 2

b = B(5)
print(b)
```

- **A.** 5
- **B.** 10
- **C.** 510
- **D.** This will cause an error
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B; PDF has B circled with "10" worked next to self.x = x * 2 - B's overriding __init__ doubles x and the inherited __str__ prints it.

**Code check:** confirmed by execution

*Also touches: method-overriding, dunder-methods, classes-and-objects*

### Q19. What is the output of this code?

**Source:** `20_inheritance.pptx` slide 9 - worked answer in `20_inheritance.pdf`

What is the output of this code?

```python
p = Person("George", "Williker")
s = Student("Buddy","Bob","2014")
s.study()
p.study()
```

- **A.** "Need to study... but...Internet!" will print twice
- **B.** "Need to study... but...Internet!" will print once
- **C.** Nothing will print
- **D.** This will cause an error
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say D; PDF boxes p.study() as the failing line - study is defined on the Student subclass only, so calling it on a Person raises an AttributeError.

**Code check:** confirmed by execution

**Extraction note:** Depends on Person/Student class definitions written live in class (slide 8 is blank); the study() method is not shown on any slide.

*Also touches: method-lookup, exceptions, classes-and-objects*

#### Practice exercises (Inheritance)

### Q20. Define a subclass of Pirate called Captain that includes the name of the pirate's ship,...

**Source:** `25_review.pptx` slide 15 - worked answer in `25_review.pdf` (practice exercise, no answer options)

Define a subclass of Pirate called Captain that includes the name of the pirate's ship, the ship's maximum speed, and a boolean value indicating if the ship has sunk. The class Captain should override its parent's constructor. The new constructor should take in the pirate's name, peg leg status, ship's name, maximum speed of ship, and optional number of doubloons. The constructor should first call the constructor for Pirate, but then add new fields to add the ship's name, speed, and sunkenness.

**Answer:** class Captain(Pirate):
    def __init__(self, name, pegleg, shipName, maxSpeed, doubloons=0):
        Pirate.__init__(self, name, pegleg, doubloons)
        self.shipName = shipName
        self.maxSpeed = maxSpeed
        self.sunk = False (inferred during extraction - not marked in the source materials)

**Detail:** No solution in notes or PDF; model solution written by the extractor (subclass overrides __init__, calls the parent constructor, then adds ship fields).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

**Extraction note:** Builds on the Pirate class from slide 12.

*Also touches: classes-and-objects, constructors, method-overriding*

### Q21. Create a subclass of S, R, which says "Wheee!" instead of "Hi", and eats pizza instead...

**Source:** `35_review.pptx` slide 13 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Create a subclass of S, R, which says "Wheee!" instead of "Hi", and eats pizza instead of kale. Its sleep should remain the same.

```python
class S:
	def talk(self):
		return "Hi!"

	def nom(self):
		return "Delicious kale!"

	def sleep(self):
		return "zzzzzz"
```

**Answer:** not recorded in the source materials

*Also touches: classes-and-objects, method-overriding*

### Q22. Create a subclass of S, R, which says "Wheee!" instead of "Hi", and eats pizza instead...

**Source:** `36_review.pptx` slide 11 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Create a subclass of S, R, which says "Wheee!" instead of "Hi", and eats pizza instead of kale. Its sleep should remain the same.

```python
class S: 
	def talk(self): 
		return "Hi!" 

	def nom(self): 
		return "Delicious kale!" 

	def sleep(self): 
		return "zzzzzz"
```

**Answer:** Handwritten: class R(S): with def talk(self): return "Wheeeee!" and def nom(self): return "Delicious pizza!"; sleep is not overridden so it is inherited from S. (from her handwritten in-class annotations (PDF))

**Detail:** Worked handwritten solution beside the code on the annotated PDF page (PDF page 12); a following inserted handwritten page (PDF page 13) also demonstrates __init__ chaining with class S and class R(S) calling S.__init__(self, a).

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: classes-and-objects, method-overriding*
