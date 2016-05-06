
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

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def num_digits(n):
    d = int(math.log10(n))+1
    return d

def rotateOne(num, d):
    strval = str(num)
    rot = strval[d-1]+strval[0:d-1]
    return int(rot)


countCirc = 0
#lim = 100
lim = 1000000
for next_prime in get_primes(2):
    if next_prime < lim :
        d = num_digits(next_prime)
        p = next_prime
        circ = True
        for i in range(0, d-1):
            p = rotateOne(p,d)
            if not(is_prime(p)):
                circ = False
                break
        # if we make it here all rotations are prime
        if circ:
            print("{} is circular".format(next_prime))
            countCirc += 1
    else:
        break
print("There are {} circular primes under {}".format(countCirc, lim))
