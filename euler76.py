import numpy as np

# partitioning problem similar to #31
# See: http://mathworld.wolfram.com/PartitionFunctionP.html

size = 101
#size = 101
n = np.zeros(size)
n[0]=1

types = range(1,100)
#types = [1,5,10,25,50,100]

for k in types:
    for i in range(0,size-k,1):
        n[i+k]=n[i+k]+n[i]
print("Answer is: " + str(n[size-1]))

