# osc-exam

By Lucas Hanson

## Exam answers

### clab

#### part a - clab

Since calling `malloc` with some size only tries to allocate the memory some problems can occur.\
First: `malloc` might not be able to allocate the memory, in which case it returns `NULL`.\
Second: since the queue has pointers to `head` and `tail` and counter `elems` they need to be initialized before returning the queue. This is why `NULL` checking the allocation mentioned before is important.

#### part b - clab

First it checks if they queue is `NULL` already, in which case it just returns.
If this was not done it would create problems when starting to loop over something that has not been initialized\
Then a loop starts from the `head`.
First it points the `cur` pointer to the `head` element.
Then it updates the `head` to the next element.
Then it can free the `cur` value and the element itself.
This is repeated until the `head` is `NULL`.\
If the loop was not used then when free the queue all the elements would still be filling up the memory.\
Then the queues `elems` is set to `0` and the queue itself is freed.

---

### asmlab

#### part a - asmlab

First I made the objectdump file and tried to look and the different functions.
Then I ran `gdb` and ran 
Whenever running gdb I always ensured to set breakpoints on `explode_bomb` and the phase I wanted to defuse which specifically was `phase_4` in this case.

---

### Logic

#### part a - logic

Since the logic diagram needs a and b or b and c to be true all of the following boolean expressions are equivalent:

[x] a fits\
[ ] b does not fit\
[x] c fits\
[x] d fits

#### part b - logic

The following entries fits:

[x] a fits\
[x] b fits\
[x] c fits\
[ ] d does not fit

---

### Assembly

#### part a - assembly

D = 1, S = 3
| irmovq $D, %rdi | rdi = 1 |
| --- | --- |
| irmovq $S, %rsi | rsi = 3 |
| irmovq two, %rax | rax = two |
| mrmovq 0(%rax), %rax | rax = 2 |
| main | |
| addq %rdi, %rax | rax = 3 |
| addq %rax, %rax | rax = 6 |
| subq %rdi, %rsi | rsi = -2 |
| je done | false |

1. 30
2. 44
3. Undefined behavior

#### part b - assembly

| Cycle | F | D | E | M | W |
| --- | --- | --- | --- | --- | --- |
| 1 | [0] | | | | |
| 2 | [1] | [0] | | | |
| 3 | [2] | [1] | [0] | | |
| 4 | [3] | [2] | [1] | [0] | |
| 5 | | [3] | [2] | [1] | [0] |
| 6 | | | [3] | [2] | [1] |
| 7 | | | | [3] | [2] |
| 8 | [4] | | | | [3] |
| 9 | | [4] | | | |
| A | | | [4] | | |
| B | | | | [4] | |
| C | [5] | | | | [4] |
| D | [6] | [5] | | | |
| E | | [6] | [5] | | |
| F | | | [6] | [5] | |

TODO: Fix the thing

### Locality

#### part a - locality

src: has spatial locality as it is reading from the array in order\
dst: does not use locality as when j is incremented jumps reads from index 92 and then 82 if dim start as 10 and i starts as 2.\
i: has temporal locality as it is reading from the same index multiple times.

#### part b - locality

i=0 uses temporal locality as `i` has been declared just above.\
j++ uses temporal locality as `j` either just been defined or it has just been incremented.\
inner loop body uses uses both types as described above.

### Caching

#### part a - caching

[x] a is\
[ ] b is\
[x] c is something that trashing leads to\
[x] d is

#### part b - caching

[x] ...  a read from an address gives you its most up-to-date value.\
[ ] ...  data in the cache can be accessed in a coherent way.\
[ ] ...  contents of the cache is consistent with what is contained in memory.

### Memory

#### part a - memory

[ ] a is not correct as I do not know\
[ ] b is not correct as I do not know\
[x] c is correct. Also dereferencing a NULL pointer can lead to a segmentation fault (but could be defined as undefined behaviour).

#### part b - memory

[ ] Weird question\
[x] Since all programs can amp to the same library it is easier to share code between processes.\
[ ] They very well could but it is not a guarantee.\
[x] as the processes can map to the same library and do not need to load a copy into their own virtual memory space. Thus reducing the memory usage.

### I/O

#### part a - i/o

[ ] 
