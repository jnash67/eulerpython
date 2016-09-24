import math
import functools


def num_digits(n):
    d = int(math.log10(n)) + 1
    return d


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


# only works for positive n
def last_digit(n):
    return n % 10


# only works for positive n
def last_n_digits(num, n):
    return int(str(num)[-n:])


# only works for positive n
def first_n_digits(num, n):
    return int(str(num)[:n])


def all_n_digit_positive_numbers(n):
    if (n <= 0):
        return None
    return list(range(10 ** (n - 1), 10 ** n))


def find_all_divisors(x):
    if x == 1:
        return [1]
    divList = []
    y = 1
    sqrtx = math.sqrt(x)
    while y <= sqrtx:
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return divList


def find_all_proper_divisors(x):
    divList = []
    y = 1
    sqrtx = math.sqrt(x)
    while y <= sqrtx:
        if x % y == 0:
            # this screens out 1 which has no proper divisors
            if not (x == y):
                divList.append(y)
            val = int(x / y)
            # don't add x as a divisor. proper divisors are < x
            if not (x == val):
                divList.append(val)
        y += 1
    return divList


def number_of_proper_divisors(x):
    return len(find_all_proper_divisors(x))


def choose(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


# from: http://stackoverflow.com/questions/5187664/generating-digits-of-square-root-of-2
# Here is a short version for calculating the square root of an integer a to digits of precision.
# It works by finding the integer square root of a after multiplying by 10 raised to the 2 x digits.
def sqroot(a, digits):
    a *= 10 ** (2 * digits)
    x_prev = 0
    x_next = 1 * (10 ** digits)
    while x_prev != x_next:
        x_prev = x_next
        x_next = (x_prev + (a // x_prev)) >> 1
    return x_next

# generate the factors of an integer
def factors(n):
        step = 2 if n%2 else 1
        return set(functools.reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))


def product(list):
    p = 1
    for i in list:
        p *= i
    return p