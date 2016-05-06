import numpy as np

# treat as partitioning problem as per
# http://math.stackexchange.com/questions/15521/making-change-for-a-dollar-and-other-number-partitioning-problems

size = 201
#size = 101
n = np.zeros(size)
n[0]=1

types = [1,2,5,10,20,50,100,200]
#types = [1,5,10,25,50,100]

for k in types:
    for i in range(0,size-k,1):
        n[i+k]=n[i+k]+n[i]
print(n)
print("Answer is: " + str(n[size-1]))

