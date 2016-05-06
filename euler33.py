import itertools

digitsSet = {1,2,3,4,5,6,7,8,9}
count = 0
epsilon = 0.000000000001
sumnum = 1
sumdiv = 1
# we want combinations with replacement because 22 is valid
for subset1 in itertools.permutations(digitsSet, 2):
    for subset2 in itertools.permutations(digitsSet,2):
        numerator = subset1[0]*10+subset1[1]
        divisor = subset2[0]*10+subset2[1]
        if (numerator < divisor):
            fraction = numerator / divisor
            cfrac = 0
            if (subset1[0] == subset2[0]):
                # get rid of the equal ones and use the others
                cnum = subset1[1]
                cdiv = subset2[1]
                cfrac = cnum / cdiv
            elif (subset1[0] == subset2[1]):
                cnum = subset1[1]
                cdiv = subset2[0]
                cfrac = cnum / cdiv
            elif (subset1[1]==subset2[0]):
                cnum = subset1[0]
                cdiv = subset2[1]
                cfrac = cnum / cdiv
            elif (subset1[1]==subset2[1]):
                cnum = subset1[0]
                cdiv = subset2[0]
                cfrac = cnum / cdiv
            if (cfrac > 0):
                if abs(cfrac-fraction)<epsilon:
                    sumnum = sumnum * numerator
                    sumdiv = sumdiv * divisor
                    print("{}/{} and {}/{}".format(numerator,divisor,cnum, cdiv))
                    print("fraction 1: {}    fraction 2: {}".format(fraction, cfrac))

print("product of the four is {}/{}".format(sumnum, sumdiv))
sumfrac = sumnum / sumdiv
print("fraction is: {}".format(sumfrac))
# .01, so denom is 100