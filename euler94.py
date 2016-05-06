import math
import sortedcontainers as sc


def heron_classic(a, b, c):
    s = (a + b + c) / 2
    A = math.sqrt((s * (s - a) * (s - b) * (s - c)))
    return A


# this variation has less rounding error. sides must be a tuple in descending order e.g. 5,5,4
def heron(t):
    a = t[0]
    b = t[1]
    c = t[2]
    return math.sqrt(((a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c))) / 4)


def is_integral(n):
    global epsilon
    if abs(n - math.floor(n)) < epsilon:
        return True
    return False


billion = 10 ** 9
epsilon = 0.00000001
areaSet = sc.SortedSet()
sumOfPerimeters = 0
for a in range(5, billion):
    perimeter1 = a+a+a+1
    perimeter2 = a+a+a-1

    if perimeter1 <= billion:
        area1 = heron_classic(a,a,a+1)
        if abs(area1 - math.floor(area1)) < epsilon:
            areaSet.add(area1)
            sumOfPerimeters += perimeter1

    if perimeter2 <= billion:
        area2 = heron_classic(a,a,a-1)
        if abs(area2 - math.floor(area2)) < epsilon:
            areaSet.add(area2)
            sumOfPerimeters += perimeter2

    if perimeter1 > billion and perimeter2 > billion:
        break

print("Sum of perimeters is {}".format(sumOfPerimeters))
print("Sum 2 --> {}".format(sum(areaSet)))
