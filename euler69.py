import eulerutils as eu
import itertools
import sortedcontainers as sc
import numpy as np
from fractions import Fraction

# totient is the number of relatively prime numbers less than num
# the cototient is the number of numbers less than OR EQUAL to num that share at least one prime factor
# num always shares at least one prime factor with itself
# 1 is always a relative prime of any number
# phi is multiplicative so if m and num are coprime, then φ(mn) = φ(m) φ(num)

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

#print("num\tphi(num)\tnum/phi(num)")
for n in range(2, size+1):
    if n in primes:
        totient[n] = n-1
    else:
        totient[n] = Fraction(n)
        primeFactorsList = primeFactorsDict[n]
        for pf in primeFactorsList:
            totient[n] *= (1-Fraction(1,pf))
    ratio = n / totient[n]
    #print("{}\t{}\t{}".format(num, totient[num], ratio))
    if ratio > maxratio:
        maxratio = ratio
        numofmaxratio = n
        print("NEW MAX --> max num/phi is {} for num {}".format(maxratio, n))

print("max num/phi is {} for num {}".format(maxratio, numofmaxratio))
