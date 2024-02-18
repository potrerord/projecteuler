##      2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##
##      What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?




##      Attempt #1: No code needed really, just made a list of the prime factors of 1-20 and eliminated any unneccesary duplicates: answer is 232792560.
##
##print()
##print("The correct answer should be:")
##print(11*13*7*2*2*17*3*3*19*2*2*5)
##print()
##


####      Attempt #2: I'd like to make a function that can do this for any range of integers though so let's give it a go:
##
##def lcm_all(lower, upper):
##    x = int(upper)
##    lcm = x
##    for y in range(upper-1, lower, -1):
##        if lcm % y != 0:
##            lcm = int(lcm * y)
##            print(" * " + str(y))
##            print(lcm)
##        else:
##            print("scrapped: " + str(y))
##    print()
##    return lcm
##
##print()
##lower = int(input("Enter a lower bound: "))
##upper = int(input("Enter an upper bound: "))
##print()
##print("The least common multiple of all integers within those bounds, inclusive, is " + str(lcm_all(lower, upper)))
##    



####        Attempt #3: I'm not in love with the multiplying method from above because it's not really how I did on paper. Gonna try to recreate that.
####        Basically the idea is that I'm gonna break each integer down into its prime factors from the top down, and compare it to a list of necessary factors for the LCM.
####        For example: 20 has {2,2,5}, 19 has {19}, and 18 has {2,3,3}. The {2} from the 18 is unnecessary because it's covered by the {2,2,5} from the 20, so we only need to keep {3,3}.
####        At this point our LCM has {2,2,3,3,5,19}.
####        Then 17 has {17}, 16 has {2,2,2,2}. Now we actually do need {2,2,2,2,3,3,5,19} to make sure 16 is included.
####        Etc.



def lcm_from_range(lower, upper):
    from collections import Counter
    x = int(lower)
    y = int(upper)
    lcm = 1
    lcm_factors = []
    for i in range(y, x, -1):                       # Starting with upper bound (20 hypothetically) and moving down until lower bound,
        i_prime_factors = []
        while i > 1:                                # We will reduce i until it is its lowest prime factor
            j = 2
            while j <= i:                           # We will test if it's divisible by integers j starting from 2 as long as the test ints are less than or equal to the tested number
                if i % j == 0:                      # If 2 is a factor of 20,
                    i_prime_factors.append(j)       # add 2 to the list
                    i /= j                          # now 20 is 10, and keep checking starting with 2
                    j = 2
                else:
                    j += 1                          # if j is not a factor of i, then add 1 to it and keep checking until we reach i
            new_factors = list((Counter(i_prime_factors)-Counter(lcm_factors)).elements())
            lcm_factors = list((Counter(lcm_factors)+Counter(new_factors)).elements())
    for i in lcm_factors:
        lcm *= i
    return lcm



print()
lower = int(input("Enter a lower bound (inclusive): "))
upper = int(input("Enter an upper bound (inclusive): "))
print()
print("The least common multiple of all integers within those bounds is:")
print(lcm_from_range(lower, upper))
    
