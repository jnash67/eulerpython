import math
import time
from sortedcontainers import SortedSet

def is_increasing(n):
    str_n = str(n)
    for i in range(0, len(str_n) - 1):
        d1 = int(str_n[i])
        d2 = int(str_n[i + 1])
        if d2 < d1:
            return False
    return True


def is_decreasing(n):
    str_n = str(n)
    for i in range(0, len(str_n) - 1):
        d1 = int(str_n[i])
        d2 = int(str_n[i + 1])
        if d2 > d1:
            return False
    return True


total_start_time = time.time()
num_digits = 3
end_num_digits = 100
# if num_digits = 2 then we want the range to be between 10 and 100, including 10, not including 100.
digits_lower_threshold = int(math.pow(10, num_digits - 1))
digits_upper_threshold = int(math.pow(10, num_digits))
count_not_bouncy = 0
count_bouncy = 0
increasing_with_n_digits = SortedSet()
decreasing_with_n_digits = SortedSet()
# both increasing and decreasing, e.g. 777
both_with_n_digits = SortedSet()
for n in range(1, digits_upper_threshold):
    if n % 1000 == 0:
        print("Done {}".format(n))
    is_inc = is_increasing(n)
    is_dec = is_decreasing(n)
    if is_inc or is_dec:
        count_not_bouncy += 1
        if n >= digits_lower_threshold:
            if is_inc and is_dec:
                both_with_n_digits.add(n)
            elif is_inc:
                increasing_with_n_digits.add(n)
            else:
                decreasing_with_n_digits.add(n)
    else:
        count_bouncy += 1
print("n < {} (10^{}) num_not_bouncy: {} num bouncy {}".format(digits_upper_threshold, digits_lower_threshold,
                                                               count_not_bouncy, count_bouncy))
# print("{}".format(not_bouncy))
len_all = len(increasing_with_n_digits) + len(decreasing_with_n_digits) + len(both_with_n_digits)
# print("{}".format(all))
print("num of just len {} is {}".format(n + 1, len_all))

digits = [str(i) for i in range(0, 10)]
for n in range(num_digits, end_num_digits):
    start_time = time.time()
    increasing_with_n_plus_one_digits = SortedSet()
    decreasing_with_n_plus_one_digits = SortedSet()
    both_with_n_plus_one_digits = SortedSet()
    for nb_int in increasing_with_n_digits:
        nb_char = str(nb_int)
        left_digit = int(nb_char[0])
        right_digit = int(nb_char[n - 1])
        # can't add a zero to the left
        for i in range(1, left_digit + 1):
            new_digit = digits[i]
            new_num = int(new_digit + nb_char)
            increasing_with_n_plus_one_digits.add(new_num)
        for i in range(right_digit, 10):
            new_digit = digits[i]
            new_num = int(nb_char + new_digit)
            increasing_with_n_plus_one_digits.add(new_num)
    for nb_int in decreasing_with_n_digits:
        nb_char = str(nb_int)
        left_digit = int(nb_char[0])
        right_digit = int(nb_char[n - 1])
        for i in range(left_digit, 10):
            new_digit = digits[i]
            new_num = int(new_digit + nb_char)
            decreasing_with_n_plus_one_digits.add(new_num)
        for i in range(0, right_digit + 1):
            new_digit = digits[i]
            new_num = int(nb_char + new_digit)
            decreasing_with_n_plus_one_digits.add(new_num)
    for nb_int in both_with_n_digits:
        nb_char = str(nb_int)
        new_digit = nb_char[0]
        new_num = int(nb_char + new_digit)
        both_with_n_plus_one_digits.add(new_num)
    decreasing_with_n_digits = decreasing_with_n_plus_one_digits
    increasing_with_n_digits = increasing_with_n_plus_one_digits
    both_with_n_digits = both_with_n_plus_one_digits
    count_all = len(increasing_with_n_digits) + len(decreasing_with_n_digits) + len(both_with_n_digits)
    count_not_bouncy += count_all
    count_bouncy = int(math.pow(10, n + 1) - 1) - count_not_bouncy
    print("num < {} (10^{}) num_not_bouncy: {} num bouncy: {} pct not bouncy {} example {}".format(
        int(math.pow(10, n + 1)), n, count_not_bouncy,
        count_bouncy, count_not_bouncy / (math.pow(10, n + 1) - 1), both_with_n_digits[0]))

    # print("{}".format(all))
    print("num of just len {} is {}".format(n + 1, count_all))

    finish_time = time.time()
    print("Running Time: %.3f seconds" % (finish_time - start_time))

total_finish_time = time.time()
print("Running Time: %.3f seconds" % (total_finish_time - total_start_time))