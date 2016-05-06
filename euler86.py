import eulerutils as eu
import math

epsilon = 0.000000000001


def is_perfect_square(i):
    global epsilon
    # if not perfect square then add
    if math.sqrt(i) - int(math.sqrt(i)) < epsilon:
        return True
    return False

#perfect_square_cuboids = set()
M = 90
count = 0
for x in range(1, M + 1):
    for y in range(x, M + 1):
        for z in range(y, M + 1):
            p1 = x * x + (y + z) ** 2
            p2 = y * y + (x + z) ** 2
            p3 = z * z + (x + y) ** 2
            minp = min(p1,p2,p3)
            if is_perfect_square(minp):
                #perfect_square_cuboids.add((x, y, z))
                #print("cuboid {},{},{} has min path {}".format(x,y,z,math.sqrt(minp)))
                count+=1

print("Total count is {} for M={}".format(count, M))
prev_count = count
M = 91
while True:
    count = prev_count
    for x in range(1, M + 1):
        for y in range(x, M + 1):
            for z in range(M, M + 1):
                p1 = x * x + (y + z) ** 2
                p2 = y * y + (x + z) ** 2
                p3 = z * z + (x + y) ** 2
                minp = min(p1, p2, p3)
                if is_perfect_square(minp):
                    # print("cuboid {},{},{} has min path {}".format(x,y,z,math.sqrt(minp)))
                    count += 1
    print("Total count is {} for M={}".format(count, M))
    if count > 1000000:
        break
    prev_count = count
    M += 1
