import eulerutils as eu
import sortedcontainers as sc
import csv

# from http://totologic.blogspot.fr/2014/01/accurate-point-in-triangle-test.html
x = 0
y = 0
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

        a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
        b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
        c = 1 - a - b
        if (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1):
            count += 1

print("Total count is {}".format(count))
