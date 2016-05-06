
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

bignum = 2**1000
print("2^1000 is " + str(bignum))
print(sum_digits(bignum))