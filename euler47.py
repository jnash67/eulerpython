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

# only checking for one of them being squared or cubed.
# Not checking if more than one is squared or more than one is cubed or for higher powers
def hasFourDistinctPrimeFactors(num, indexofprimestouse):
    global primes
    if (num % 2 == 0):
        # if even then we know that 2 would have to be the first prime factor
        p1 = 2
        primeslice = primes[1:indexofprimestouse]
        lenslice = len(primeslice)
        for i in range(0,lenslice):
            p2 = primeslice[i]
            for j in range(i, lenslice):
                p3 = primeslice[j]
                multcheck = p1 * p2 * p3
                if (multcheck > num):
                    break
                for k in range(j, lenslice):
                    p4 = primeslice[k]
                    mult = p1*p2*p3*p4
                    if (mult > num):
                        break
                    if (areTheseFourFactors(num, mult, p1, p2, p3, p4)):
                        return True
    else:
        primeslice = primes[0:indexofprimestouse]
        lenslice = len(primeslice)
        for i in range(0,lenslice):
            p1 = primeslice[i]
            for j in range(i, lenslice):
                p2 = primeslice[j]
                for k in range(j, lenslice):
                    p3 = primeslice[k]
                    multcheck = p1 * p2 * p3
                    if (multcheck > num):
                        break
                    for l in range(k, lenslice):
                        p4 = primeslice[l]
                        mult = p1*p2*p3*p4
                        if (mult > num):
                           break
                        if (areTheseFourFactors(num, mult, p1, p2, p3, p4)):
                            return True
    return False

def areTheseFourFactors(num, mult, p1, p2, p3, p4):
        if (mult == num):
            print("{} Has 4 distinct prime factors {},{},{},{}".format(num, p1,p2,p3,p4))
            return True
        # check for squares of primes
        if (p1*mult == num) or (p2*mult == num) or (p3*mult == num) or (p4*mult == num):
            print("{} Has 4 distinct prime factors with one of them squared {},{},{},{}".format(num, p1,p2,p3,p4))
            return True
        # check for cubes
        if (p1*p1*mult == num) or (p2*p2*mult == num) or (p3*p3*mult == num) or (p4*p4*mult == num):
            print("{} Has 4 distinct prime factors with one of them cubed {},{},{},{}".format(num, p1,p2,p3,p4))
            return True
        # check for a square and a cube
        if (p1*p2*p2*mult == num) or (p1*p1*p2*mult == num):
            print("{} Has 4 distinct prime factors with one of the first two squared the other of the first two cubed {},{},{},{}".format(num, p1,p2,p3,p4))
            return True
        return False

primes = sc.SortedList()
minwithfour = 2*3*5*7
maxn = 100000
maxprime = int(maxn / minwithfour)
gp = get_primes(2)
for i in range(1,maxn):
    next_prime = next(gp)
    primes.append(next_prime)
    if (next_prime > maxprime):
        break

for a in range(210,maxn):
    if not(a in primes):
        # find highest prime to use
        for i in range(1, maxn):
            if primes[i-1] > a / minwithfour:
                break
        #print("Highest prime to use for {} is {}".format(a, primes[i-1]))
        if (hasFourDistinctPrimeFactors(a, i)):
            if (hasFourDistinctPrimeFactors(a+1,i)):
                print("==================== Found a pair")
                if (hasFourDistinctPrimeFactors(a+2,i)):
                    print("==================== Found a triplet")
                    if (hasFourDistinctPrimeFactors(a+3,i)):
                        print("{} {} {} {} have four distinct prime factors".format(a,a+1,a+2,a+3))
                        break
