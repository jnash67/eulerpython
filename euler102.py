import eulerutils as eu
import sortedcontainers as sc
import csv
import itertools


def line(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    yintercept = y1 - (slope * x1)
    xintercept = -yintercept / slope
    return (slope, yintercept, xintercept)


def through_origin(x1, y1, x2, y2, x3, y3):
    if not ((x1 > 0 and x2 > 0 and x3 > 0) or (x1 < 0 and x2 < 0 and x3 < 0) or (y1 > 0 and y2 > 0 and y3 > 0) or (
                        y1 < 0 and y2 < 0 and y3 < 0)):
        l1 = line(x1, y1, x2, y2)
        l2 = line(x2, y2, x3, y3)
        l3 = line(x3, y3, x1, y1)
        if l1[1] <= 0 and l1[2] <= 0:
            if (l2[1] >= 0 and l2[2] >= 0) or (l3[1] >= 0 and l3[2] >= 0):
                return True
        if l1[1] >= 0 and l1[2] >= 0:
            if (l2[1] <= 0 and l2[2] <= 0) or (l3[1] <= 0 and l3[2] <= 0):
                return True
        if l2[1] <= 0 and l2[2] <= 0:
            if (l1[1] >= 0 and l1[2] >= 0) or (l3[1] >= 0 and l3[2] >= 0):
                return True
        if l2[1] >= 0 and l2[2] >= 0:
            if (l1[1] <= 0 and l1[2] <= 0) or (l3[1] <= 0 and l3[2] <= 0):
                return True
        if l3[1] <= 0 and l3[2] <= 0:
            if (l1[1] >= 0 and l1[2] >= 0) or (l2[1] >= 0 and l2[2] >= 0):
                return True
        if l3[1] >= 0 and l3[2] >= 0:
            if (l1[1] <= 0 and l1[2] <= 0) or (l2[1] <= 0 and l2[2] <= 0):
                return True
        print("({},{}), ({},{}), ({},{})".format(x1, y1, x2, y2, x3, y3))
    return False


print(through_origin(448,617,-988,0,-103,-504))

file = "p102_triangles.txt"
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        x3 = int(row[4])
        y3 = int(row[5])
        if through_origin(x1, y1, x2, y2, x3, y3):
            count += 1

print("Total count is {}".format(count))
