import math
import numpy as np

maxK = 12000
maxNumber = 2 * maxK

numFactors = int(math.log(maxNumber, 2))
factors = np.zeros(numFactors)

k = np.zeros(2*(maxK + 1))
k[1] = 0
factors[0] = 1
curMaxFactor = 1
j = 0

while True:
    if j == 0:
        if curMaxFactor == numFactors:
            break
        if factors[0] < factors[1]:
            factors[0] += 1
        else:
            curMaxFactor += 1
            factors[curMaxFactor - 1] = float("inf")
            factors[0] = 2

        j += 1
        factors[1] = factors[0] - 1
    elif j == curMaxFactor - 1:
        factors[j] += 1
        sumfactors = np.sum(factors)
        prodfactors = np.prod(factors)
        if prodfactors > maxNumber:
            j -= 1
        else:
            pk = prodfactors - sumfactors - curMaxFactor
            if pk <= maxK and prodfactors < k[pk]:
                k[pk] = prodfactors
    elif factors[j] < factors[j + 1]:
        factors[j] += 1
        factors[j + 1] = factors[j] - 1
        j += 1
    elif factors[j] >= factors[j + 1]:
        j -= 1

distinctSet = set()
for i in range(0, maxK+1):
    distinctSet.add(k[i])
print("Sum is {}".format(sum(distinctSet)))