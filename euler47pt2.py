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

def calc_results(p1, p2, p3, p4, result):

    # get with one square
    sq1 = p1 * result
    sq2 = p2 * result
    sq3 = p3 * result
    sq4 = p4 * result
    # get with one cube
    cu1 = p1 * sq1
    cu2 = p2 * sq2
    cu3 = p3 * sq3
    cu4 = p4 * sq4

    # get with two squares
    # p1 & p2 squared
    sq12 = sq1 * p2
    # p1 & p3 squared
    sq13 = sq1 * p3
    # p1 & p4 squared
    sq14 = sq1 * p4
    # p2 & p3 squared
    sq23 = sq2 * p3
    # p2 & p4 squared
    sq24 = sq2 * p4
    # p3 & p4 squared
    sq34 = sq3 * p4

    # get with 3 squares
    sq123 = sq12*p3
    sq124 = sq12*p4
    sq134 = sq13*p4
    sq234 = sq23*p4

    # get with 4 squares
    sq1234 = sq123*p4

    # get with two cubes
    # p1 & p2 cubed
    cu12 = cu1 * p2
    # p1 & p3 cubed
    cu13 = cu1 * p3
    # p1 & p4 cubed
    cu14 = cu1 * p4
    # p2 & p3 cubed
    cu23 = cu2 * p3
    # p2 & p4 cubed
    cu24 = cu2 * p4
    # p3 & p4 cubed
    cu34 = cu3 * p4

    # get with 3 cubes
    cu123 = cu12*p3
    cu124 = cu12*p4
    cu134 = cu13*p4
    cu234 = cu23*p4

    # get with 4 cubes
    cu1234 = cu123*p4

    addToResultSet(result)
    addToResultSet(sq1)
    addToResultSet(sq2)
    addToResultSet(sq3)
    addToResultSet(sq4)
    addToResultSet(sq12)
    addToResultSet(sq13)
    addToResultSet(sq14)
    addToResultSet(sq23)
    addToResultSet(sq24)
    addToResultSet(sq34)
    addToResultSet(sq123)
    addToResultSet(sq124)
    addToResultSet(sq134)
    addToResultSet(sq234)
    addToResultSet(sq1234)
    addToResultSet(cu1)
    addToResultSet(cu2)
    addToResultSet(cu3)
    addToResultSet(cu4)
    addToResultSet(cu12)
    addToResultSet(cu13)
    addToResultSet(cu14)
    addToResultSet(cu23)
    addToResultSet(cu24)
    addToResultSet(cu34)
    addToResultSet(cu123)
    addToResultSet(cu124)
    addToResultSet(cu134)
    addToResultSet(cu234)
    addToResultSet(cu1234)

def addToResultSet(num):
    global maxn
    global resultsSet
    if (num < maxn):
        resultsSet.add(num)

primes = sc.SortedList()
resultsSet = set()
minwithfour = 2 * 3 * 5 * 7
maxn = 200000
maxprime = int(maxn / minwithfour)
gp = get_primes(2)
for i in range(1, maxn):
    next_prime = next(gp)
    primes.append(next_prime)
    if (next_prime > maxprime):
        break

lenprimes = len(primes)
for i in range(0,lenprimes):
    p1 = primes[i]
    for j in range(i+1, lenprimes):
        p2 = primes[j]
        for k in range(j+1, lenprimes):
            p3 = primes[k]
            multcheck = p1 * p2 * p3
            if (multcheck > maxn):
                break
            for l in range(k+1, lenprimes):
                p4 = primes[l]
                mult = p1*p2*p3*p4
                if (mult > maxn):
                    break
                calc_results(p1,p2,p3,p4, mult)

lenresults = len(resultsSet)
resultsList = sorted(list(resultsSet))
for r in range(0, lenresults-3):
    r1 = resultsList[r]
    r2 = resultsList[r+1]
    r3 = resultsList[r+2]
    r4 = resultsList[r+3]
    if (r2-r1 == 1) and (r3-r2==1) and (r4-r3==1):
        print("First four in a row starting at index {}".format(r))
        print("They are: {} {} {} {}".format(r1,r2,r3,r4))
        break
