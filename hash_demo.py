"""
Hash Function Demonstration
Richard Ignacio
---------------------------------------------
This program uses the modulo operator to
create the simple hash function,

    H(k) = k mod m

for demonstrating how hash functions work.
"""

import random

"""Fixed size of unique hash values"""
SIZE = 4

"""Sample size of unique input values"""
N = 10

"""Minimum and maximum values of the inputs"""
MIN = 0
MAX = 100


def hash_mod(k):
    """Simple modulo hashing function"""
    return k % SIZE


def main():
    """Calculate hashes for N number of unique random inputs between MIN and MAX"""
    dup = []  # Track duplicate inputs
    hys = []  # Track collisions
    cnt = 0

    print()
    print("Hash Function: H(k) = k mod m")
    print(f"Hash Size (m): {SIZE}")
    print(f"Sample Size  : {N}")
    print()

    print("O-----------------------------------O")
    print("| Input: k | Hash: H(k) | Collision |")
    print("|-----------------------------------|")
    while cnt < N:
        y = random.randint(MIN, MAX)

        while y in dup:
            y = random.randint(MIN, MAX)

        dup.append(y)
        hy = hash_mod(y)

        col = '    X' if hy in hys else ''
        print(f"| {y:8} | {hy:10} | {col:9} |")

        hys.append(hy)
        cnt += 1

    print(f"O-----------------------------------O")


if __name__ == '__main__':
    main()
