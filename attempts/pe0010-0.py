####        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
####
####        Find the sum of all the primes below two million.


##      Attempt 1: Just gonna use my prime function from earlier for this.

print()

# Define function to find primes:

def is_prime(x):
    factors = []
    if x > 2:
        i = 2
        while i <= x**0.5:
            if x % i == 0:
                return False
                break
            else:
                i += 1
        return True
    elif x == 1:
        return False
    elif x == 2:
        return True

# Actual code:

primes = []
i = 1
primes_sum = 0

n = int(input("Enter a value n to get the sum of all primes below n: "))

while i < n:
    if is_prime(i):
        primes_sum += i
        i += 1
    else:
        i += 1

print("The sum of all primes below " + str(n) + "is:")
print(primes_sum)
