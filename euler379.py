import collections
import math
import time

import sympy

prime_exponent_dicts = collections.defaultdict(dict)
mobius_dict = collections.defaultdict(int)
divisors_dict = collections.defaultdict(list)

# In problem 108 and 110 we worked with OEIS A018892, Number of ways to write 1/n as a sum of exactly
# 2 unit fractions. That page points out that the series is is equivalent to the number of pairs (x,y)
# such that LCM(x,y)=n.  So OEIS 018892 is part of the answer to this question as well.
# This involves A182082, A061503, A048691

# sigma_1(ab) = sigma_1(a)*sigma_1(b)
# A018892 = (sigma_0(n^2)+1)//2
# g(n) is the sum of the A018892s from 1 to n inclusive.
#
# we are given g(10^6) = 37429395.
# since g is a summation over sigma_0 which is multiplicative, it too is multiplicative

def a018892(nval):
    return (sigma_k(int(nval * nval), 0) + 1) // 2


def a018892_2(nval):
    return (sigma_0_pow(nval, 2) + 1) // 2


# sigma_0 aka tau
# def fast_sigma_0(n):
#     if n == 1:
#         return 1
#     pd = prime_factors_dict(n)
#     s0mult = 1
#     for p, e in pd.items():
#         s0mult *= (e + 1)
#     return int(s0mult)


# sigma_0 aka tau
# def sigma_0(nval):
#     return divisor_count(nval)

# Number of distinct primes dividing n. http://oeis.org/A001221
def omega(nval):
    if nval == 1:
        return 0
    if nval in prime_exponent_dicts:
        pd = prime_exponent_dicts[nval]
    else:
        pd = sympy.factorint(nval)
        prime_exponent_dicts[nval] = pd
    return len(pd)


# http://oeis.org/A019554
def smallest_number_whose_square_is_divisible_by_n(nval):
    if nval == 1:
        return 1
    if nval in prime_exponent_dicts:
        pd = prime_exponent_dicts[nval]
    else:
        pd = sympy.factorint(nval)
        prime_exponent_dicts[nval] = pd
    snwsidbn = 1
    for pval, expval in pd.items():
        snwsidbn *= math.pow(pval, math.ceil(expval / 2))
    return int(snwsidbn)


# http://oeis.org/A055205
def number_of_nonsquare_divisors_of_nsquared(nval):
    s0 = sigma_0_pow(nval, 1)
    s0sq = sigma_0_pow(nval, 2)
    return s0sq-s0


def sigma_0_and_sigma_0_squared(nval):
    if nval == 1:
        return 1, 1
    if pow == 0:
        return 1, 1
    if nval in prime_exponent_dicts:
        pd = prime_exponent_dicts[nval]
    else:
        pd = sympy.factorint(nval)
        prime_exponent_dicts[nval] = pd
    s0mult = 1
    s0sqmult = 1
    for pval, expval in pd.items():
        s0mult *= (expval + 1)
        s0sqmult *= (expval * 2 + 1)
    return int(s0mult), int(s0sqmult)

# http://oeis.org/A048691
def sigma_0_nsquared(nval):
    if nval == 1:
        return 1
    if nval in divisors_dict:
        divs = divisors_dict[nval]
    else:
        divs = sympy.divisors(nval)
        divisors_dict[nval] = divs
    sigval = 0
    for div in divs:
        mult = nval // div
        if mult in mobius_dict:
            mob = mobius_dict[mult]
        else:
            mob = int(sympy.mobius(mult))
            mobius_dict[mult] = mob
        sig0 = sigma_0_pow(div, 1)
        sigval += mob * math.pow(sig0, 2)
    return int(sigval)


# def sigma_0_nsquared(nval):
#     if nval == 1:
#         return 1
#     divs = sympy.divisors(nval)
#     sigval = 0
#     for div in divs:
#         mult = nval // div
#         mob = sympy.mobius(mult)
#         sig0 = sigma_0_pow(div, 1)
#         sigval += sig0 * math.pow(mob,2)
#     return int(sigval)



# sigma_0(n^p). sigma_0_pow(n,1)=sigma_0(n)=http://oeis.org/A000005
# sigma_0_pow(n,2)=sigma_0(n^2)=http://oeis.org/A048691
def sigma_0_pow(nval, powval=1):
    if nval == 1:
        return 1
    if pow == 0:
        return 1
    if nval in prime_exponent_dicts:
        pd = prime_exponent_dicts[nval]
    else:
        pd = sympy.factorint(nval)
        prime_exponent_dicts[nval] = pd
    s0mult = 1
    for pval, expval in pd.items():
        s0mult *= (expval * powval + 1)
    return int(s0mult)


# sigma_1 aka just sigma
def sigma_1(nval):
    if nval == 1:
        return 1
    if nval in prime_exponent_dicts:
        pd = prime_exponent_dicts[nval]
    else:
        pd = sympy.factorint(nval)
        prime_exponent_dicts[nval] = nval
    psigmult = 1
    for pval, expval in pd.items():
        psigmult *= ((math.pow(pval, expval + 1) - 1) / (pval - 1))
    return int(psigmult)


# sigma_k(n,0)=sigma_0(n)=count of divisors of n A000005
# sigma_k(n,1)=sigma_1(n)=sum of divisors of n A000203
# sigma_k(n,2)=sigma_2(n)=sum of squares of divisors of n A001157
def sigma_k(nval, kval=1):
    if nval == 1:
        return 1
    if kval == 1:
        return sigma_1(nval)
    if kval == 0:
        return sigma_0_pow(nval, 1)
    divs = sympy.divisors(nval)
    sigval = 0
    for div in divs:
        sigval += math.pow(div, kval)
    return int(sigval)


# this is summatory of tau. A fast special formula.
# http://math.stackexchange.com/questions/850135/tau-summatory-function
def sum_of_sigma_0s(nval):
    sigma_0_sum = 0
    s = math.floor(math.sqrt(nval))
    for k in range(1, s + 1):
        sigma_0_sum += math.floor(nval / k)
    sigma_0_sum *= 2
    sigma_0_sum -= s * s
    return sigma_0_sum


# http://oeis.org/A061503
def sum_of_sigma_0s_for_nsquared_using_omega(nval):
    # Sum(i=1..n, 2 ^ omega(i) * floor(n / i))
    sigma_0_sum = 0
    for i in range(1, nval + 1):
        # ss += sigma_0_pow(i, 2)
        sigma_0_sum += math.pow(2, omega(i)) * math.floor(nval / i)
    return sigma_0_sum


# http://oeis.org/A061503
def sum_of_sigma_0s_for_nsquared(nval):
    sigma_0_sum = 0
    for i in range(1, nval + 1):
        # ss += sigma_0_pow(i, 2)
        sigma_0_sum += sigma_0_nsquared(i)
    return sigma_0_sum


# http://oeis.org/A061503
def slow_sum_of_sigma_0s_for_nsquared(nval):
    sigma_0_sum = 0
    for i in range(1, nval + 1):
        # ss += sigma_0_pow(i, 2)
        sigma_0_sum += sigma_0_pow(i, 2)
    return sigma_0_sum


def stats(nval):
    s0 = sigma_0_pow(nval, 1)
    s0sq = sigma_0_pow(nval, 2)
    s0sq2 = sigma_0_nsquared(nval)
    print("tau/sigma_0(n) {}: {}".format(nval, s0))
    print("tau^2(n) {}: {}".format(nval, s0sq))
    print("tau^2(n) using mobius {}: {}".format(nval, s0sq2))
    print("sum of sigma_0s(n) {}: {}".format(nval, sum_of_sigma_0s(nval)))
    #print("sum_of_sigma_0s_squared(n) {}: {}".format(math.pow(nval, 2), sum_of_sigma_0s_for_nsquared(nval)))
    print("=================")



n0 = int(math.pow(10, 4))
n1 = int(math.pow(10, 6))
n2 = int(math.pow(10, 12))

stats(10)
stats(n0)
stats(n1)
stats(2000000)
stats(n2)

start_time = time.time()
for i in range(1, 100 + 1):
    sig = sigma_0_nsquared(i)
    print("{} {}".format(i, sig))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

# sumtau = 0
# sumtausq = 0
# for n in range(1, 10 + 1):
#     if n % 100000 == 0:
#         print("On n {}".format(n))
#     tau = fast_sigma_0(n)
#     t2 = fast_sigma_0(n * n)
#     sumtau += tau
#     sumtausq += t2
# # print("{}: {}".format(n, g))
# print("n:{} sum of tau(n):{}  sum of tau(n^2):{}".format(10, sumtau, sumtausq))
# finish = time.time()

start_time = time.time()
sumtau = 0
sumtausq = 0
for i in range(1, n1 + 1):
    if i % 100000 == 0:
        print("On n {}".format(i))
    # tau, tausq = sigma_0_and_sigma_0_squared(i)
    tau = sigma_0_pow(i, 1)
    tausq = sigma_0_pow(i, 2)
    sumtau += tau
    sumtausq += tausq
print("n:{} sum of tau(n):{}  sum of tau(n^2):{}".format(n1, sumtau, sumtausq))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

stats(10)
stats(n0)
stats(n1)
stats(2000000)
# stats(n2)

print("sum_of_sigma_0s {}: {}".format(n0, sum_of_sigma_0s(n0)))

start_time = time.time()
d = sympy.factorint(n0)
g = 1
for p, e in d.items():
    pe = math.pow(p, e)
    ss = sum_of_sigma_0s(pe)
    g *= ss
print("sigma_0_summatory mult prime factors {}: {}".format(n0, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

# prime_factors_dict(n1)
#
# print("Prime Factors {}:{}".format(n1, prime_factors_dict(n1)))
# print("Prime Factors {}:{}".format(n2, prime_factors_dict(n2)))
#
# print("Divisors {}:{}".format(n1, divisors(n1)))
# print("Divisors {}:{}".format(n2, divisors(n2)))

#
# print("\nPrime Factors of Multiple between Sum(Tau(n)^2)/sum(Tau(n))")
# print("Prime Factors {}:{}".format(376197, prime_factors_dict(376197)))
# print("Prime Factors {}:{}".format(463463, prime_factors_dict(463463)))
# print("Prime Factors {}:{}".format(898597, prime_factors_dict(898597)))
#
# print("\nPrime Factors of Sum(Tau(n))")
# print("Prime Factors {}:{}".format(13970034, prime_factors_dict(13970034)))
# print("Prime Factors {}:{}".format(29326296, prime_factors_dict(29326296)))
# print("Prime Factors {}:{}".format(27785452449086, prime_factors_dict(27785452449086)))
#
# print("\nPrime Factors of Sum(Tau(n^2))")
# print("Prime Factors {}:{}".format(73858790, prime_factors_dict(73858790)))
# print("Prime Factors {}:{}".format(161230032, prime_factors_dict(161230032)))
#
# print("\nPrime Factors of Sum(Tau(n)^2)")
# print("Prime Factors {}:{}".format(421094344, prime_factors_dict(421094344)))
# print("Prime Factors {}:{}".format(957082634, prime_factors_dict(957082634)))
#
# print("Sigma Summatory {}:{}".format(n1, sigma_0_summatory(n1)))
# print("Sigma Summatory {}:{}".format(2 * n1, sigma_0_summatory(2 * n1)))
# # print("Sigma Summatory {}:{}".format(n2,sigma_0_summatory(n2)))
# #
# print("tau {}: {}".format(n1, tau(n1)))
# print("tau {}: {}".format(2 * n1, tau(2 * n1)))
# # print("tau {}: {}".format(n2,tau(n2)))
# #
# print("tau^2 {}: {}".format(n1, tau_n_pow(n1, 2)))
# print("tau^2 {}: {}".format(2 * n1, tau_n_pow(2 * n1, 2)))
# # print("tau^2 {}: {}".format(n2, tau_pow(n2, 2)))
#
# print("a018892 {}: {}".format(n1, a018892(n1)))
# print("a018892 {}: {}".format(n2, a018892(n2)))

start_time = time.time()
g = 0
for i in range(1, n1 + 1):
    if i % 100000 == 0:
        print("On n {}".format(i))
    tau = sigma_0_pow(i, 1)
    g += tau
# print("{}: {}".format(n, g))
print("{} {}".format(i, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

start_time = time.time()
g = 0
for i in range(1, n1 + 1):
    if i % 100000 == 0:
        print("On n {}".format(i))
    g += sigma_1(i)
print("{} {}".format(i, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

print("tau {}: {}".format(n1, sigma_0_pow(n1, 1)))
print("tau {}: {}".format(n2, sigma_0_pow(n2, 1)))

print("sigma_0_summatory {}: {}".format(n1, sum_of_sigma_0s(n1)))
# print("sigma_0_summatory {}: {}".format(2000000, sigma_0_summatory(2000000)))
# print("sigma_0_summatory {}: {}".format(n2, sigma_0_summatory(n2)))

start_time = time.time()
g = 0
print("\tA00005\tA00005\tA000005\tA048691\tA000203\tA001157")
for i in range(1, 10 + 1):
    if i % 100000 == 0:
        print("On n {}".format(i))
    # g += a018892(n)
    # tau = tau(n)
    # g += tau * tau
    sig = sigma_1(i)
    # tau = tau(n)
    # t0 = sigma_k(n, 0)
    # t0_2 = sigma_0_pow(n, 1)
    # t0sq = sigma_0_pow(n, 2)
    # t1 = sigma_k(n, 1)
    # t2 = sigma_k(n, 2)
    # g += t2
    # print("{}:\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}".format(n, tau, t0,t0_2, t0sq, t1, t2, g))
    print("{} {}".format(i, sig))
# print("{}: {}".format(n, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

# start = time.time()
# g = 1
# for n in range(2, n1 + 1):
#     g += a018892_2(n)
# print("{} {}".format(n, g))
# finish = time.time()
# print("Running Time a018892_2: %.3f seconds" % (finish - start,))

# start = time.time()
# g = 0
# for n in range(1, 100 + 1):
#     if n % 100000 == 0:
#         print("On n {}".format(n))
#     g += tau(n)
# print("{} {}".format(n, g))
# finish = time.time()
# print("Running Time: %.3f seconds" % (finish - start,))