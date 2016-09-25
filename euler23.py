import math
import itertools

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
            if (x != val) and (y!=val):
                divList.append(val)
        y += 1
    # print(divList)
    return divList

def number_of_proper_divisors(x):
    return len(findAllProperDivisors(x))


print(findAllProperDivisors(4))
sumOfAll = 0
numPerf = 0
numAbun = 0
numDefic = 0
abundants = []
positiveIntNotSum = list(range(1, 28124))
for i in range(1,28124):
    divList = findAllProperDivisors(i)
    a1 = sum(divList)
    #if a1<1 then we've already checked it for amiability
    if (a1 == i):
        #print("{} is perfect".format(i))
        numPerf +=1
    elif not(i < a1):
        #print("{} is deficient with sum of proper divisors {}".format(i, a1))
        numDefic +=1
    else:
        #print("{} is abundant with sum of proper divisors {}".format(i, a1))
        numAbun +=1
        abundants.append(i)

print(abundants)
print("There are {} abundants under 28124".format(len(abundants)))

for c in itertools.combinations_with_replacement(abundants,2):
    sumOfAbundant = c[0] + c[1]
    if (sumOfAbundant in positiveIntNotSum):
        i = positiveIntNotSum.index(sumOfAbundant)
        del positiveIntNotSum[i]
        #print ("Deleting {}. It is the sum of two abundant numbers. There are {} remaining.".format(sumOfAbundant, len(positiveIntNotSum)))

remaining = len(positiveIntNotSum)
sumOfRemaining = sum(positiveIntNotSum)
print(positiveIntNotSum)
"""
v. slow program. brute force of
There are 1456 positive ints under 28124 that cannot be written as the sum of two abundant numbers
The sum of these are 4179871
In the range there are 4 perfects, 21154 deficients, and 6965 abundants

We iterate through 6965 (num) choose 2 (r) with replacement permutations which is a total of  (num + r - 1)!/r!(num-1)!
6966!/2!6965! = 24,259,095
"""
print("There are {} positive ints under 28124 that cannot be written as the sum of two abundant numbers".format(remaining))
print("The sum of these are {}".format(sumOfRemaining))
print("In the range there are {} perfects, {} deficients, and {} abundants".format(numPerf, numDefic, numAbun))
