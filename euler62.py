from collections import Counter
import numpy as np


# must be odd
size = 1001


maxn = 20000
cubes = []
for i in range(0, maxn):
    cubes.append([])

lowestNumOfCubedDigitsDict = {}
for i in range(345,maxn):
    cube = i**3
    sortedstrcube = "".join(sorted(str(cube)))
    if sortedstrcube in lowestNumOfCubedDigitsDict:
        lowestNum = lowestNumOfCubedDigitsDict[sortedstrcube]
        cubes[lowestNum].append(i)
    else:
        lowestNumOfCubedDigitsDict[sortedstrcube] = i
        cubes[i].append(i)

maxcount = 0
for i in cubes:
    count = len(i)
    if (count > maxcount):
        maxcount = count
        print("Biggest so far is {} with {} permutations".format(i, count))
    if (count==5):
        print("The smallest cube with 5 cube permutations is {}^3 or {}".format(i, i[0]**3))

        break

