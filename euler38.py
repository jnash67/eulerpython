import itertools
import math

"""
1 digit number times 1,2,3,4,5 can produce a concatenated pandigital
2 digit number times 1,2,3,4
3 digit number times 1,2,3
4 digit number times 1,2
5 digit number times 1
"""

def num_digits(n):
    d = int(math.log10(n))+1
    return d

def isPandigital(numList):
    allstr = ""
    for a in numList:
        allstr = allstr + str(a)
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
                return int(allstr)
    return 0

def make_concatenated_product_and_check(num):
    global maxpan
    global count
    products = []
    l = 0
    for j in range(1,10):
        if (l < 9):
            val = num * j
            products.append(val)
            l = l + num_digits(val)
            if (l >= 9):
                break
    if (l == 9):
        val = isPandigital(products)
        if (val > 0):
            print("concatenated product of {} from 1-{} is pandigital {}".format(num,j,val))
            count += 1
            if (val > maxpan):
                maxpan = val

maxpan = 0
count = 0

for i in range(1,99999):
    make_concatenated_product_and_check(i)

print("Count is "+str(count))
print("Max is " + str(maxpan))
