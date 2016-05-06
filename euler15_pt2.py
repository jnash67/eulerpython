import itertools

gridSize = 3
count = 0
for path in itertools.product('RD', repeat=2*gridSize):
    if list(path).count('R') == gridSize:
        count += 1

print("There are " + str(count) + " paths for a grid of size " + str(gridSize))

