import eulerutils as eu
import math

epsilon = 0.000000000001
sumAllDigits = 0
for i in range(1,101):
    intsqrt = eu.number.sqroot(i,99)
    strintsqrt = str(intsqrt)
    sumdig = 0
    for d in strintsqrt:
        sumdig += int(d)
    # if not perfect square then add
    if not(math.sqrt(i) - int(math.sqrt(i)) < epsilon):
        print("Adding sum of str_digits for {}".format(i))
        sumAllDigits += sumdig

print("Sum of all str_digits is {}".format(sumAllDigits))