import itertools
import math

def is_path(pathList):
    gridSize = len(pathList)//2

    # start at top left
    x = 0
    y = 0
    count = 0
    for step in pathList:
        count += 1
        if step == 'R':
            x += 1
        elif step == 'D':
            y += 1
        if (x>gridSize) or (y>gridSize):
            break
        if (x==gridSize) and (y==gridSize) and (count==2*gridSize):
            return True
    return False

print(list(itertools.product('RD', repeat=4)))

# The code below is way too slow
# It's the number of ways to choose exactly half of 2 * gridsize of Rs and Ds
# so it's just num choose k or num! / (k! * (num-k)!) or 40 choose 20 or 40! / (20! * 20!)
answer = math.factorial(40) / (math.factorial(20)**2)
print("answer is " + str(answer))

# p = is_path(('R','R','D','D'))
# print(str(p))
#
# gridSize = 20
# count = 0
# for path in itertools.product('RD', repeat=2*gridSize):
#     p = is_path(path)
#     if p:
#         count += 1
#         print(str(path) + " is path " + str(count))
#
# print("There are " + str(count) + " paths for a grid of size " + str(gridSize))

