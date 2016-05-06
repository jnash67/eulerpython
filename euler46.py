import math
import itertools
import sortedcontainers as sc

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

def is_goldbach(composite):
    global primes
    assert not(composite in primes), "Not a composite number"
    goldbach = False
    for p in primes:
        if (p > composite):
            return False
        maxsq = int(math.sqrt(composite/2)+1)
        for q in range(1,maxsq):
            if (composite==p+2*q*q):
                # it's goldbach
                print("{} = {} + 2*{}^2".format(i, p, q))
                return True
    return False



primes = sc.SortedList()
maxn = 10000
gp = get_primes(3)
for i in range(1,maxn):
    next_prime = next(gp)
    primes.append(next_prime)

for i in range(9,maxn, 2):
    if not (i in primes):
        # it is composite
        if not(is_goldbach(i)):
            print("{} is NOT goldbach".format(i))
            break
