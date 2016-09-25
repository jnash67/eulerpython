import sortedcontainers as sc
import time
import numpy as np
#import BitVector as bv
#import bits_mod as bm
import bitarray as ba

# primesfrom2to from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def very_fast_numpy_primes_less_than(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input num>=6, Returns a array of primes, 2 <= p < num """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(0, int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def fast_all_primes_less_than(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input num>=6, Returns a list of primes, 2 <= p < num """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in range(0,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(0,1,n/3-correction) if sieve[i]]


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a


def S(n):
    global primes
    global oddSumsOfTwoPrimes
    if n == 2:
        return 1
    ssum = 0
    # we add one for prime 2 and one for prime 3
    ssum += 2
    # by Goldbach Conjecture and because any even number k can be made of any number of primes > 2 up to all 2s
    for i in range(4, n + 1, 2):
        ssum = ssum + i // 2 - 1
    # by Waring's Prime Number Conjecture and because any odd number k can be made of any number of
    # primes > 2 up to all 2s minus 1. Main question is whether it is prime and whether there
    # are two primes that make up the odd number
    for i in range(5, n + 1, 2):
        ssum = ssum + i // 2 - 2
        if oddSumsOfTwoPrimes[i]==1:
            ssum += 1
        if i in primes:
            ssum += 1
    return ssum


start = time.time()

fibs = sc.SortedList()
for k in range(3, 45):
    fibs.append(fibonacci(k))


f44 = fibs[-1]
maxval = f44
primes = very_fast_numpy_primes_less_than(maxval + 1)
#sumOfTwoPrimes = bv.BitVector(size=f44+1)
#sumOfTwoPrimes = bm.Bits(f44, ones=False)
oddSumsOfTwoPrimes = ba.bitarray(f44)

# Here we calculate
p1 = 2
for p2index in range(1, len(primes)):
    p2 = primes[p2index]
    p1p2 = p1 + p2
    if p1p2 > maxval:
        break
    oddSumsOfTwoPrimes[p1p2] = 1

s10 = S(10)
print("S(10)={}".format(s10))
s100 = S(100)
print("S(100)={}".format(s100))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))

s1000 = S(1000)
print("S(100)={}, S(1000)={}".format(s100, s1000))

sumoverfibs = 0
f = 3
for fib in fibs:
    sfk = S(fib)
    print("S(F({})) is {} where F({}) is {}".format(f, sfk, f, fib))
    sumoverfibs += sfk
    f += 1

print("Sum over the fibonaccis is {}".format(sumoverfibs))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
