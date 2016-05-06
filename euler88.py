import eulerutils as eu
import numpy as np
import sortedcontainers as sc
import time


def combinations_with_replacement_with_terminating_condition(iterable, r):
    global globalmax
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    t = tuple(pool[i] for i in indices)
    yield t
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        t = tuple(pool[i] for i in indices)
        tprod = eu.number.product(t)
        if tprod > globalmax:
            indices[i] = n-1
        yield t


start = time.time()

lower = 2
upper = 12000
globalmax = 2 * (upper + 1)
factors = list(range(2, globalmax))

minsetsumarray = np.zeros(upper + 1)
setofminsetsumdict = sc.SortedDict()

# 2^14 > 12000, so there's no point at choosing more than 14 from the set of primes with replacement
for choose in range(2, 15):
    factors = list(range(2, globalmax // 2 ** (choose - 2)))
    iter = combinations_with_replacement_with_terminating_condition(factors, choose)
    for trial in iter:
        trialprod = eu.number.product(trial)
        if (trial[0] > 110 and trialprod > globalmax):
            break
        if trialprod <= globalmax:
            trialsum = np.sum(trial)
            # we need prod - sum ones to make the sum and the prod equal
            if trialsum >= trialprod:
                trialk = choose
            else:
                trialk = choose + (trialprod - trialsum)
            if trialk <= upper:
                val = minsetsumarray[trialk]
                if (val == 0) or (val > 0 and trialprod < val):
                    minsetsumarray[trialk] = trialprod
                    setofminsetsumdict[trialk] = trial

uniqueminsetsum = sc.SortedSet()
for i in range(lower, upper + 1):
    if minsetsumarray[i] == 0:
        print("The approach didn't find a set for k={}".format(i))
    else:
        uniqueminsetsum.add(minsetsumarray[i])

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))

print("The sum of the the minimum product-sum numbers (excl. duplicates) is {}".format(np.sum(uniqueminsetsum)))
print("The set is {}".format(uniqueminsetsum))
