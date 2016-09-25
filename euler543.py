import eulerutils as eu
import numpy as np
import sortedcontainers as sc
import time

globalmax = 0
globaltprod = 0
globaltsum = 0


def combinations_with_replacement_and_sum_with_terminating_condition(iterable, r):
    global globalmax
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    t = tuple(pool[i] for i in indices)
    yield sum(t), t
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        t = tuple(pool[i] for i in indices)
        tsum = sum(t)
        if tsum > globalmax:
            indices[i] = n - 1
        else:
            yield tsum, t


def combinations_with_replacement_with_terminating_condition(iterable, r):
    global globalmax, globaltprod, globaltsum
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    t = tuple(pool[i] for i in indices)
    globaltsum = sum(t)
    globaltprod = eu.number.product(t)
    if globaltsum > globalmax:
        indices[0] = n - 1
    else:
        # globaltprod = eu.number.product(t)
        # if globaltprod > globalmax:
        #     indices[0] = num - 1
        # else:
        yield t
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        t = tuple(pool[i] for i in indices)
        globaltsum = sum(t)
        if globaltsum > globalmax:
            indices[i] = n - 1
        else:
            # globaltprod = eu.number.product(t)
            # if globaltprod > globalmax:
            #     indices[i] = num - 1
            # else:
            yield t


# returns 1 if num can be written as sum of k primes (with repetitions allowed) and 0 otherwise
def P(n, k):
    if k >= n:
        return 0
    global primes
    global globalmax
    primes_subset = [p for p in primes if p <= n]
    globalmax = n
    for t in combinations_with_replacement_and_sum_with_terminating_condition(primes_subset, k):
        tsum = t[0]
        if tsum == n:
            return True
    return False


def S(n):
    global results
    sum = 0
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            pik = P(i, k)
            if pik:
                sum += 1
                results[i][k] = True
    return sum


def S_given_results(n, results):
    sum = 0
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            pik = results[i][k]
            if pik:
                sum += 1
    return sum



start = time.time()

fibs = sc.SortedList()
for k in range(3, 45):
    fibs.append(eu.fibonacci(k))


maxval = 100
globalmax = maxval
primes = eu.primes.very_fast_numpy_primes_less_than(maxval+1)
# ? is bool
results = np.zeros((maxval+1, maxval+1), dtype='?')
#print(S(10))

for k in range(1, maxval+1):
    if 2*k > globalmax:
        break
    for ptuple in combinations_with_replacement_with_terminating_condition(primes, k):
        results[globaltsum, k] = True

#S_given_results(maxval, results)

ptentwo = results[10][2]
s10 = S_given_results(10, results)
print("P(10,2)={}, S(10)={}".format(ptentwo, s10))
s100 = S_given_results(100, results)
s1000 = S_given_results(1000, results)
print("S(100)={}, S(1000)={}".format(s100, s1000))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
