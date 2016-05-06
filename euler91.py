import math


# heron's formula
def triangle_area(a, b, c):
    global epsilon
    s = (a + b + c) / 2
    asq = (s * (s - a) * (s - b) * (s - c))
    if (asq < 0):
        if (abs(asq) < epsilon):
            return 0
    A = math.sqrt(asq)
    return A


def the_other_one(x, y, a, b, c):
    if ((x == a) and (y == b)) or ((y == a) and (x == b)):
        return c
    if ((x == b) and (y == c)) or ((y == b) and (x == c)):
        return a
    return b


# triangle must start at origin
grid = 50
epsilon = 0.00001
count = 0
coordinates_set = set()

for x1 in range(0, grid + 1):
    for y1 in range(0, grid + 1):
        for x2 in range(0, grid + 1):
            for y2 in range(0, grid + 1):
                coords = ((x1, y1), (x2, y2))
                reverse_coords = ((x2, y2), (x1, y1))
                if not coords in coordinates_set and not reverse_coords in coordinates_set:
                    coordinates_set.add(coords)
                    dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
                    dist2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                    dist3 = math.sqrt(x2 ** 2 + y2 ** 2)
                    area = triangle_area(dist1, dist2, dist3)
                    if area != 0:
                        hyp = max(dist1, dist2, dist3)
                        a = min(dist1, dist2, dist3)
                        b = the_other_one(hyp, a, dist1, dist2, dist3)
                        if abs(a * a + b * b - hyp * hyp) < epsilon:
                            count += 1
                            print("{},{} , {},{}, {},{}".format(0, 0, x1, y1, x2, y2))
                            print("{} {} {} -> {}".format(dist1, dist2, dist3, area))

print("Count is {}".format(count))
