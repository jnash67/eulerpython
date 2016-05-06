import eulerutils as eu
import itertools
import sortedcontainers as sc
import numpy as np
from fractions import Fraction

size = 1000000
#size = 1020

# we want the largest Fraction above 2/5 = 0.4 and below 3/7 = .(428571) that is a reduced proper fraction
upper_bound = Fraction(3, 7)
lower_bound = Fraction(2, 5)

# all 1/n are reduced proper fractions.  After 1/2 =0.5 none are bigger then 2/5 = 0.4
# all 2/n for odd n are reduced proper fractions but after 2/5 none are bigger than 2/5
# no 3/n are to the left of 3/7 for n>7
# so we start with 4 and go up to
# primes = eu.primes.fast_all_primes_less_than(size)
# primeFactorsDict = {}
# for p in primes:
#     for mult in range(2 * p, size + 1, p):
#         primeFactorsDict.setdefault(mult, sc.SortedSet()).add(p)

for denominator in range(4, size + 1):
    # we can calculate the min and max numerators so the range is within the current bound
    min_num = int((denominator / lower_bound.denominator) * lower_bound.numerator) - 1
    max_num = int((denominator / upper_bound.denominator) * upper_bound.numerator)+ 1
    denominator_prime = eu.primes.is_prime(denominator)
    numerator = min_num
    new_lower_bound = False
    while numerator < max_num:
        f = Fraction(numerator, denominator)
        if lower_bound < f < upper_bound:
            numerator_prime = eu.primes.is_prime(numerator)
            if numerator_prime and denominator_prime:
                lower_bound = f
                new_lower_bound = True
                print("New immediately below {}".format(f))
            elif numerator_prime and not denominator_prime:
                pf2 = eu.primes.prime_factors(denominator)
                if not (numerator in pf2):
                    lower_bound = f
                    new_lower_bound = True
                    print("New immediately below {}".format(f))
            elif denominator_prime and not numerator_prime:
                pf1 = eu.primes.prime_factors(numerator)
                if not (denominator in pf1):
                    lower_bound = f
                    new_lower_bound = True
                    print("New immediately below {}".format(f))
            else:
                pf1 = eu.primes.prime_factors(numerator)
                pf2 = eu.primes.prime_factors(denominator)
                if not (eu.collectionutils.do_collections_share_an_item(pf1, pf2)):
                    lower_bound = f
                    print("New immediately below {}".format(f))
                    new_lower_bound = True

        if new_lower_bound:
            # redo the range for denominator
            min_num = int((denominator / lower_bound.denominator) * lower_bound.numerator) - 1
            numerator = min_num
            new_lower_bound = False
        else:
            numerator += 1
