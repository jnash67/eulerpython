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

def truncLeft(num, d):
    strval = str(num)
    trl = strval[0:d-1]
    return int(trl)

def truncRight(num, d):
    strval = str(num)
    trr = strval[1:d]
    return int(trr)

countTrunc = 0
#lim = 100
lim = 1000000
sumAll = 0
for next_prime in get_primes(9):
    if next_prime < lim :
        d = num_digits(next_prime)
        pl = next_prime
        pr = next_prime
        trunc = True
        for i in range(1, d):
            pl = truncLeft(pl,d-i+1)
            pr = truncRight(pr,d-i+1)
            if not(is_prime(pl)) or not(is_prime(pr)):
                trunc = False
                break
        # if we make it here all rotations are prime
        if trunc:
            print("{} is left and right truncatable".format(next_prime))
            sumAll += next_prime
            countTrunc += 1
    else:
        break
print("There are {} left and right truncatable primes under {}".format(countTrunc, lim))
print("Their sum is {}".format(sumAll))