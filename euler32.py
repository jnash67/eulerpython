import itertools

"""
1 digit number times a 1 digit number will produce a 1 or 2 digit number
1d * 1d >= 1d <= 2d <==== CANNOT produce 9 digit pandigital of multiplicand/multiplier/product
1d * 2d >= 2d <= 3d <==== CANNOT produce 9 digit pandigital of multiplicand/multiplier/product
1d * 3d >= 3d <= 4d <==== CANNOT
2d * 2d >= 2d <= 3d <==== CANNOT
2d * 3d >= 4d <= 5d <==== CAN
1d * 4d >= 4d <= 5d <==== CAN
2d * 4d >= 5d <= 6d <==== CANNOT
1d * 5d >= 5d <= 6d <==== CANNOT
3d * 3d >= 5d <= 6d <==== cannot produce 9 digit pandigital of multiplicand/multiplier/product
"""

def checkResult(multiplicand, multiplier):
    product = multiplicand * multiplier
    strprod = str(product)
    allstr = str(multiplicand)+str(multiplier)+str(product)
    resultSet = set()
    found = True
    for char in allstr:
        if char in resultSet:
            found = False
        else:
            resultSet.add(char)
    if found:
        if len(resultSet)==9:
            if not('0' in resultSet):
                # we have one
                print("{} * {} = {} is pandigital".format(multiplicand, multiplier, product))
                return product
    return 0

digitsSet = {1,2,3,4,5,6,7,8,9}
count = 0
sumOfProducts=0
uniqueProducts = set()
# we want permutations because 19 is different from 91
for subset1 in itertools.permutations(digitsSet, 2):
    for subset2 in itertools.permutations(digitsSet,3):
        multiplicand = subset1[0]*10+subset1[1]
        multiplier = subset2[0]*100+subset2[1]*10+subset2[2]
        sum = checkResult(multiplicand, multiplier)
        if (sum >0):
            count+=1
            uniqueProducts.add(sum)
            sumOfProducts += sum

for subset1 in itertools.permutations(digitsSet, 1):
    for subset2 in itertools.permutations(digitsSet,4):
        multiplicand = subset1[0]
        multiplier = subset2[0]*1000+subset2[1]*100+subset2[2]*10+subset2[3]
        sum = checkResult(multiplicand, multiplier)
        if (sum >0):
            count+=1
            uniqueProducts.add(sum)
            sumOfProducts += sum

print("Total is "+str(count))
print("Sum of products is " + str(sumOfProducts))
uniqueSum = 0
for i in uniqueProducts:
    uniqueSum += i
print("Sum of unique products is " + str(uniqueSum))