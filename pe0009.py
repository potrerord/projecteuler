####    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
####
####    a^2 + b^2 = c^2
####    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
####
####    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
####    Find the product abc.
####
####
####
####    Answer: 200, 375, 425 -> 

## Step 0: New line, import math

print()
import math
import sys
import time
start_time = time.time()

## Attempt #2: realized the pre-generated list isn't gonna work bc I read the problem wrong lmao

c = 1

while True:
    lower_eq = math.ceil((c**2 - (c - 1)**2) ** 0.5)
    upper_neq = math.ceil(math.ceil(c**2 / 2) ** 0.5)

    for a in range(lower_eq, upper_neq):
            b_2 = c**2 - a**2
            
            if b_2 ** 0.5 % 1 == 0:
                b = int(b_2 ** 0.5)
                abc_sum = a + b + c
                if abc_sum == 1000:
                    abc_prod = a * b * c
                    print(a)
                    print(b)
                    print(c)
                    print()
                    print("abc = " + str(abc_prod))     
                    print((time.time() - start_time))           # ~0.18 seconds!
                    sys.exit()
    
    c += 1
    






####            Attempt #1:
####
####
####            ## Step 1: Generate list of Pythagorean triplets.
####
####            ## a) get list of squares and roots.
####
####            roots = []
####            squares = []
####            x = 1
####
####            while x**2 < 1000:
####                roots.append(x)
####                squares.append(x**2)
####                x += 1
####                
####            print("roots = ", roots)
####            print()
####            print("squares = ", squares)
####            print()
####
####            ## b) Test each square for Pythagorean triples.
####
####            h = 0
####            for c2 in squares:
####                lower = c2 - h
####                upper = math.ceil(c2 / 2)
####                for a2 in squares:
####                    if a2 < lower or a2 >= upper:
####                        continue
####                    else:
####                        b2 = c2 - a2
####                        if b2 ** .5 % 1 == 0:
####                            print(int(a2 ** .5))
####                            print(int(b2 ** .5))
####                            print(int(c2 ** .5))
####                            print()
####                h = c2
####
####
####            ## Step 2: Find sum.
####
####
####            ## Step 3: Find product.
