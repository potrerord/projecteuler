####    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
####
####    7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
####
####    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
####
####    (Correct answer: 23514624000)


##      Attempt #3: I think i can do it even shorter:

print()
print('This program will return the greatest product from 13 adjacent digits in a string.')
print()
num = input('Enter a string of at least 13 digits: ')
print()

max_product = 0

for start in range(len(num) - 12):
    product = 1
    for i in range(start, start + 13):
        product *= int(num[i])
        max_product = max(max_product, product)

print('The greatest product of 13 adjacent digits in this string is:')
print(max_product)
print()
    


##      Attempt #2: That last attempt worked but I'm looking at other answers and I think i can do this way faster:


    ##print()
    ##print('This program will return the greatest product from 13 adjacent digits in a string.')
    ##print()
    ##num = input('Enter a string of at least 13 digits: ')
    ##print()
    ##
    ##max_product = 0
    ##
    ##start = 0
    ##while start <= len(num) - 13:
    ##    product = 1
    ##    for i in range(start, start + 13):
    ##        product *= int(num[i])
    ##        if product > max_product:
    ##            max_product = product
    ##    start += 1
    ##
    ##print('The greatest product of 13 adjacent digits in this string is:')
    ##print(max_product)
    ##print()

##      Nice - much more elegant solution than defining multiple functions.


##      Attempt #1: Gonna try doing a function that accepts a list of integers and a starting position to create a list of 13,
##      then use that list of 13 to get the product and enter into a variable if it's larger than the previous result, then
##      return that variable.

    ##def list_13(total, start):            # Defining a function to take a number and a starting position
    ##    list_13 = []
    ##    if len(total) < 13:
    ##        print('Error: need at least 13 digits to create a list of 13 digits.')
    ##    else:
    ##        i = int(start)
    ##        for _ in range(13):
    ##            a = int(total[i])
    ##            list_13.append(a)
    ##            i += 1
    ##    return list_13
    ##
    ##def list_product(x):
    ##    list_product = 1
    ##    for i in x:
    ##        list_product *= i
    ##    return list_product
    ##
    ##print()
    ##print('This program will find the greatest product from 13 adjacent digits in an integer of any amount of digits greater than 13.')
    ##print()
    ##total = input('Enter an integer with at least 13 digits: ')
    ##start = 0
    ##greatest_product = 0
    ##
    ##while start <= len(total) - 13:
    ##    current_list = list_13(total, start)
    ##    if list_product(current_list) > greatest_product:
    ##        best_position = start
    ##        best_list = current_list
    ##        greatest_product = list_product(current_list)
    ##    start += 1
    ##
    ##print()
    ##print('Starting from position ' + str(best_position) + ', the thirteen adjacent digits with the greatest product are: ' + str(best_list))
    ##print('The product of these adjacent digits is ' + str(greatest_product) + '.')
    ##print()
