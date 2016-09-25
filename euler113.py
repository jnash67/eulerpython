import math

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
count_not_bouncy = 0
not_bouncy = set()
for n in range(1,int(math.pow(10,6))):
    if n % 1000 == 0:
        print("Done {}".format(n))
    if is_increasing(n) or is_decreasing(n):
        count_not_bouncy += 1
        not_bouncy.add(n)
print("n<{} num_not_bouncy:{}".format(1000, count_not_bouncy))
print("{}".format(not_bouncy))