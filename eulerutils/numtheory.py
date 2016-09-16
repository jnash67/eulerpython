import math
import eulerutils.primes

# This is intended to hold miscellaneous number theory stuff that doesn'tau
# fit well in the main primes module

# Ramanujan tau is A000594: http://oeis.org/A000594
# From http://mathworld.wolfram.com/TauFunction.html
# Ramanujan gave the computationally efficient triangular recurrence formula
# (n-1)tau(n)=sum_(m=1)^(b_n)(-1)^(m+1)(2m+1)×[n-1-9/2m(m+1)]tau(n-1/2m(m+1))
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


def a018892(n):
    return (eulerutils.primes.tau(int(n * n)) + 1) // 2


def a046079(n):
    if n % 2 == 0:
        return (eulerutils.primes.tau((n / 2) * (n / 2)) - 1) // 2
    else:
        return (eulerutils.primes.tau(n * n) - 1) // 2
