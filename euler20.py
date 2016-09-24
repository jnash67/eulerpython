import math

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


n = 100
fact = math.factorial(n)
sum = sum_digits(fact)
print("The factorial is {}".format(fact))
print("Sum of digits is {}".format(sum))