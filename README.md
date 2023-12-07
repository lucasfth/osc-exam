# osc-exam

By Lucas Hanson

## Exam answers

### clab

#### part a - clab

Since calling `malloc` with some size only tries to allocate the memory a big problem can occur later.\
If someone was to try and dereference the pointers to head, tail, or elems they would get a segmentation fault as the memory has not been intialized yet.
Therefore it is important that `queue_new` checks if the allocation was successful and if it was then to initialize head, tail, and elems.\
To do this the following body is a potential solution:

```c
queue_t * queue_new(void)
{
    queue_t *q = malloc(sizeof(queue_t));
    if (q == NULL) {return NULL;}
    q->head = NULL;
    q->tail = NULL;
    q->elems = 0;
    return q;
}
```

Since the queue has pointers to `head` and `tail` and counter `elems` they need to be initialized before returning the queue.
This is why `NULL` checking the allocation mentioned before is important, as it would also cause a segmentation fault if the queue was not allocated before initializing the pointers and counter.\

#### part b - clab

First it checks if they queue is `NULL` already, in which case it just returns.
If this was not done it would create problems when starting to loop over something that does not exist.\
Then a loop starts from the `head`.
First it points the `cur` pointer to the `head` element.
Then it updates the `head` pointer to point to the next element.
Then it can free the `cur` value and the element itself.
This is repeated until the `head` is `NULL`.\
If the loop was not used then only the `queue_t` would be freed, meaning that all the elements would still be filling up the memory.
Then the queues `elems` is set to `0` (which is not needed) and the queue itself is freed.

### asmlab

#### part a - asmlab

First I made the objectdump file and tried to look and the different functions.
Then I ran `gdb` and ran 
Whenever running gdb I always ensured to set breakpoints on `explode_bomb` and the phase I wanted to defuse which specifically was `phase_4` in this case.

#### part b - asmlab

### prflab

#### part a - prflab

I used my previous `my_rotate` function and put it into `rotate_thread` which was modified to only operate on specified columns.
Originally I then created dim many threads and then gave them a single column each to rotate.
This turned out to be extremely inefficient as it costs to much to create and join the threads.\
I then created four threads (this is done in `my_rotate_t`) and gave them a quarter of the columns to rotate each (which will be done in `rotate_thread`).
This turned out to be much more efficient as each thread would have a one fourth of work to do (compared to `my_rotate`) and the cost of creating and joining the threads was not as big of a factor.
The way I ensured to split up the work equally was by first calculating what a fourth of dim was by doing bit shifting (as this is only calculated once it does not matter much in terms of efficiency).
Then I gave each `rotate_thread` a struct defining the start index, `j`, and then how many rows to rotate, `limit`.
They would then only operate on the specified columns but still run through all the rows.\
Another potential optimization I could have done was to instead make each thread run through all the columns but specify which rows to make the operations on.

#### part b - prflab

### syslab

#### part a - syslab

I made the function `handle_request` the thread function.
This was done as it was an easier implementation as the call to `accept` is blocking until a connection is made.
Then when a connection was made it will then start at thread which will be responsible for the rest of the commonication between the client and the server (if the website is not cached).
By doing it this way whenever a connection is made the main thread is never blocked and can continue to wait for new connections, as soon as it has spawned the new thread.

#### part b - syslab

My cachin, `Cache`, works by having a double linked list consisting of `Node`s where the head and tail nodes are also known.
Furthermore a dictionary, `Table`, is also used to get instant access when trying to access a single node in the cache.\
The way I operate with it is that I lock the cache (not the dictionary nor the nodes themselves) when setting in a new node.
If the cache is full then the head is removed.
Regardless I will set in the new node (except if it is to big).\
When I try to read a value I go through the dictionary to access the node (if it does not exist it just returns `NULL`).
I then start a thread which will lock and move the accessed node to the tail.
Then I can return the node without waiting for the cache to be rearranged.\
By doing it this way I ensure that no two threads are rearranging the cache simultaneously and that the nodes can still be accessed.

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
| 5 | [4] | [3] | [2] | [1] | [0] |
| 6 | [5] | [4] | [3] | [2] | [1] |
| 7 | [6] | [5] | [4] | [3] | [2] |
| 8 | [7] | [6] | [5] | [4] | [3] |
| 9 | [8] | [7] | [6] | [5] | [4] |
| A | [4] | [8] | [7] | [6] | [5] |
| B | [5] | [4] | [8] | [7] | [6] |
| C | [6] | [5] | [4] | [8] | [7] |
| D | [7] | [6] | [5] | [4] | [8] |
| E | [8] | [7] | [6] | [5] | [4] |
| F | [4] | [8] | [7] | [6] | [5] |

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
[ ] d is

#### part b - caching

[ ] ...  a read from an address gives you its most up-to-date value.\
[x] ...  data in the cache can be accessed in a coherent way.\
[ ] ...  contents of the cache is consistent with what is contained in memory.

### Memory

#### part a - memory

[ ] a is not correct as I do not know\
[ ] b is not correct as I do not know\
[x] c is correct. Also dereferencing a NULL pointer can lead to a segmentation fault (but could be defined as undefined behaviour).

#### part b - memory

[ ] Weird question\
[x] Since all programs can use to the same library it is easier to share code between processes.\
[ ] They very well could but it is not a guarantee.\
[x] as the processes can map to the same library and do not need to load a copy into their own virtual memory space. Thus reducing the memory usage.

### I/O

#### part a - i/o

[ ] Seems to be something regarding pipelining (SEQ+)\
[ ] Could not find a mention\
[ ] It does not give control from one user process to another\
[ ] CPU Disk controller give me data from here. Disk controller write to main memory. Disk controller to CPU hey I am done. (so no)\
[x] Yes.

#### part b - i/o

[ ] \
[ ] maybe\
[ ]

### Concurrency

#### part a - concurrency

[ ] Max was 18\
[x] Was one of the result when I ran the program\
[x] Was the only result when I can the program cool\
[x] Was one of the result when I ran the program\
[x] Was one of the result when I ran the program

#### part b - concurrency

[ ] is not updated by thread\
[x] is global and updated by thread\
[x] is global and updated by thread\
[ ] tk is not global\
[ ] mutex a mutex???

### Miscellaneous

#### part a - miscellaneous

[x] is correct since the compiler may not even have full access to function calls. The function called may also have side effects and dependencies which is not obvious for the compiler.\
[ ] it can if done manually\
[ ] nope

#### part b - miscellaneous

[x] plausible if p2 does not have direct acces and memory protection is in place\
[x] plausible if memory protection is not in place\
[ ] \
[x] can also happen

### part c - miscellaneous

[ ]\
[x] I heard the word context switch\
[ ]

### part d - miscellaneous

[ ]\
[ ]\
[ ]

### part e - miscellaneous

[ ]\
[ ]\
[ ]
