import math

def findAllProperDivisors(x):
    divList = []
    y = 1
    sqrtx = math.sqrt(x)
    while y <= sqrtx:
        if x % y == 0:
            # this screens out 1 which has no proper divisors
            if not(x == y):
                divList.append(y)
            val = int(x/y)
            # don't add x as a divisor. proper divisors are < x
            if not(x == val):
                divList.append(val)
        y += 1
    # print(divList)
    return divList

def number_of_proper_divisors(x):
    return len(findAllProperDivisors(x))


sumOfAll = 0
for i in range(1,10000):
    divList = findAllProperDivisors(i)
    a1 = sum(divList)
    #if a1<1 then we've already checked it for amiability
    if not(a1 < i):
        divList = findAllProperDivisors(a1)
        a2 = sum(divList)
        # then amiable
        if (a2==i) and (a1!=i):
            # then i and a1 are amiable
            print("{} and {} are amiable".format(a1,a2))
            sumOfAll = sumOfAll + a1 + a2
print("Sum is " + str(sumOfAll))
