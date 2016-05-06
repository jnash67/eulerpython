import math
import itertools
import sortedcontainers as sc

triangulars = sc.SortedList()
pentagonals = sc.SortedList()
hexagonals = sc.SortedList()

#for i in range(1,10000000):
maxn = 100000
for i in range(1,maxn):
    triangulars.append(int(i*(i+1)/2))
    pentagonals.append(int(i*(3*i-1)/2))
    hexagonals.append(int(i*(2*i-1)))

for t in triangulars:
    if t in pentagonals:
        if t in hexagonals:
            print("{} is triangular, pentagonal, and hexagonal".format(t))
            indexoft = triangulars.index(t) + 1
            indexofp = pentagonals.index(t) +1
            indexofh = hexagonals.index(t)+1
            print("it is the {}th triangular, the {}th pentagonal, and the {}th hexagonal".format(indexoft,indexofp,indexofh))
        print("{} is triangular and pentagonal but NOT hexagonal".format(t))