# osc-exam

By Lucas Hanson

## Exam answers

### clab

#### part a

Since calling `malloc` with some size only tries to allocate the memory some problems can occur.\
First: `malloc` might not be able to allocate the memory, in which case it returns `NULL`.\
Second: since the queue has pointers to `head` and `tail` and counter `elems` they need to be initialized before returning the queue. This is why `NULL` checking the allocation mentioned before is important.

#### part b

First it checks if they queue is `NULL` already, in which case it just returns.
If this was not done it would create problems when starting to loop over something that has not been initialized\
Then a loop starts from the `head`.
First it points the `cur` pointer to the `head` element.
Then it updates the `head` to the next element.
Then it can free the `cur` value and the element itself.
This is repeated until the `head` is `NULL`.\
If the loop was not used then when free the queue all the elements would still be filling up the memory.\
Then the queues `elems` is set to `0` and the queue itself is freed.

### asmlab

#### part a

First I made the objectdump file and tried to look and the different function.
I 
Whenever running gdb I always ensured to set breakpoints on `explode_bomb` and the phase I wanted to defuse which specifically was `phase_4` in this case.

### Logic

#### part a

Since the logic diagram needs a and b or b and c to be true all of the following boolean expressions are equivalent:

1. a fits
2. b does not fit
3. c fits
4. d fits

#### part b

The following entries fits:

1. a fits
2. b fits
3. c fits
4. d does not fit
