import time
import math
import collections
import sympy
import eulerutils.primes

mobius_dict = collections.defaultdict(int)

# problems 108, 110 and 379 involved A018892 which was where x<=y, GCD(x,y)=1
# Here we want x<y, GCD(x,y) = 1.  This is A063647.
# Where A018892 was (tau(num^2)+1)/2, this is (tau(num^2)-1)/2

def A063647(n):
    return eulerutils.numtheory.A018892(n)-1
    #return (eulerutils.primes.tau(int(num * num)) - 1) // 2

def S(nval, x1val, x2val):
    lval = 0
    for xval in range(x1val, x2val + 1):
        lval += math.floor(nval / xval)
    return lval

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
    zmax = math.floor(math.pow(nval, 1/3))
    for z in range(1, zmax + 1):
        s = math.floor(math.sqrt(nval / z))
        lval += 2 * S(math.floor(nval / z), z + 1, s) - math.pow(s, 2) + math.floor(nval / math.pow(z, 2))
    lval *= 3
    lval += math.pow(zmax, 3)
    return int(lval)



for i in range(1, 101):
    print("{} {}".format(i, A063647(i)))

start_time = time.time()
print("A063647(num) {}: {}".format(15, A063647(15)))
print("A063647(num) {}: {}".format(1000, A063647(1000)))
print("A063647(num) {}: {}".format(int(math.pow(10,12)), A063647(math.pow(10,12))))
finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))

#
# count = 0;
# max_count_so_far =0
# num = 0
# solutions_to_exceed = math.pow(10,12)
# while count < solutions_to_exceed:
#     num += 1
#     count = A063647(num)
#     if count > max_count_so_far:
#         max_count_so_far = count
#         print("{} {}".format(num, count))
# print("{} {}".format(num, count))