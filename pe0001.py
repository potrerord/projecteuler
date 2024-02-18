"""
If we list all the natural numbers below 10 that are multiples of 3 or 
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution: 233168
"""


def main():
    """Use defined functions in the context of the problem."""

    answer = sum_multiples_of(1000, 3, 5)
    print(answer)


def sum_multiples_of(upper_bound: int, *args: int) -> int:
    """Return the sum of all multiples of args.
    
    Usage: sum_multiples_of(upper bound not inclusive, any integers)
    """

    # Initialize sum.
    total_sum = 0

    # Iterate up to upper bound (not inclusive).
    for num in range(upper_bound):

        # Reset flag to exit multiple check.
        flag = False

        # Iterate through all integers in argument.
        for arg in args:

            # If the number is a multiple of arg, add it to the sum.
            if num % arg == 0:
                total_sum += num

                # Mark flag as true if number got counted.
                flag = True
            
            # Don't count num more than once.
            if flag:
                break

    return total_sum


if __name__ == "__main__":
    main()
