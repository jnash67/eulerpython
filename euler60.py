import timeit

import functools

import time

import eulerutils as eu
import itertools
import sortedcontainers as sc

def timeit(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
    return newfunc


@timeit
def check_pairs_min_sum(n):
    global primes
    global alreadyCheckedPrimePairs

    # an upper bound for the max is the last 5 primes concatenated together
    minsumstr = ""
    for i in range(0,n):
        minsumstr += str(primes[len(primes) - i - 1])
    minsum = int(minsumstr)
    count = 0

    for i in itertools.combinations(primes,n):
        count += 1
        if (count % 1000000 == 0):
            print("{:,} combinations checked".format(count))
        found = True
        sumi = sum(i)
        if (sumi < minsum):
            for j in itertools.combinations(i,2):
                p1 = j[0]
                p2 = j[1]
                if not (p1,p2) in alreadyCheckedPrimePairs:
                    found = False
                    break

            if found:
                print("A combination that works is {}. They sum to {}".format(i, sum(i)))
                if (sumi<minsum):
                    minsum = sumi
                    print("THIS IS A NEW MINIMUM SUM")

    # this doesn't work if we use @timeit
    return minsum


@timeit
def precalculate_prime_pairs():
    global primes
    # pre-calculate the status of all prime pairs
    for i in itertools.combinations(primes,2):
        p1 = i[0]
        p2 = i[1]
        p1str = str(p1)
        p2str = str(p2)
        p1p2 = int(p1str + p2str)
        p2p1 = int(p2str + p1str)
        if eu.primes.is_prime(p1p2) and eu.primes.is_prime(p2p1):
            alreadyCheckedPrimePairs.add((p1,p2))


maxn = 1000
# we can ignore 2 and 5, they will not be part of any such prime pair sets
primes = eu.primes.all_primes_between(3,maxn)
b = primes.index(5)
del(primes[b])
print("There are {} primes".format(len(primes)))
biggestprime = primes[len(primes)-1]
print("The biggest prime is {}".format(biggestprime))
print("{} choose 4 is {:,}".format(len(primes),int(eu.number.choose(len(primes),4))))
print("{} choose 5 is {:,}".format(len(primes),int(eu.number.choose(len(primes),5))))

#alreadyCheckedNonPrimePairs = sc.SortedSet()
alreadyCheckedPrimePairs = sc.SortedSet()
precalculate_prime_pairs()

minsum = check_pairs_min_sum(4)
#print("For the range tested, the overall minimum sum is {}".format(minsum))
minsum = check_pairs_min_sum(5)
#print("For the range tested, the overall minimum sum is {}".format(minsum))