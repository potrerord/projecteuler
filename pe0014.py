"""
Anthony Narag
2023-08-10-thu
03:42 PM

Attempt #1
Solution: 837799
Execution time: 50678.42ms

Attempt #2
Execution time: 48188.82ms (no print debugging)

Attempt #3
Execution time: 73233.84ms (iterating upward instead of downward)

Attempt #4
Execution time: 50644.01ms (only added lessthan number to skips)

Attempt #5
Execution time: 48504.46ms (no print debugging)
"""
"""
The following iterative sequence is defined for the set of positive
integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""

from typing import List, Set
from time import time

def main():
    """Call defined functions in the context of the problem."""

    # Initialize timer.
    start = time()

    # Update test value.
    TEST = 999999

    # Get result.
    result = longest_collatz_sequence(TEST)

    # Print report.
    print()
    print(f"longest collatz sequence starting at {TEST} or under:\n{result}\n")
    print(f"length: {len(result)}")
    print()

    # End timer and report.
    end = time()
    runtime = end - start
    print(f"Execution time: {runtime * 1000:.2f}ms\n")
    

def longest_collatz_sequence(
        highest: int,
        skips: Set[int] = set()
) -> List[int]:
    """Find the longest Collatz sequence with a starting value less than
    or equal to the "highest" parameter.

    Uses a "skips" set to skip certain integers whose sequences are
    subsequences of another already found. skips defaults to an empty
    set if no argument is entered.
    """
    
    # Initialize information about the longest sequence.
    longest_sequence = []
    longest_sequence_length = 0

    # Iterate downward through all integers starting with highest.
    for number in range(highest, 0, -1):
        # Skip any integer that has already been found in a subsequence.
        if number in skips:
            continue

        # Get sequence and update longest length if necessary.
        sequence = make_collatz_sequence(number)
        if len(sequence) > longest_sequence_length:
            longest_sequence = sequence
            longest_sequence_length = len(sequence)
        
        # Add all newly found subsequence elements to skips set.
        for element in sequence:
            if element < number:
                skips.add(element)
    
    return longest_sequence


def make_collatz_sequence(n: int) -> List[int]:
    """Return a list of integers representing each term in the sequence
    created by the function as defined in the "Collatz conjecture"
    (https://en.wikipedia.org/wiki/Collatz_conjecture):

    f(n) = { n / 2   if n is even
           { 3n + 1  if n is odd
    """

    # Initialize empty "next sequence".
    recursive_next_sequence = []

    # Skip the conversion if n is 1.
    if n != 1:
        # Convert n to a new value if even.
        if n % 2 == 0:
            new_n = int(n / 2)

        # Convert if odd.
        else:
            new_n = int(3 * n + 1)
        
        # Recursively get the sequence of the new n.
        recursive_next_sequence = make_collatz_sequence(new_n)
    
    # Begin sequence list with n.
    sequence = [n]
    if recursive_next_sequence:
        for element in recursive_next_sequence:
            sequence.append(element)
    
    return sequence


if __name__ == "__main__":
    main()
