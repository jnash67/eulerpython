import collections
import math
import eulerutils.primes
import sympy

prime_exponent_dicts = collections.defaultdict(dict)
mobius_dict = collections.defaultdict(int)
divisors_dict = collections.defaultdict(list)


# This is intended to hold miscellaneous number theory stuff that doesn't
# fit well in the main primes module

# Ramanujan tau is A000594: http://oeis.org/A000594
# From http://mathworld.wolfram.com/TauFunction.html
# Ramanujan gave the computationally efficient triangular recurrence formula
# (num-1)tau(num)=sum_(m=1)^(b_n)(-1)^(m+1)(2m+1)×[num-1-9/2m(m+1)]tau(num-1/2m(m+1))
# where: b_n=1/2(sqrt(8n+1)-1)
def ramanujan_tau(n):
    if n == 1:
        return 1
    s = 0
    bn = (int(math.sqrt(8 * n + 1)) - 1) // 2
    for m in range(1, bn + 1):
        t1 = math.pow(-1, m + 1)
        t2 = 2 * m + 1
        t3 = n - 1 - ((9 / 2) * m * (m + 1))
        n2 = n - ((m * (m + 1)) // 2)
        s += t1 * t2 * t3 * ramanujan_tau(n2)
    return int(s / (n - 1))


def A046079(n):
    if n % 2 == 0:
        return (eulerutils.primes.tau((n / 2) * (n / 2)) - 1) // 2
    else:
        return (eulerutils.primes.tau(n * n) - 1) // 2


def A018892(nval):
    return (sigma_k(int(nval * nval), 0) + 1) // 2


# partial sum of A018892
def A182082(nval):
    sumsig = fast_sum_of_sigma_0s_for_nsquared(nval)
    return (sumsig + nval) // 2


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


# this is summatory of tau. A fast special formula.
# http://math.stackexchange.com/questions/850135/tau-summatory-function
def sum_of_sigma_0s(nval):
    s = math.floor(math.sqrt(nval))
    return int(2 * S(nval, 1, s) - math.pow(s, 2))


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
    zmax = math.floor(math.pow(nval, 1 / 3))
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


def S(nval, x1val, x2val):
    lval = 0
    for xval in range(x1val, x2val + 1):
        lval += math.floor(nval / xval)
    return lval
