import eulerutils as eu
import itertools
import sortedcontainers as sc
import numpy as np
from fractions import Fraction

# totient is the number of relatively prime numbers less than n
# the cototient is the number of numbers less than OR EQUAL to n that share at least one prime factor
# n always shares at least one prime factor with itself
# 1 is always a relative prime of any number
# phi is multiplicative so if m and n are coprime, then φ(mn) = φ(m) φ(n)

size = 1000000
primes = sc.SortedList()
for next_prime in eu.primes.get_primes(2):
    if next_prime < size :
        primes.add(next_prime)
    else:
        break

totient = np.zeros(size+1)
maxratio = 0
numofmaxratio = 0
coprimetotest = 1
primeFactorsDict = {}
for p in primes:
    for mult in range(2*p, size+1,p):
        primeFactorsDict.setdefault(mult, sc.SortedSet()).add(p)

#print("n\tphi(n)\tn/phi(n)")
for n in range(2, size+1):
    if n in primes:
        totient[n] = n-1
    else:
        totient[n] = Fraction(n)
        primeFactorsList = primeFactorsDict[n]
        for pf in primeFactorsList:
            totient[n] *= (1-Fraction(1,pf))
    ratio = n / totient[n]
    #print("{}\t{}\t{}".format(n, totient[n], ratio))
    if ratio > maxratio:
        maxratio = ratio
        numofmaxratio = n
        print("NEW MAX --> max n/phi is {} for n {}".format(maxratio, n))

print("max n/phi is {} for n {}".format(maxratio, numofmaxratio))
