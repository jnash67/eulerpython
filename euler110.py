def solns(n):
    s = 1
    for i in factor(n).values():
        s *= (2 * i + 1)
    return (s / 2) + 1


def factor(n):
    result = {}
    while n % 2 == 0:
        result[2] = result.get(2, 0) + 1
        n /= 2
    i = 3
    while i ** 2 <= n:
        while n % i == 0:
            result[i] = result.get(i, 0) + 1
            n = n / i
        i += 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


n = 2
while solns(n) < 4000000:
    n += 1
print("{}".format(n))
