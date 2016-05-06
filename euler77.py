import eulerutils as eu
import numpy as np

# partitioning problem similar to #31 & #76
# See: http://mathworld.wolfram.com/PartitionFunctionP.html

def ways_to_partition(types, sum):
    n = np.zeros(sum+1)
    n[0]=1
    for k in types:
        for i in range(0,sum-k+1,1):
            n[i+k]=n[i+k]+n[i]
    return n[sum]


result = 0
count = 10
while True:
    primes = eu.primes.all_primes_less_than(count)
    result = ways_to_partition(primes, count)
    print("#{} --> {}".format(count, result))
    if result>5000:
        break
    count += 1

print("Answer is: " + str(count))