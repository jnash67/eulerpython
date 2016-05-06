import eulerutils as eu

# the answer is the number of elements in the Farey sequence minus the first and the last (0 and 1) which is
# 1 + sum(k = 1 to n) totient(k) minus two
# can also get totient function from sy

farey = 1000000
sum = 1
for i in range(1,farey+1):
    t = eu.primes.totient(i)
    sum += t

sum = sum - 2
print("Sum is {}".format(sum))