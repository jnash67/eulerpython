import itertools
import numpy as np


# must be odd
size = 1001
n = np.zeros((size,size))

count = 1
spirals = size // 2 + 1
spiralCount = 1
x = size // 2
y = size // 2
n[x,y]=count

while spiralCount < spirals:
    # go right once always
    y+=1
    count+=1
    n[x,y]=count

    # go down (2 * spiralCount) -1 times
    for i in range(0, (2*spiralCount)-1):
        x+=1
        count+=1
        n[x,y]=count
       
    # go left 2 * spiralCount times
    for i in range(0, (2*spiralCount)):
        y-=1
        count+=1
        n[x,y]=count

    # go up 2 * spiralCount times
    for i in range(0, (2*spiralCount)):
        x-=1
        count+=1
        n[x,y]=count

    # go right 2 * spiralCount times
    for i in range(0, (2*spiralCount)):
        y+=1
        count+=1
        n[x,y]=count

    spiralCount += 1

print(n)
sum = 0
for i in range(0, size):
    sum = sum + n[i][i]
    sum = sum + n[i][size-1-i]

# we subtract one because we double count the center which is always 1
sum = sum - 1

print("Sum of diagonals of spiral is " + str(sum))
