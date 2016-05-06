import math
import sortedcontainers as sc
import itertools

def num_digits(n):
    d = int(math.log10(n))+1
    return d

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

def same_digits_regardless_of_length(a,b):
    if sorted(set(str(a))) == sorted(set(str(b))):
        return True
    else:
        return False

def same_digits_and_same_length(a,b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False

primes = sc.SortedList()
fourdigitprimes = []
gp = get_primes(2)
while True:
    next_prime = next(gp)
    n = num_digits(next_prime)
    if (n>4):
        break
    if (n==4):
        fourdigitprimes.append(next_prime)

for i in itertools.combinations(fourdigitprimes,3):
    p1 = i[0]
    p2 = i[1]
    p3 = i[2]
    if (same_digits_and_same_length(p1, p2)):
        if (same_digits_and_same_length(p2,p3)):
            if abs(p2-p1)==abs(p3-p2):
                print("arithmetic sequence {} {} {}".format(p1,p2,p3))
