# Simple Hash Function Demonstration

This program uses the modulo operator to
create the simple hash function,

  H(k) = k mod m

for demonstrating how hash functions work.

The small fixed size of the hashes demonstrates
collisions.

This explains why an inverse function of H(k) 
can't exist; A hash cannot be mapped back to the 
original input because multiple inputs can generate
that same hash.

---
    Sample Output:

    Hash Function: H(k) = k mod m
    Hash Size (m): 4
    Sample Size  : 10

    O-----------------------------------O
    | Input: k | Hash: H(k) | Collision |
    |-----------------------------------|
    |       49 |          1 |           |
    |       83 |          3 |           |
    |       70 |          2 |           |
    |       98 |          2 |     X     |
    |       28 |          0 |           |
    |       12 |          0 |     X     |
    |        7 |          3 |     X     |
    |       25 |          1 |     X     |
    |       33 |          1 |     X     |
    |       22 |          2 |     X     |
    O-----------------------------------O
