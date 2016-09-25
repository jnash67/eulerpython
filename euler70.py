from __future__ import generators
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

numofminratio = 783169
phiofnumofminratio = 781396
minratio = numofminratio / phiofnumofminratio
print("first min num/phi is {} for num {} and phi {}".format(minratio, numofminratio,phiofnumofminratio))
primeFactorsDict = {}
size = 10000000
for totient in eu.primes.totients_below_not_in_order(size):
    n = totient[0]
    t = totient[1]
    # calculating the ratio should be faster than a bunch of string compares so
    # do that first
    ratio = n / t
    if ratio < minratio:
        if eu.numtext.same_digits_and_same_length(n,t):
            minratio = ratio
            numofminratio = n
            phiofnumofminratio = t
            print("NEW MIN PERMUTATION --> min num/phi is {} for num {} and phi {}".format(ratio, n, t))

print("min num/phi is {} for num {} and phi {}".format(minratio, numofminratio,phiofnumofminratio))
