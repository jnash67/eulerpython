import eulerutils as eu
import sortedcontainers as sc
import time
import BitVector as bv
import numpy as np


def S_given_results(n, results):
    sum = 0
    for i in range(1, n + 1):
        for k in range(1, (i+2) // 2):
            if not results[i] is None:
                pik = results[i][k]
                if pik == 1:
                    sum += 1
    return sum


start = time.time()

fibs = sc.SortedList()
for k in range(3, 45):
    fibs.append(eu.fibonacci(k))

f44 = fibs[-1]

# maxval = f44
maxval = 100
globalmax = maxval

# the resulting matrix is lower triangular since P(n,k)=0 for k>=n
results = np.empty(maxval+1, dtype=object)
# results = ba.BitArray2D(rows=maxval, columns=maxval//2)

primes = eu.primes.very_fast_numpy_primes_less_than(maxval + 1)

for k in primes:
    if k > maxval:
        break
    if k % 1000 == 0:
        print("On the {}th thousand. {} thousands to go".format(k//1000, (f44-k)//1000))
    # for all multiples of this prime including the first:
    for m in range(1, maxval):
        kmult = m * k
        if kmult > maxval:
            break
        if results[kmult] is None:
            results[kmult] = bv.BitVector(size=(kmult+2) // 2)
        results[kmult][m] = True
        # for all other primes add to this prime and its multiples
        for p in primes:
            if kmult + p > maxval:
                break
            for right in range(1, (kmult+2) // 2):
                if results[kmult][right] == 1:
                    if results[kmult + p] is None:
                        results[kmult + p] = bv.BitVector(size=(kmult + p + 2) // 2)
                    results[kmult + p][right + 1] = 1

ptentwo = results[10][2]
s10 = S_given_results(10, results)
print("P(10,2)={}, S(10)={}".format(ptentwo, s10))
s100 = S_given_results(100, results)
print("S(100)={}".format(s100))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))

s1000 = S_given_results(1000, results)
print("S(100)={}, S(1000)={}".format(s100, s1000))

sumoverfibs = 0
f = 3
for fib in fibs:
    sfk = S_given_results(fib, results)
    print("S(F({})) is {} where F({}) is {}".format(f, sfk, f, fib))
    sumoverfibs += sfk
    f += 1

print("Sum over the fibonaccis is {}".format(sumoverfibs))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
