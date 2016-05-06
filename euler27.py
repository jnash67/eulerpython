import itertools
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

coefs = list(range(-1000,1000))

maxcount = 0
maxa = 0
maxb = 0
for c in itertools.combinations_with_replacement(coefs,2):
    a = c[0]
    b = c[1]
    prime = True
    i = 1
    count = 0
    while prime:
        val = i*i + a*i + b
        if (is_prime(val)):
            # prime remains true
            count += 1
            i += 1
        else:
            prime = False
    if (count > maxcount):
        maxcount = count
        maxa = a
        maxb = b
        print("Current max is {} primes with coefs a {} and b {}".format(maxcount, maxa,maxb))

print("Max max is {} primes with coefs a {} and b {}".format(maxcount, maxa,maxb))
print("Product of coefficients is " + str(maxa*maxb))