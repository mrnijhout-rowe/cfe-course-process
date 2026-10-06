# Peer Instruction Questions: Processes and Concurrency

Source: Dr. Cynthia Taylor's CS1 slide decks (see README.md in this folder
for provenance, license, and conventions). Answers are hers unless marked
as inferred.

## Processes

### Q1. To create a new process to run this procedure on arguments d,e,f

**Source:** `31_processes.pptx` slide 8 - worked answer in `31_processes.pdf`

To create a new process to run this procedure on arguments d,e,f

```python
def newProc(a,b,c):
	...
```

- **A.** p = Process(newProc,d,e,f)
- **B.** p = Process(target=newProc, args=d,e,f)
- **C.** p = Process(target=newProc, args=(d,e,f))
- **D.** p = Process(target=newProc(a,b,c), args=(d,e,f))
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says C; PDF page 11 has C circled, with margin notes marking A as lacking named args, B's args as not a tuple, and D as calling the function instead of passing it.

**Code check:** confirmed by execution

*Also touches: functions-as-arguments, keyword-arguments, tuples*

### Q2. We have two processes, A and B.  Both have an execution time of 20 ms.  A starts before...

**Source:** `31_processes.pptx` slide 12 - worked answer in `31_processes.pdf`

We have two processes, A and B.  Both have an execution time of 20 ms.  A starts before B.  Which will finish running first?

- **A.** A
- **B.** B
- **C.** There is no way to tell
- **D.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says C; PDF page 15 has C circled - the OS controls scheduling, so completion order is not predictable.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: scheduling, nondeterminism, concurrency*

### Q3. How many times will "Hello" print?

**Source:** `31_processes.pptx` slide 13 - worked answer in `31_processes.pdf`

How many times will "Hello" print?

```python
def spawn():
	print("Hello")
	for i in range(2):
		p = Process(target=toRun)
		p.start()

def toRun():
	print("Hello")

def main():
	for i in range(4):
		p = Process(target=spawn)
		p.start()
```

- **A.** 2
- **B.** 8
- **C.** 12
- **D.** 16
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says C; PDF page 16 has C (12) circled with a worked process tree - main spawns 4 spawn processes (4 Hellos), each of which spawns 2 toRun processes (8 more), totaling 12.

**Code check:** confirmed by execution

*Also touches: for-loops, tracing, spawning-processes*

### Q4. Will we always get faster results with more processes in the pool?

**Source:** `32_communication.pptx` slide 8 - worked answer in `32_communication.pdf`

Will we always get faster results with more processes in the pool?

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says 'B' and the PDF has B circled; next slide explains that creating and switching between processes costs time and resources, so speedup does not grow forever.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

*Also touches: concurrency, performance, overhead*

#### Practice exercises (Processes)

### Q5. Write code to create a pool of 4 processes, and use them to compute the sum of the numb...

**Source:** `32_communication.pptx` slide 7 - worked answer in `32_communication.pdf` (practice exercise, no answer options)

Write code to create a pool of 4 processes, and use them to compute the sum of the numbers 1 . . . . n

**Answer:** not recorded in the source materials

**Detail:** No worked solution appears in the notes, later slides, or the annotated PDF (page 7 has only an underline scribble); speaker note says 'Add clicker questions on this'.

**Extraction note:** Exercise slide without options; solved live in class with no recorded solution.

*Also touches: concurrency, pool-map, functions*

### Q6. Assume you have a very large number, n, and a list, P, that consists of the primes from...

**Source:** `35_review.pptx` slide 11 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Assume you have a very large number, n, and a list, P, that consists of the primes from 2 to the first prime larger than the square root of n. Use a process pool with 4 processes to determine if n is prime.

**Answer:** not recorded in the source materials

*Also touches: concurrency, lists*

### Q7. Assume you have a very large number, n, and a list, P, that consists of the primes from...

**Source:** `36_review.pptx` slide 9 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Assume you have a very large number, n, and a list, P, that consists of the primes from 2 to the first prime larger than the square root of n. Use a process pool with 4 processes to determine if n is prime.

**Answer:** Create multiprocessing.Pool(4), map a helper such as def divides(p): return n % p == 0 over P (e.g. results = pool.map(divides, P)), and report n prime iff no result is True (not any(results)). (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes or PDF (the PDF page only underlines parts of the prompt); solution sketched by the extractor from the course's standard Pool.map pattern.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: concurrency, process-pool, multiprocessing*

## Concurrency

### Q8. Would it fix this to say r.value = r.value + 1?

**Source:** `32_communication.pptx` slide 16 - worked answer in `32_communication.pdf`

Would it fix this to say r.value = r.value + 1?

```python
r.value = r.value + 1
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Speaker note says 'B' and the PDF has B circled with handwritten reasoning showing the one line still decomposes into get r.value, add 1, set r.value, so processes can still interleave between machine instructions.

**Code check:** confirmed by execution

**Extraction note:** Refers to the RawValue race-condition scenario set up on slides 13-15 (two processes both incrementing a shared RawValue).

*Also touches: processes, race-conditions, shared-memory, atomicity*

### Q9. What is the BEST version of this code?

**Source:** `33_synchronization.pptx` slide 5 - worked answer in `33_synchronization.pdf`

What is the BEST version of this code?

- **A.** def func(r,lock):
	lock.acquire()
	for i in range(10):
		r.value = r.value + 1
		time.sleep(.05)
	lock.release()
- **B.** def func(r,lock):
	for i in range(10):
		lock.acquire()
		r.value = r.value + 1
		lock.release()
		time.sleep(.05)
- **C.** def func(r,lock):
	for i in range(10):
		r.value = r.value + 1
		lock.acquire()
		time.sleep(.05)
		lock.release()
- **D.** Multiple options are equally good
- **E.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF circles B - acquire and release inside the loop around just the shared update, keeping the sleep outside the locked section.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option labels A/B/C were interleaved with the code blocks in the text dump; pairing confirmed via pptx shape positions and the annotated PDF (A top-left, B top-right, C bottom-left).

*Also touches: locks, processes, critical-section*

### Q10. Will this code give us consistent results?

**Source:** `33_synchronization.pptx` slide 7 - worked answer in `33_synchronization.pdf`

Will this code give us consistent results?

```python
def func(r):
	lock = Lock()
	for i in range(10):
		lock.acquire()
		r.value = r.value + 1
		lock.release()
		time.sleep(.05)
```

- **A.** Yes
- **B.** No
- **C.** I don't know

**Answer:** B (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say B and the PDF circles No with handwritten 'need shared lock' - each process creates its own Lock inside func, so the lock protects nothing; it must be created once and passed in.

**Code check:** confirmed by execution

*Also touches: locks, processes, shared-memory*

### Q11. What will happen if we run this code?

**Source:** `33_synchronization.pptx` slide 8 - worked answer in `33_synchronization.pdf`

What will happen if we run this code?

```python
def func(r,lock):
	for i in range(10):
		lock.acquire()
		r.value = r.value + 1
		time.sleep(.0001)
r = RawValue("i",0)
lock = Lock()
for i in range(10):
	p = Process(target=func, args=(r,lock))
	p.start()
```

- **A.** Everything will be okay
- **B.** It will cause an error
- **C.** It will print once and then stop
- **D.** Something else
- **E.** I don't know

**Answer:** C (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say C and the PDF circles C with handwritten 'always all release!' - the lock is acquired but never released, so whichever process gets it first blocks all others after one update.

**Code check:** confirmed by execution

*Also touches: locks, deadlock, processes*

### Q12. Which of these could cause deadlock?

**Source:** `33_synchronization.pptx` slide 10 - worked answer in `33_synchronization.pdf`

Which of these could cause deadlock?

- **A.** def func(l1,l2):
	l1.acquire()
	l2.acquire()
	#code
	l2.release()
	l1.release()

def func2(l1,l2):
	l2.acquire()
	l1.acquire()
	#code
	l1.release()
	l2.release()
- **B.** def func(l1,l2):
	l1.acquire()
	#code
	l1.release()
	l2.acquire()
	#code
	l2.release()

def func2(l1,l2):
	l2.acquire()
	#code
	l2.release()
	l1.acquire()
	#code
	l1.release()
- **C.** def func(l1,l2):
	l1.acquire()
	l2.acquire()
	#code
	l1.release()
	l2.release()

def func2(l1,l2):
	l2.acquire()
	l1.acquire()
	#code
	l2.release()
	l1.release()
- **D.** More than one of the above
- **E.** I don't know

**Answer:** D (speaker notes, confirmed by her in-class annotations (PDF))

**Detail:** Notes say 'D - A and C' and the PDF circles D along with A and C (B marked 'OK') - A and C both acquire the two locks in opposite orders across the two functions, which can deadlock; B never holds both locks at once.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) reached the same answer.

**Extraction note:** Option labels A/B/C were interleaved with the code blocks in the text dump; pairing confirmed via pptx shape positions and the annotated PDF (A left column, B middle, C right).

*Also touches: deadlock, locks, processes*

#### Practice exercises (Concurrency)

### Q13. Write code where 10 processes each add 1 to r.value 10 times, ending with r.value equal...

**Source:** `35_review.pptx` slide 12 - worked answer in `35_review.pdf` (practice exercise, no answer options)

Write code where 10 processes each add 1 to r.value 10 times, ending with r.value equal to 100. Make sure you use the lock to ensure you end up with the correct result.

**Answer:** not recorded in the source materials

*Also touches: processes, locks*

### Q14. Write code where 10 processes each add 1 to a RawValue r 10 times, ending with r.value...

**Source:** `36_review.pptx` slide 10 - worked answer in `36_review.pdf` (practice exercise, no answer options)

Write code where 10 processes each add 1 to a RawValue r 10 times, ending with r.value equal to 100. Make sure you use the lock to ensure you end up with the correct result.

**Answer:** Create r = RawValue('i', 0) and lock = Lock(); worker does for i in range(10): lock.acquire(); r.value += 1; lock.release(); spawn 10 Process objects with the worker as target, start them all, join them all, then r.value == 100. (inferred during extraction - not marked in the source materials)

**Detail:** No answer in notes or on the annotated PDF page; solution sketched by the extractor from the course's standard RawValue-plus-Lock pattern.

**Concept check:** confirmed - an independent blind solve (recorded answer withheld) re-derived a matching solution.

*Also touches: processes, locks, shared-memory, race-conditions*
