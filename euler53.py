import eulerutils as eu
import math

count = 0
for n in range(1, 101):
    for r in range(1, n):
        c = eu.number.choose(n,r)
        if c > 1000000:
            count += 1
print("The count is {}".format(count))