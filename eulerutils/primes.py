import math
import sortedcontainers as sc
import eulerutils as eu
import collections
import numpy as np

pF = collections.defaultdict(list)
primesList = []


# primesfrom2to from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def very_fast_numpy_primes_less_than(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n / 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(0, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


# rwh_primes1 from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def fast_all_primes_less_than(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


# http://stackoverflow.com/questions/1024640/calculating-phik-for-1kn/1134851#1134851
# doesn't return them in order
def totients_below_not_in_order(N):
    allprimes = fast_all_primes_less_than(N + 1)

    def rec(n, partialtot=1, min_p=0):
        for p in allprimes:
            if p > n:
                break
            # avoid double solutions such as (6, [2,3]), and (6, [3,2])
            if p < min_p: continue
            yield (p, p - 1, [p])
            for t, tot2, r in rec(n // p, partialtot, min_p=p):  # uses integer division
                yield (t * p, tot2 * p if p == r[0] else tot2 * (p - 1), [p] + r)

    for n, t, factors in rec(N):
        yield (n, t)


def totient(n):
    if n == 1:
        return 1
    a = 1
    c = collections.Counter(prime_factors(n))
    for i in c.keys():
        k = c[i]
        a *= (i ** k) - (i ** (k - 1))
    return a


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


# returns prime after n
def next_prime(n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    while not is_prime(n):
        n += 2
    return n


def all_primes_less_than(n):
    primes = sc.SortedList()
    gp = get_primes(2)
    while True:
        next_prime = next(gp)
        if next_prime < n:
            primes.append(next_prime)
        else:
            break
    return primes


def all_primes_between(a, n):
    primes = sc.SortedList()
    gp = get_primes(a)
    while True:
        next_prime = next(gp)
        if next_prime < n:
            primes.append(next_prime)
        else:
            break
    return primes


def all_n_digit_primes(n):
    primes = sc.SortedList()
    start = 2
    if (n > 1):
        start = int("9" * (n - 1)) + 1
    ndigitprimes = []
    gp = get_primes(start)
    while True:
        next_prime = next(gp)
        dig = eu.number.num_digits(next_prime)
        if (dig > n):
            break
        if (dig == n):
            ndigitprimes.append(next_prime)
    return ndigitprimes


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


# from https://projecteuler.net/thread=70;page=5
def prime_factors(n):
    o = n
    i = 2
    if n in pF:
        return pF[n]
    while i <= math.sqrt(n):
        if n in pF:
            pF[o] = pF[o] + pF[n]
            return pF[o]
        if n % i == 0:
            n = n // i
            pF[o].append(i)
            i = 2
            continue
        try:
            i = primesList[i]
        except:
            i = next_prime(i)
            primesList.append(i)
    pF[o].append(n)
    return pF[o]


def is_pythagorean_triple_primitive(a, b, c):
    afactors = prime_factors(a)
    bfactors = prime_factors(b)
    if eu.collectionutils.do_collections_share_an_item(afactors, bfactors):
        return False
    else:
        cfactors = prime_factors(c)
        if eu.collectionutils.do_collections_share_an_item(afactors, cfactors):
            return False
        elif eu.collectionutils.do_collections_share_an_item(bfactors, cfactors):
            return False
    return True
