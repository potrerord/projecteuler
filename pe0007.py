####        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
####
####        What is the 10 001st prime number?



####        Attempt #1: just gonna refine my is_prime() function and make a list of primes, hopefully it can handle 10001 of them lol.

def is_prime(x):
    factors = []
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x > 2:
        i = 2
        while i <= x**0.5:
            if x % i == 0:
                return False
                break
            else:
                i += 1
        return True


primes = []
i = 1

print()
n = int(input("Enter a value n to get the nth prime: "))

while len(primes) < n:
    if is_prime(i):
        primes.append(i)
        i += 1
    else:
        i += 1

print(primes[n - 1])
