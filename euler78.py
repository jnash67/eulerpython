import eulerutils as eu
import numpy as np

# partitioning problem similar to #31 & #76 & 77
# See: http://mathworld.wolfram.com/PartitionFunctionP.html
pdict = {}
# plist = [1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
plist = [1, 1, 2, 3, 5, 7, 11, 15, 22]
n = 0
for p in plist:
    pdict[n] = p
    n += 1

# use euler recurrence relation
#  P(num)=sum_(k=1)^num(-1)^(k+1)[P(num-1/2k(3k-1))+P(num-1/2k(3k+1))]
while True:
    sum = 0
    for k in range(1, n + 1):
        f1 = (1 / 2) * k * (3 * k - 1)
        f2 = (1 / 2) * k * (3 * k + 1)
        index1 = int(n - f1)
        index2 = int(n - f2)
        if index1 < 0:
            dictval1 = 0
        else:
            dictval1 = pdict[index1]
        if index2 < 0:
            dictval2 = 0
        else:
            dictval2 = pdict[index2]
        if index1 < 0 and index2 < 0:
            break
        if (k + 1) % 2 == 0:
            sum += dictval1 + dictval2
        else:
            sum -= dictval1 + dictval2

    pdict[n] = sum
    if sum % 1000000 == 0:
        break
    n += 1

print("Answer is: " + str(n))
