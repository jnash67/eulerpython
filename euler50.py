import math
import sortedcontainers as sc
import itertools

def num_digits(n):
    d = int(math.log10(n))+1
    return d

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

# http://stackoverflow.com/questions/464864/python-code-to-pick-out-all-possible-combinations-from-a-list
def all_subsets(ss):
  return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(0, len(ss)+1)))

#http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

primes = sc.SortedList()
primesBelowOneMillion = []
primesThatAreSumOfConsecutivePrimes = {}
gp = get_primes(2)
while True:
    next_prime = next(gp)
    if next_prime < 1000000:
        primesBelowOneMillion.append(next_prime)
    else:
        break

print("There are {} primes below one million".format(len(primesBelowOneMillion)))
print("The first 100 are: {}".format(primesBelowOneMillion[0:100]))
maxcount = 0
for i in range(0, len(primesBelowOneMillion)):
    sumOfConsecutive = primesBelowOneMillion[i]
    count = 1
    for j in range(i+1, len(primesBelowOneMillion)):
        sumOfConsecutive = sumOfConsecutive + primesBelowOneMillion[j]
        if sumOfConsecutive > 1000000:
            break
        count += 1
        if sumOfConsecutive in primesBelowOneMillion:
            if sumOfConsecutive in primesThatAreSumOfConsecutivePrimes:
                existingCount = primesThatAreSumOfConsecutivePrimes[sumOfConsecutive]
                if count > existingCount:
                    primesThatAreSumOfConsecutivePrimes[sumOfConsecutive] = count
            else:
                primesThatAreSumOfConsecutivePrimes[sumOfConsecutive] = count
            if count >= maxcount:
                maxcount = count
                print("{} is the sum of {} consecutive primes".format(sumOfConsecutive, count))

key = keywithmaxval(primesThatAreSumOfConsecutivePrimes)
item = primesThatAreSumOfConsecutivePrimes[key]
print("There are {} primes that are a sum of consecutive primes under 1mm".format(len(primesThatAreSumOfConsecutivePrimes)))
print("The largest one is {} with {} consecutive primes".format(key,item))
