# osc-exam

By Lucas Hanson

## Table of contents

* [clab](#clab)
* [asmlab](#asmlab)
* [prflab](#prflab)
* [syslab](#syslab)
* [Logic](#logic)
* [Assembly](#assembly)
* [Locality](#locality)
* [Caching](#caching)
* [Memory](#memory)
* [I/O](#io)
* [Concurrency](#concurrency)
* [Miscellaneous](#miscellaneous)

## Exam answers

### clab

#### part a - clab

Since calling `malloc` with some size only tries to allocate the memory a big problem can occur later.\
If someone was to try and dereference the pointers to head, tail, or elems they would get a segmentation fault as the memory has not been initialized yet.
Therefore it is important that `queue_new` checks if the allocation was successful and if it was then initialize head, tail, and elems.\
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

First, it checks if the queue is `NULL` already, in which case it just returns.
If this was not done it would create problems when starting to loop over something that does not exist.\
Then a loop starts from the `head`.
First, it points the `cur` pointer to the `head` element.
Then it updates the `head` pointer to point to the next element.
Then it can free the `cur` value and the element itself.
This is repeated until the `head` is `NULL`.\
If the loop was not used then only the `queue_t` would be freed, meaning that all the elements would still be filling up the memory.
Then the queue `elems` is set to `0` (which is not needed) and the queue itself is freed.

### asmlab

#### part a - asmlab

First I made the objectdump file and tried to look and the different functions.
I quickly identified the function `explode_bomb` and each of the different phases.
Then I ran `gdb` and ensured to set a breakpoint on `explode_bomb` and `phase_3`.
Then when I got to input the string for phase 3 I gave a random string initially and I could then run disas.\
I then went down to `__isoc99_sscanf@plt` with the `nexti`.
When I then ran `x/10c $rsi` and `x/s $rsi` I could see that the input needed was probably two integers.
I then started over again and gave the inputs `2` and `10`.
This proved to be quite a lucky choice since at `0x00005555555566e9` and `0x00005555555566ec` it compares the number of values stored at $eax which was 2 and then if 1 was less or equal to that it would jump to the bomb.
Then the two next operations check if my first value is 7 or above.
If it is then it will jump to the bomb.
Then on `0x0000555555556739` and `0x000055555555673d` it checks if five is greater than my first value, and if so it jumps to a bomb.
Then I checked what was on $eax before instruction `0x000055555555673f`.
It was 390.
Which means that if the first value is two then the second value has to be 390.
But due to how operations `0x0000555555556706` and `0x0000555555556709` work the second value will be another value based on the first value.\
The possible solutions are:

* 1 334
* 2 390
* 3 -553
* 4 0
* 5 -553

This was figured out by using `disas`, `i r` and `ni` a lot.

#### part b - asmlab

In phase two I checked out the gadgets in r_target.
I ended up identifying a call to 58 which pops from the top of the stack to $rax.

### prflab

#### part a - prflab

I used my previous `my_rotate` function and put it into `rotate_thread` which was modified to only operate on specified columns.
Originally I created dim many threads and then gave them a single column each to rotate.
This turned out to be extremely inefficient as it costs too much to create and join the threads.\
I then created four threads (this is done in `my_rotate_t`) and gave them a quarter of the columns to rotate each (which will be done in `rotate_thread`).
This turned out to be much more efficient as each thread would have one-fourth of the work to do (compared to `my_rotate`) and the cost of creating and joining the threads was not as big of a factor.
The way I ensured to split up the work equally was by first calculating what a fourth of dim was by doing bit shifting (as this is only calculated once it does not matter much in terms of efficiency).
Then I gave each `rotate_thread` a struct defining the start index, `j`, and then how many rows to rotate, `limit`.
They would then only operate on the specified columns but still run through all the rows.\
Another potential optimization I could have done was to make each thread run through all the columns but specify which rows to make the operations on.

This is what each of the pthread functions do (the ones I used):

* `pthread_t` defines the thread or in my case a list of threads.
* `thread_create` is used to create each of the threads and also defines which function the thread should run and which struct it should give as argument.
* `thread_join` is used to wait for all the threads to finish.

#### part b - prflab

Vecorization could potentially benefit `rotate_t`.
But due to the cost of loading the pixels into vectors, and the complexity of the rotate itself it would probably not be worth it since we already use resources on spinningg up threads.\
It could be done by rotating the upper left 4*4 pixels with vectorization and then store it at the bottom right.
This would essentially enable rotating multiple 4*4 pixels concurrently.\
But if the number of threads are not made to be a number less than four it does not make sense to make it vectorized.

Multithreading could potentially benefit `blend_v`.
This could be done by dividing the work into e.g. four parts and then letting each thread blend.
This would allow blending 16 pixels concurrently.\
But for the current image sizes it does not make sense.
So it would only make sense if the images were much larger.

### syslab

#### part a - syslab

I made the function `handle_request` the thread function.
This was done as it was an easier implementation as the call to `accept` is blocked until a connection is made.
Then when a connection is made it will start a thread which will be responsible for the rest of the communication between the client and the server (if the website is not cached).
By doing it this way whenever a connection is made the main thread is never blocked and can continue to wait for new connections, as soon as it has spawned the new thread.

#### part b - syslab

My cachin, `Cache`, works by having a double linked list consisting of `Node`s where the head and tail nodes are also known.
Furthermore a dictionary, `Table`, is also used to get instant access when trying to access a single node in the cache.\
The way I operate with it is that I lock the cache (not the dictionary nor the nodes themselves) when setting in a new node.
If the cache is full then the head is removed.
Regardless I will set in the new node (except if it is too big).\
When I try to read a value I go through the dictionary to access the node (if it does not exist it just returns `NULL`).
I then start a thread that will lock and move the accessed node to the tail.
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
| 6 | [4] | [3] | [ ] | [2] | [1] |
| 7 | [4] | [3] | [ ] | [ ] | [2] |
| 8 | [4] | [3] | [ ] | [ ] | [ ] |
| 9 | [5] | [4] | [3] | [ ] | [ ] |
| A | [5] | [4] | [ ] | [3] | [ ] |
| B | [5] | [4] | [ ] | [ ] | [3] |
| C | [5] | [4] | [ ] | [ ] | [ ] |
| D | [6] | [5] | [4] | [ ] | [ ] |
| E | [6] | [5] | [ ] | [4] | [ ] |
| F | [6] | [5] | [ ] | [ ] | [4] |

### Locality

#### part a - locality

src: has spatial locality as it is reading from the array in order\
dst: does not use locality as when j is incremented it jumps from index 92 to 82 if dim starts as 10 and i starts as 2.\
i: has temporal locality as it is reading from the same index multiple times.

#### part b - locality

i=0 uses temporal locality as `i` has been declared just above.\
j++ uses temporal locality as `j` either just been defined or has just been incremented.\
inner loop body uses both types as described in part a.

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
[x] c is correct. Also dereferencing a NULL pointer can lead to a segmentation fault (but could be defined as undefined behavior).

#### part b - memory

[ ] Weird question\
[x] Since all programs can use to the same library it is easier to share code between processes.\
[ ] They very well could but it is not a guarantee.\
[x] as the processes can map to the same library and do not need to load a copy into their own virtual memory space. Thus reducing memory usage.

### I/O

#### part a - i/o

[x] [https://arc.net/l/quote/tpxyznil](https://arc.net/l/quote/tpxyznil) \
[x] Could not find a mention\
[ ] It does not give control from one user process to another\
[ ] CPU Disk controller gives me data from here. Disk controller writes to main memory. Disk controller to CPU hey I am done. (so no)\
[ ] It would either have to be disk controller over disk drive.

#### part b - i/o

[ ] \
[ ] maybe\
[ ]

### Concurrency

#### part a - concurrency

[ ] Max was 18\
[x] Was one of the results when I ran the program\
[x] Was the only result when I can the program cool\
[x] Was one of the results when I ran the program\
[x] Was one of the results when I ran the program

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

[ ] Memory protection should make ensure this does not happen\
[x] plausible if memory protection is not in place\
[ ] what?\
[x] can also happen if shared memory is used

### part c - miscellaneous

[ ]\
[x] I heard the word context switch\
[ ]

### part d - miscellaneous

[ ]\
[x]\
[ ]

### part e - miscellaneous

[ ]\
[ ]\
[x]
