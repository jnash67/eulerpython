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
def check_five_pairs_min_sum():
    global primes
    global alreadyCheckedPrimePairs

    # an upper bound for the max is the last 5 primes concatenated together
    minsumstr = ""
    for i in range(0,5):
        minsumstr += str(primes[len(primes) - i - 1])
    minsum = int(minsumstr)
    count = 0
    lenp = len(primes)

    for i in range(0, lenp):
        p1 = primes[i]
        for j in range(i+1, lenp):
            p2 = primes[j]
            sump1p2 = primes[i]+primes[j]
            if (sump1p2 > minsum):
                break
            if (p1,p2) in alreadyCheckedPrimePairs:
                for k in range(j+1, lenp):
                    p3 = primes[k]
                    sump1p2p3 = sump1p2 + p3
                    if (sump1p2p3 > minsum):
                        break
                    if (p1,p3) in alreadyCheckedPrimePairs:
                        if (p2,p3) in alreadyCheckedPrimePairs:
                            for l in range(k+1, lenp):
                                p4 = primes[l]
                                sump1p2p3p4 = sump1p2p3 + p4
                                if (sump1p2p3p4 > minsum):
                                    break
                                if (p1,p4) in alreadyCheckedPrimePairs:
                                    if (p2,p4) in alreadyCheckedPrimePairs:
                                        if (p3,p4) in alreadyCheckedPrimePairs:
                                            for m in range(l+1, lenp):
                                                p5 = primes[m]
                                                sump1p2p3p4p5 = sump1p2p3p4 + p5
                                                if (sump1p2p3p4p5 > minsum):
                                                    break
                                                if (p1,p5) in alreadyCheckedPrimePairs:
                                                    if (p2,p5) in alreadyCheckedPrimePairs:
                                                        if (p3,p5) in alreadyCheckedPrimePairs:
                                                            if (p4,p5) in alreadyCheckedPrimePairs:
                                                                print("A combination that works is {},{},{},{},{}. They sum to {}".format(p1,p2,p3,p4,p5, sump1p2p3p4p5))
                                                                if (sump1p2p3p4p5<minsum):
                                                                    minsum = sump1p2p3p4p5
                                                                    print("THIS IS A NEW MINIMUM SUM")

    # this doesn't work if we use @timeit
    return minsum


@timeit
def check_four_pairs_min_sum():
    global primes
    global alreadyCheckedPrimePairs

    # an upper bound for the max is the last 5 primes concatenated together
    minsumstr = ""
    for i in range(0,4):
        minsumstr += str(primes[len(primes) - i - 1])
    minsum = int(minsumstr)
    count = 0
    lenp = len(primes)

    for i in range(0, lenp):
        p1 = primes[i]
        for j in range(i+1, lenp):
            p2 = primes[j]
            sump1p2 = primes[i]+primes[j]
            if (sump1p2 > minsum):
                break
            if (p1,p2) in alreadyCheckedPrimePairs:
                for k in range(j+1, lenp):
                    p3 = primes[k]
                    sump1p2p3 = sump1p2 + p3
                    if (sump1p2p3 > minsum):
                        break
                    if (p1,p3) in alreadyCheckedPrimePairs:
                        if (p2,p3) in alreadyCheckedPrimePairs:
                            for l in range(k+1, lenp):
                                p4 = primes[l]
                                sump1p2p3p4 = sump1p2p3 + p4
                                if (sump1p2p3p4 > minsum):
                                    break
                                if (p1,p4) in alreadyCheckedPrimePairs:
                                    if (p2,p4) in alreadyCheckedPrimePairs:
                                        if (p3,p4) in alreadyCheckedPrimePairs:
                                            print("A combination that works is {},{},{},{}. They sum to {}".format(p1,p2,p3,p4,sump1p2p3p4))
                                            if (sump1p2p3p4<minsum):
                                                minsum = sump1p2p3p4
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


maxn = 10000
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
print("There are {} prime pairs that are also prime when concatenated in either order.".format(len(alreadyCheckedPrimePairs)))

primesInPairs = sc.SortedSet()
for p in alreadyCheckedPrimePairs:
    p1 = p[0]
    p2 = p[1]
    primesInPairs.add(p1)
    primesInPairs.add(p2)
print("There are {} primes in pairs".format(len(primesInPairs)))

minsum = check_four_pairs_min_sum()
minsum = check_five_pairs_min_sum()
#print("For the range tested, the overall minimum sum is {}".format(minsum))
#minsum = check_pairs_min_sum(5)
#print("For the range tested, the overall minimum sum is {}".format(minsum))