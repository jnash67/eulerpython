import math


def is_increasing(str_num):
    for i in range(0, len(str_num) - 1):
        d1 = int(str_num[i])
        d2 = int(str_num[i + 1])
        if d2 > d1:
            return False
    return True


def is_decreasing(str_num):
    for i in range(0, len(str_num) - 1):
        d1 = int(str_num[i])
        d2 = int(str_num[i + 1])
        if d2 < d1:
            return False
    return True


digits = [str(i) for i in range(0, 10)]
count_not_bouncy = 0
num_digits = 3
max_num_digits = 5
threshold = int(math.pow(10, num_digits))
increasing_with_n_digits = set()
decreasing_with_n_digits = set()
# both increasing and decreasing, e.g. 777
both_with_n_digits = set()
for num in range(1, int(math.pow(10, num_digits + 1))):
    str_num = str(num)
    is_inc = is_increasing(str_num)
    is_dec = is_decreasing(str_num)
    if is_inc and is_dec:
        count_not_bouncy += 1
        if num >= threshold:
            both_with_n_digits.add(str_num)
    elif is_inc:
        count_not_bouncy += 1
        if num >= threshold:
            increasing_with_n_digits.add(str_num)
    elif is_dec:
        count_not_bouncy += 1
        if num >= threshold:
            decreasing_with_n_digits.add(str_num)
print("num_digits <= {} num_not_bouncy:{}".format(threshold, count_not_bouncy))
all = increasing_with_n_digits.union(decreasing_with_n_digits).union(both_with_n_digits)
print("{}".format(all))

for n in range(num_digits + 1, max_num_digits + 1):
    increasing_with_n_plus_one_digits = set()
    decreasing_with_n_plus_one_digits = set()
    both_with_n_plus_one_digits = set()
    for nb in increasing_with_n_digits:
        left_digit = int(nb[0])
        right_digit = int(nb[n - 1])
        # can't add a zero to the left
        for i in range(1, left_digit + 1):
            count_not_bouncy += 1
            increasing_with_n_plus_one_digits.add(digits[i] + nb)
        for i in range(right_digit, 10):
            count_not_bouncy += 1
            increasing_with_n_plus_one_digits.add(nb + digits[i])
    for nb in decreasing_with_n_digits:
        left_digit = int(nb[0])
        right_digit = int(nb[n - 1])
        for i in range(left_digit, 10):
            count_not_bouncy += 1
            decreasing_with_n_plus_one_digits.add(digits[i] + nb)
        for i in range(0, right_digit + 1):
            count_not_bouncy += 1
            decreasing_with_n_plus_one_digits.add(nb + digits[i])
    for nb in both_with_n_digits:
        count_not_bouncy += 1
        both_with_n_plus_one_digits.add(nb + nb[0])

    decreasing_with_n_digits = decreasing_with_n_plus_one_digits
    increasing_with_n_digits = increasing_with_n_plus_one_digits
    both_with_n_digits = both_with_n_plus_one_digits
print("num<{} num_not_bouncy:{}".format(max_num_digits, count_not_bouncy))
# print("{}".format(not_bouncy))
