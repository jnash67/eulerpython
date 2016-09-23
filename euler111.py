import collections
import math
import eulerutils
import time

# we won't be calculating above 10 digits
highest_max = 10
# we store values for each digit and for each possible max so we don't have to
# iterate through the primes twice since we don't know the actual max num of repeated digits
# until we fully iterate once.
M = collections.defaultdict(dict)
# there are 9 rows, 1 for each digit, and highest_max columns
N = [[0 for j in range(0, highest_max)] for i in range(0, 10)]
S = [[0 for j in range(0, highest_max)] for i in range(0, 10)]
sum_of_S = 0
str_digits = [str(i) for i in range(0,10)]
for digit in str_digits:
    M[digit] = 0

# i.e. in a d digit number, the maximum possible number of repeated str_digits is d
for max_possible_repeated in range(4, highest_max+1):
    start_time = time.time()
    n1 = int(math.pow(10, max_possible_repeated - 1))
    n2 = int(math.pow(10, max_possible_repeated))
    primes = eulerutils.primes.very_fast_numpy_primes_less_than(n2)
    print("{}".format(len(primes)))

    print("Digit, d\t\tM({},d)\t\tN({},d)\t\tS({},d)".format(max_possible_repeated, max_possible_repeated,
                                                             max_possible_repeated, max_possible_repeated))
    for digit in str_digits:
        int_digit = int(digit)
        for int_p in primes:
            str_p = str(int_p)
            num = str_p.count(digit)
            if num > M[digit]:
                M[digit] = num
            # we don't know if num is the absolute max, so let's increment
            # the max count and sum for all possible maxes
            if num > 1:
                for i in range(1, num+1):
                    N[int_digit][i-1] += 1
                    S[int_digit][i-1] += int_p
        max = M[digit]
        sum_of_S += S[int_digit][max-1]
        print("{}\t\t\t\t{}\t\t\t{}\t\t\t{}".format(digit, M[digit], N[int_digit][max-1], S[int_digit][max-1]))
        finish_time = time.time()
        print("Running Time: %.3f seconds" % (finish_time - start_time))
    print("Sum of all is {}".format(sum_of_S))
