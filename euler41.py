import math
import collections

# find largest pandigital prime
# let's first see if there's any 9 digit pandigital primes and take the largest of those
# there are no pandigitals greater than 9 str_digits

def num_digits(n):
    d = int(math.log10(n))+1
    return d

# pandigital use all str_digits from 1-9
# n-digit pandigital makes use of all str_digits 1 to n
def isNDigitPandigital(num, n):
    allstr = str(num)
    resultSet = set()
    noduplicates = True
    for char in allstr:
        digChar = int(char)
        if digChar in resultSet:
            noduplicates = False
        else:
            resultSet.add(digChar)
    if noduplicates:
        if not(0 in resultSet):
            if not(anyGreaterThanN(resultSet, n)):
                # we have one
                return True
    return False

def anyGreaterThanN(list, n):
    for i in list:
        if i>n:
            return True
    return False

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


lim = 999999999
resultsDict = {}
count = 0
largest = 0
noflargest = 0
for next_prime in get_primes(1):
    if next_prime < lim :
        n = num_digits(next_prime)
        if (isNDigitPandigital(next_prime, n)>0):
            count += 1
            # found a solution for p. increment dictionary counter.
            resultsDict[n] = resultsDict.get(n,0) + 1
            largest = next_prime
            noflargest = n
            print("{} is pandigital prime".format(next_prime))

print(resultsDict)
print("The largest was {} with {} str_digits".format(largest,noflargest))