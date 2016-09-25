import collections
import math
import time
import sympy
import fractions

prime_exponent_dicts = collections.defaultdict(dict)
mobius_dict = collections.defaultdict(int)
divisors_dict = collections.defaultdict(list)


# In problem 108 and 110 we worked with OEIS A018892, Number of ways to write 1/num as a sum of exactly
# 2 unit fractions. That page points out that the series is is equivalent to the number of pairs (x,y)
# such that LCM(x,y)=num.  So OEIS 018892 is part of the answer to this question as well.
# This involves A182082, A061503, A048691

# sigma_1(ab) = sigma_1(a)*sigma_1(b)
# A018892 = (sigma_0(num^2)+1)//2
# g(num) is the sum of the A018892s from 1 to num inclusive.
#
# we are given g(10^6) = 37429395.
# since g is a summation over sigma_0 which is multiplicative, it too is multiplicative

def A018892(nval):
    return (sigma_k(int(nval * nval), 0) + 1) // 2


def A018892_2(nval):
    return (sigma_0_pow(nval, 2) + 1) // 2


# partial sum of A018892
def A182082(nval):
    sumsig = fast_sum_of_sigma_0s_for_nsquared(nval)
    return (sumsig + nval) // 2


# sigma_0 aka tau
# def fast_sigma_0(num):
#     if num == 1:
#         return 1
#     pd = prime_factors_dict(num)
#     s0mult = 1
#     for p, e in pd.items():
#         s0mult *= (e + 1)
#     return int(s0mult)


# sigma_0 aka tau
# def sigma_0(nval):
#     return divisor_count(nval)

# Number of distinct primes dividing num. http://oeis.org/A001221
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
    return s0sq - s0


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



# sigma_0(num^p). sigma_0_pow(num,1)=sigma_0(num)=tau(num)=tau_2(num) -> http://oeis.org/A000005
# sigma_0_pow(num,2)=sigma_0(num^2)=http://oeis.org/A048691
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


# sigma_k(num,0)=sigma_0(num)=count of divisors of num -> A000005
# sigma_k(num,1)=sigma_1(num)=sum of divisors of num -> A000203
# sigma_k(num,2)=sigma_2(num)=sum of squares of divisors of num -> A001157
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


def S(nval, x1val, x2val):
    lval = 0
    for xval in range(x1val, x2val + 1):
        lval += math.floor(nval / xval)
    return lval


# this is summatory of tau. A fast special formula.
# http://math.stackexchange.com/questions/850135/tau-summatory-function
# https://oeis.org/A006218
def sum_of_sigma_0s(nval):
    s = math.floor(math.sqrt(nval))
    return int(2 * S(nval, 1, s) - math.pow(s, 2))


# http://oeis.org/A061503
def sum_of_sigma_0s_for_nsquared_using_omega(nval):
    # Sum(i=1..num, 2 ^ omega(i) * floor(num / i))
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
# algorithm from: https://math.stackexchange.com/questions/133630/divisor-summatory-function-for-squares
# There's a bug here.  It's off by 1 for num = 10^6 (i.e. 37429394 instead of 37429395) and
# num = 10^12 but not many other values including 2*10^6. I suspect it's some rounding error for some large numbers.
def fast_sum_of_sigma_0s_for_nsquared(nval):
    sqrtn = math.floor(math.sqrt(nval))
    lval = 0
    for a in range(1, sqrtn + 1):
        if a % 100000 == 0:
            print("On num {}".format(a))
        if a in mobius_dict:
            mob = mobius_dict[a]
        else:
            mob = int(sympy.mobius(a))
            mobius_dict[a] = mob
        # fast_sum_of_tau_3 is slower for small a's.  As a increases, it speeds up.
        if mob != 0:
            lval += mob * fast_sum_of_tau_3(math.floor(nval / math.pow(a, 2)))
    return int(lval)


# http://oeis.org/A061201
# This is the sum of tau_3(num) aka d_3(num) which is A007425
def fast_sum_of_tau_3(nval):
    lval = 0
    zmax = math.floor(math.pow(nval, fractions.Fraction(1, 3)))
    for z in range(1, zmax + 1):
        s = math.floor(math.sqrt(nval / z))
        lval += 2 * S(math.floor(nval / z), z + 1, s) - math.pow(s, 2) + math.floor(nval / math.pow(z, 2))
    lval *= 3
    lval += math.pow(zmax, 3)
    return int(lval)


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
    # s0sq2 = sigma_0_nsquared(nval)
    print("tau/sigma_0(num) {}: {}".format(nval, s0))
    print("tau^2(num) {}: {}".format(nval, s0sq))
    # print("tau^2(num) using mobius {}: {}".format(nval, s0sq2))
    print("sum of sigma_0s(num) {}: {}".format(nval, sum_of_sigma_0s(nval)))
    # print("sum_of_sigma_0s_squared(num) {}: {}".format(nval, fast_sum_of_sigma_0s_for_nsquared(nval)))
    print("sum of A018892(num) {}: {}".format(nval, A182082(nval)))
    print("=================")


start_time = time.time()
for i in range(1, 100 + 1):
    ans = A182082(i)
    sig = fast_sum_of_sigma_0s_for_nsquared(i)
    print("{} {} {}".format(i, sig, ans))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

n0 = int(math.pow(10, 4))
n1 = int(math.pow(10, 6))
n2 = int(math.pow(10, 12))

start_time = time.time()
print("sum of A018892(num) {}: {}".format(n2, A182082(n2)))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

stats(10)
stats(n0)
stats(n1)
stats(2000000)
stats(n2)

# sumtau = 0
# sumtausq = 0
# for num in range(1, 10 + 1):
#     if num % 100000 == 0:
#         print("On num {}".format(num))
#     tau = fast_sigma_0(num)
#     t2 = fast_sigma_0(num * num)
#     sumtau += tau
#     sumtausq += t2
# # print("{}: {}".format(num, g))
# print("num:{} sum of tau(num):{}  sum of tau(num^2):{}".format(10, sumtau, sumtausq))
# finish = time.time()

start_time = time.time()
sumtau = 0
sumtausq = 0
for i in range(1, n1 + 1):
    if i % 100000 == 0:
        print("On num {}".format(i))
    # tau, tausq = sigma_0_and_sigma_0_squared(i)
    tau = sigma_0_pow(i, 1)
    tausq = sigma_0_pow(i, 2)
    sumtau += tau
    sumtausq += tausq
print("num:{} sum of tau(num):{}  sum of tau(num^2):{}".format(n1, sumtau, sumtausq))
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
# print("\nPrime Factors of Multiple between Sum(Tau(num)^2)/sum(Tau(num))")
# print("Prime Factors {}:{}".format(376197, prime_factors_dict(376197)))
# print("Prime Factors {}:{}".format(463463, prime_factors_dict(463463)))
# print("Prime Factors {}:{}".format(898597, prime_factors_dict(898597)))
#
# print("\nPrime Factors of Sum(Tau(num))")
# print("Prime Factors {}:{}".format(13970034, prime_factors_dict(13970034)))
# print("Prime Factors {}:{}".format(29326296, prime_factors_dict(29326296)))
# print("Prime Factors {}:{}".format(27785452449086, prime_factors_dict(27785452449086)))
#
# print("\nPrime Factors of Sum(Tau(num^2))")
# print("Prime Factors {}:{}".format(73858790, prime_factors_dict(73858790)))
# print("Prime Factors {}:{}".format(161230032, prime_factors_dict(161230032)))
#
# print("\nPrime Factors of Sum(Tau(num)^2)")
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
        print("On num {}".format(i))
    tau = sigma_0_pow(i, 1)
    g += tau
# print("{}: {}".format(num, g))
print("{} {}".format(i, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

start_time = time.time()
g = 0
for i in range(1, n1 + 1):
    if i % 100000 == 0:
        print("On num {}".format(i))
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
        print("On num {}".format(i))
    # g += a018892(num)
    # tau = tau(num)
    # g += tau * tau
    sig = sigma_1(i)
    # tau = tau(num)
    # t0 = sigma_k(num, 0)
    # t0_2 = sigma_0_pow(num, 1)
    # t0sq = sigma_0_pow(num, 2)
    # t1 = sigma_k(num, 1)
    # t2 = sigma_k(num, 2)
    # g += t2
    # print("{}:\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}\tau\tau{}".format(num, tau, t0,t0_2, t0sq, t1, t2, g))
    print("{} {}".format(i, sig))
# print("{}: {}".format(num, g))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

# start = time.time()
# g = 1
# for num in range(2, n1 + 1):
#     g += a018892_2(num)
# print("{} {}".format(num, g))
# finish = time.time()
# print("Running Time a018892_2: %.3f seconds" % (finish - start,))

# start = time.time()
# g = 0
# for num in range(1, 100 + 1):
#     if num % 100000 == 0:
#         print("On num {}".format(num))
#     g += tau(num)
# print("{} {}".format(num, g))
# finish = time.time()
# print("Running Time: %.3f seconds" % (finish - start,))
