import functools
import time
import eulerutils as eu
import itertools
import sortedcontainers as sc
import math
import time

# the largest prime less than 50mm is
# x^2 + 2^3 + 2^4 = 50mm

start = time.time()

size = 50000000
maxsq = int(math.sqrt(size)+1)
maxcu = int(math.pow(size, 1 / 3) + 1)
maxqu = int(math.pow(size, 1 / 4) + 1)
expressable = sc.SortedSet()
primesthatcanbesquared = eu.primes.fast_all_primes_less_than(maxsq)
primesthatcanbecubed = eu.primes.fast_all_primes_less_than(maxcu)
primesthatcanbequartic = eu.primes.fast_all_primes_less_than(maxqu)

count = 0
for p1 in primesthatcanbesquared:
    for p2 in primesthatcanbecubed:
        for p3 in primesthatcanbequartic:
            count += 1
            if (count % 1000000 == 0):
                print("{} million iterations".format(count // 1000000))

            val = p1**2 + p2**3 + p3**4
            if val < size:
                expressable.add(val)

print("There are {} expressable that way".format(len(expressable)))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
