"""
2024-02-21-wed
Anthony Narag
Project Euler Problem 16
pe0016-find_power_patterns.py

Goal:
The final digit of powers of 2 cycle through {2, 4, 8, 6} -- I'm trying
to find repeatable behavior in the final two digits of powers of two.

Result:
Looks like 2^22 is where the repeats begin.
"""
import math
import sys

# The base of the power.
POWER_BASE: int = 2

# The highest exponent being tested.
EXP_HIGH: int = 63

# The number of final digits to log from each power.
FINAL_DIGIT_COUNT: int = 2

# Amount of characters for rjust when printing.
RIGHT_ALIGN: int = 6


def main() -> None:
    print("Note - max system int:")
    print(f"2^{int(math.log2(sys.maxsize)) + 1} - 1")
    print()

    # List of powers of constant base.
    powers_list: list[int] = make_first_powers_list(POWER_BASE, EXP_HIGH)

    # List of final digits from powers.
    final_digits_list: list[int] = make_final_digits_list(
        powers_list, FINAL_DIGIT_COUNT)

    # Print repeats.
    i: int
    for i in range(len(final_digits_list)):
        # Print a separator if a repeat is found.
        for j in range(FINAL_DIGIT_COUNT + 1):
            if final_digits_list[i] == final_digits_list[j]:
                print(f"---- pattern: 2^{j} ----")

        # Print the base and exponent.
        print(f"{POWER_BASE}^{i}: ".rjust(RIGHT_ALIGN), end="")

        # Print the final digits in the same line.
        print(f"{final_digits_list[i]}".rjust(FINAL_DIGIT_COUNT))


def make_final_digits_list(int_list: list[int],
                           digit_count: int,
                           base: int = 10) -> list[int]:
    """Return a list of the final x digits from each int in a given
    list.

    @param int_list    the list containing numbers to parse
    @param digit_count the number of final digits
    @param base        the number representation base, default 10

    @return a list of integers containing the final digits
    """

    final_digits_list: list[int] = []

    number: int
    for number in int_list:
        final_digits_list.append(get_final_digits(
            number, digit_count, base))

    return final_digits_list


def make_first_powers_list(base: int, exp_max: int) -> list[int]:
    """Return a list of the first x powers of an integer base, starting
    from base^0.

    @param base    the base of the powers in the list
    @param exp_max the final exponent in the list

    @return a list of integers containing the powers
    """

    powers_list: list[int] = []

    exp: int
    for exp in range(exp_max + 1):
        powers_list.append(base ** exp)

    return powers_list


def get_final_digits(num: int, digit_count: int, base: int = 10) -> int:
    """Get the final x digits from an int num.

    @param num         the num in question
    @param digit_count the amount of final digits to get
    @param base        the number representation base, default 10

    @return an int containing the final digits from the num.
    """

    return num % (base ** digit_count)


if __name__ == "__main__":
    main()
