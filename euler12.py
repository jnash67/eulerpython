import math

def divisorGeneratorDumb(n):
    for i in range(1,n//2+1):
        if n%i == 0: yield i
    yield n

def triangular_number(n):
    return n * (n + 1) // 2

def FindAllDivisors(x):
    if (x == 1):
        return [1]
    divList = []
    y = 1
    sqrtx = math.sqrt(x)
    while y <= sqrtx:
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    # print(divList)
    return divList

def number_of_divisors(x):
    return len(FindAllDivisors(x))

# def divisorGenSmart(n):
#     factors = list(factorGenerator(n))
#     nfactors = len(factors)
#     f = [0] * nfactors
#     while True:
#         yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
#         i = 0
#         while True:
#             f[i] += 1
#             if f[i] <= factors[i][1]:
#                 break
#             f[i] = 0
#             i += 1
#             if i >= nfactors:
#                 return

print("hello")
num_divisors = 0
n = 1
while True:
    triangle = triangular_number(n)
    num_divisors = number_of_divisors(triangle)
    print("triangle number {} is {} and has {} divisors".format(n, triangle, num_divisors))
    if (num_divisors > 500):
        break
    n = n + 1

print("done")
# for i in divisorGeneratorDumb(100):
#     print(i)
