import eulerutils as eu
import itertools

"""
Find the smallest prime which, by replacing part of the number (not necessarily adjacent str_digits) with the same digit,
is part of an eight prime value family.

12,345,678

# try replacing 2 of the str_digits, 3 of the str_digits, 4 of the str_digits with the same digit

"""

def does_family_have_n_primes(familySet, n):
    global primes
    count = 0
    for p in familySet:
        if p in primes:
            count += 1
    if count >= n:
        return True
    return False


# eightdigitprimes = eu.primes.all_n_digit_primes(8)
# print("There are {} 8 digit primes".format(len(eightdigitprimes)))
maxn = 1000000
# we use primes for primality testing so it should contain all primes below the max
primes = eu.primes.all_primes_between(2,maxn)
print("There are {} primes".format(len(primes)))

#digitsSet = {0,1,2,3,4,5,6,7}
familySet = set()
found = False
for prime in primes:
    if found:
        break
    d = eu.number.num_digits(prime)
    digits = range(0,d)
    # check substituting one
    for i in digits:
        familySet.clear()
        low = 0
        if i == 0:
            low = 1
        for replacewith in range(low, 10):
            newNum = eu.numtext.replace_one_digit(prime,i,replacewith)
            familySet.add(newNum)

        sortedFamilyList = sorted(familySet)
        if does_family_have_n_primes(sortedFamilyList, 8):
            print ("we replaced one digit {}".format(i))
            found = True
            print("A family with 8 primes is {}".format(sortedFamilyList))
            for p in sortedFamilyList:
                if p in primes:
                    print("The first prime is {}".format(p))

    # check substituting two
    for i in itertools.combinations(digits, 2):
        dig1 = i[0]
        dig2 = i[1]
        familySet.clear()
        low = 0
        if dig1 == 0:
            low = 1
        for replacewith in range(low, 10):
            familySet.add(eu.numtext.replace_two_digits(prime,dig1,dig2,replacewith))

        sortedFamilyList = sorted(familySet)
        if does_family_have_n_primes(sortedFamilyList, 8):
            print ("we replaced two str_digits {} and {}".format(dig1,dig2))
            found = True
            print("A family with 8 primes is {}".format(sortedFamilyList))
            for p in sortedFamilyList:
                if p in primes:
                    print("The first prime is {}".format(p))

    # check substituting three
    for i in itertools.combinations(digits, 3):
        dig1 = i[0]
        dig2 = i[1]
        dig3 = i[2]
        familySet.clear()
        low = 0
        if dig1 == 0:
            low = 1
        for replacewith in range(low, 10):
            familySet.add(eu.numtext.replace_three_digits(prime,dig1,dig2,dig3,replacewith))

        sortedFamilyList = sorted(familySet)
        if does_family_have_n_primes(sortedFamilyList, 8):
            print ("we replaced three str_digits {} and {} and {}".format(dig1,dig2,dig3))
            found = True
            print("A family with 8 primes is {}".format(sortedFamilyList))
            for p in sortedFamilyList:
                if p in primes:
                    print("The first prime is {}".format(p))

