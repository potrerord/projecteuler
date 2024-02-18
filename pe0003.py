"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Solution: 6857

NOTE: FACTORS FUNCTION IS BROKEN SOMEHOW
"""

from math import ceil
from typing import List


def main():
    """Call defined functions in the context of the problem."""

    # Get user input.
    num = int(input("Enter a number: "))

    print()
    print(f"The factors of {num} are:")
    print(factors(num))
    print()
    print(f"The prime factors of {num} are:")
    print(prime_factors(num))
    print()


# FIX
def factors(num: int) -> List[int]:
    """NOTE: BROKEN
    
    Return a list of all factors of num.
    """

    # Initialize empty factor set.
    factor_set = set()

    # Duplicate argument num into a range to be checked and changed.
    check_range = num
    
    # Initialize potential factors.
    potential_factor = 1

    # Loop up until factor meets range, inclusive to catch square roots.
    while potential_factor <= check_range:
        # If potential_factor is indeed a factor, add it to the list.
        if num % potential_factor == 0:
            factor_set.add(potential_factor)

            # Also add the corresponding factor pair.
            factor_set.add(int(num / potential_factor))

            # Also lower range to the higher factor in the pair.
            check_range /= potential_factor
        
        # Increment factor.
        potential_factor += 1

    # Convert and sort factor list before returning.
    factor_list = list(factor_set)
    factor_list.sort()

    return factor_list


def is_prime(num: int) -> bool:
    """Check if a number is prime."""

    # Limit the factor check up to just higher than the sqrt of num.
    factor_limit = ceil(num ** 0.5) + 1

    # Iterate through all integerss from 2 to the factor limit.
    for potential_factor in range (2, factor_limit):
        # If a factor is found, it's not prime.
        if num % potential_factor == 0:
            return False

    # If it makes it out of that loop, it's prime.
    return True


def prime_factors(num: int) -> List[int]:
    """Return a list of prime factors of num."""

    # Initialize prime factors list.
    prime_factors = []

    # Call factors() and iterate through list.
    for factor in factors(num):

        # Call is_prime() to check factor. Add to list if prime.
        if is_prime(factor):
            prime_factors.append(factor)

    return prime_factors


if __name__ == "__main__":
    main()
