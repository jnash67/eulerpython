import math
import itertools
from . import number
from . import primes
from . import numtext
from . import collectionutils
from . import pandigital
from . import cards
from . import spiral
from . import encrypt
from . import convergent
from . import timing
from . import binary_tree
from . import graph
from . import rpn
from . import rpnconvert


def dec_to_bin(x):
    return int(bin(x)[2:])


def triangular_number(n):
    return n * (n + 1) // 2


def square_number(n):
    return n * n


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def hexagonal_number(n):
    return n * (2 * n - 1)


def heptagonal_number(n):
    return n * (5 * n - 3) // 2


def octagonal_number(n):
    return n * (3 * n - 2)


def collatz(n):
    yield n
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        yield n


# def fibonacci_with_f0equals0(n):
#     if (n == 0):
#         return 0
#
#
#     return 0, fibonacci(n)


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a
