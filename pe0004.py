"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""


"""
Attempt #1:
  - testing all products of 3 digit numbers to see if they're
    palindromes.
  - next try will prob be test all 5/6 digit palindromes to see if
    they are products of 3 digit numbers
"""


largest_pal_product = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        product = int(x * y)
        product_str = str(product)
        if all(product_str[i] == product_str[-i-1] for i in range(int(len(product_str)/2))) and product > largest_pal_product:
            final_x = x
            final_y = y
            largest_pal_product = product

print()
print("The largest palindromic product from two 3-digit numbers is " + str(largest_pal_product) + ".")
print()
print("Those two 3-digit factors are " + str(final_x) + " and " + str(final_y) + ".")
            
                
        

