import eulerutils as eu
import numpy as np
import sortedcontainers as sc
import time
import itertools

globalmax = 0
globaltprod = 0
globaltsum = 0

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

f44 = fibs[-1]

maxval = 100
globalmax = maxval
firstprimes = eu.primes.fast_all_primes_less_than(11)
primes = eu.primes.very_fast_numpy_primes_less_than(maxval + 1)
# ? is bool
results = np.zeros((maxval + 1, maxval + 1), dtype='?')

# generate first 10 results by brute force
for k in range(1, 11):
    if 2*k > 10:
        break
    for t in itertools.combinations_with_replacement(firstprimes, k):
        tsum = sum(t)
        if tsum <= 10:
            results[tsum, k] = True

ptentwo = results[10][2]
s10 = S_given_results(10, results)
print("P(10,2)={}, S(10)={}".format(ptentwo, s10))

# generate results for all multiples of primes
for p in primes:
    if p > maxval // 2:
        break
    for m in range(2, (maxval + 1) // p):
        pmult = m * p
        results[pmult, m] = True

# for all subsequent numbers look at all pairs of previously calculated values
for k in range(11, maxval + 1):
    up = 2
    down = k-2
    mid = k//2
    while up <= mid:
        if up + down ==k:
            for upright in range(1, k // 2):
                for downright in range(1, k // 2):
                    if results[up, upright] == True and results[down, downright] == True:
                        results[k, upright + downright] = True
        else:
            print("k:{} != up:{} + down:{}".format(k, up,down))
        up+=1
        down-=1


s100 = S_given_results(100, results)
print("S(100)={}".format(s100))
# s1000 = S_given_results(1000, results)
# print("S(100)={}, S(1000)={}".format(s100, s1000))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
