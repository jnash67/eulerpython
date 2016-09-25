import eulerutils as eu
import sortedcontainers as sc
import time
import BitVector as bv
import numpy as np


def S_given_results(n, results):
    sum = 0
    for i in range(1, n + 1):
        for k in range(1, (i+2) // 2):
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
maxval = f44
globalmax = maxval

# the resulting matrix is lower triangular since P(num,k)=0 for k>=num
results = np.empty(maxval+1, dtype=object)
# results = ba.BitArray2D(rows=maxval, columns=maxval//2)

primes = eu.primes.very_fast_numpy_primes_less_than(maxval + 1)

for k in range(2, maxval + 1):
    if k % 1000 == 0:
        print("On the {}th thousand. {} thousands to go".format(k//1000, (f44-k)//1000))
    if k in primes:
        if results[k] is None:
            results[k] = bv.BitVector(size=(k+2) // 2)
        results[k][1] = 1
    for p in primes:
        if k + p > maxval:
            break
        for right in range(1, (k+2) // 2):
            if results[k][right] == 1:
                if results[k + p] is None:
                    results[k + p] = bv.BitVector(size=(k + p + 2) // 2)
                results[k + p][right + 1] = 1

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
