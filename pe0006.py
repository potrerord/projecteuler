##        The sum of the squares of the first ten natural numbers is,
##
##        1^2 + 2^2 + ... + 10^2 = 385
##
##        The square of the sum of the first ten natural numbers is,
##
##        (1 + 2 + ... + 10)^2 = 55^2 = 3025
##
##
##        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
##        3025 − 385 = 2640.
##
##        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
##



##          Attempt #1: Gonna just make a function to do sum of squares, function for square of sum (easy) and subtract I guess

def square_of_sum_from_range(lower, upper):
    all_list = []
    for i in range (lower, upper + 1):
        all_list.append(i)
    all_sum = sum(all_list)
    square_of_sum = all_sum**2
    return square_of_sum

def sum_of_squares_from_range(lower, upper):
    all_list = []
    for i in range (lower, upper + 1):
        all_list.append(i**2)
    sum_of_squares = sum(all_list)
    return sum_of_squares




x = int(input("Enter a lower bound (inclusive): "))
y = int(input("Enter an upper bound (inclusive): "))
print()
print("The square of the sum is:")
print(square_of_sum_from_range(x,y))
print()
print("The sum of the squares is:")
print(sum_of_squares_from_range(x,y))
print()
print("The difference between the square of the sum and the sum of the squares is:")
print(str(square_of_sum_from_range(x,y)) + " - " + str(sum_of_squares_from_range(x,y)) + " = " + str(square_of_sum_from_range(x,y) - sum_of_squares_from_range(x,y)))
