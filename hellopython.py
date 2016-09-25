import random
import sys
import os
import math
import functools
import euler10
import itertools


def divisorGeneratorDumb(n):
    for i in range(1,n//2+1):
        if n%i == 0: yield i
    yield n

def triangular_number(n):
    return n * (n + 1) // 2

# def divisorGenSmart(num):
#     factors = list(factorGenerator(num))
#     nfactors = len(factors)
#     f = [0] * nfactors
#     while True:
#         yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
#         i = 0
#         while True:
#             f[i] += 1
#             if f[i] <= factors[i][1]:
#                 break
#             f[i] = 0
#             i += 1
#             if i >= nfactors:
#                 return

# for i in divisorGeneratorDumb(100):
#     print(i)
def chunk(seq, chunksize, process=iter):
    """ Yields items from an iterator in iterable chunks."""
    it = iter(seq)
    while True:
        yield process(itertools.chain([it.next()], itertools.islice(it, chunksize - 1)))

# num = 6965
# r = 2
# answer = math.factorial(num+r-1)/(math.factorial(r)*math.factorial(num-1))
# print(answer)

lst = ['a', 'b', 'c', 'd', 'e', 'f']
for i in chunk(lst, 2, list):
    print(i)