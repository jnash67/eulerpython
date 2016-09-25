def is_increasing(n):
    str_n = str(n)
    for i in range(0, len(str_n) - 1):
        d1 = int(str_n[i])
        d2 = int(str_n[i + 1])
        if d2 > d1:
            return False
    return True


def is_decreasing(n):
    str_n = str(n)
    for i in range(0, len(str_n) - 1):
        d1 = int(str_n[i])
        d2 = int(str_n[i + 1])
        if d2 < d1:
            return False
    return True

n = 1
count_bouncy = 0
while True:
    if not is_increasing(n) and not is_decreasing(n):
        count_bouncy += 1
    if count_bouncy / n == (count_bouncy * 100 // n) / 100:
        print("num:{} num_bouncy:{} %:{} mod:{}".format(n, count_bouncy, count_bouncy * 100 // n,
                                                      count_bouncy * 100 % n))
        if (count_bouncy * 100 // n) == 99:
            break
    n += 1
