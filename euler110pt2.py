import math
import itertools
import eulerutils.primes

# it is OEIS secquence A018892: http://oeis.org/A018892
# There it says that one formula for the sequence is: a(n) = (tau(n^2)+1)/2

def a018892(n):
    return (eulerutils.primes.tau(int(n * n)) + 1) // 2

def a046079(n):
    if n % 2 == 0:
        return (eulerutils.primes.tau((n / 2) * (n / 2)) - 1) // 2
    else:
        return (eulerutils.primes.tau(n * n) - 1) // 2

count = 0;
max_count_so_far =0
n = 28539043018409500000-83268967541760
solutions_to_exceed = 4000000
while count < solutions_to_exceed:
    n += 83268967541760
    count = a018892(n)
    if count > max_count_so_far:
        max_count_so_far = count
        print("{} {}".format(n, count))
print("{} {}".format(n, count))