##    The prime factors of 13195 are 5, 7, 13 and 29.
##
##    What is the largest prime factor of the number 600851475143 ?
##
    

def factors(x):
    factor_list = []
    maximum = x
    i = 1
    while i < x:
        if maximum % i == 0:
            factor_list.append(i)
            factor_list.append(int(x / i))
            x /= i
            i += 1
        else:
            i += 1
    factor_list.sort()
    return factor_list

def is_prime(x):
    factor_list = []
    for i in range (1, x+1):
        if x % i == 0:
            factor_list.append(i)
            if len(factor_list) > 2:
                return False
                break
    if len(factor_list) == 2:
        return True

print()

num = int(input("Enter a number: "))
prime_factors = []

for i in factors(num):
    if is_prime(i):
        prime_factors.append(i)

print()
print("The factors of " + str(num) + " are:")
print(factors(num))
print()
print("The prime factors of " + str(num) + " are:")
print(prime_factors)






