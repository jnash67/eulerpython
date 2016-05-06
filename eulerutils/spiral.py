import numpy as np
import sortedcontainers as sc


# n must be odd
def create_clockwise_spiral(size):
    if size % 2 == 0:
        print("Size of spiral should be odd")
        size = size + 1

    n = np.zeros((size, size))

    count = 1
    spirals = size // 2 + 1
    spiralCount = 1
    x = size // 2
    y = size // 2
    n[x, y] = count

    # spiralTuple is the spiral, it's x and y positions and the current value
    spiralTuple = n, x, y, count

    while spiralCount < spirals:
        # go right once always
        spiralTuple = spiral_right(spiralTuple, 1)
        # go up (2 * spiralCount) -1 times
        spiralTuple = spiral_down(spiralTuple, (2 * spiralCount) - 1)
        # go left 2 * spiralCount times
        spiralTuple = spiral_left(spiralTuple, 2 * spiralCount)
        # go down 2 * spiralCount times
        spiralTuple = spiral_up(spiralTuple, 2 * spiralCount)
        # go right 2 * spiralCount times
        spiralTuple = spiral_right(spiralTuple, 2 * spiralCount)

        spiralCount += 1

    return n


# n must be odd
def create_counterclockwise_spiral(size):
    if size % 2 == 0:
        print("Size of spiral should be odd")
        size = size + 1

    n = np.zeros((size, size))

    count = 1
    spirals = size // 2 + 1
    spiralCount = 1
    x = size // 2
    y = size // 2
    n[x, y] = count

    # spiralTuple is the spiral, it's x and y positions and the current value
    spiralTuple = n, x, y, count

    while spiralCount < spirals:
        # go right once always
        spiralTuple = spiral_right(spiralTuple, 1)
        # go up (2 * spiralCount) -1 times
        spiralTuple = spiral_up(spiralTuple, (2 * spiralCount) - 1)
        # go left 2 * spiralCount times
        spiralTuple = spiral_left(spiralTuple, 2 * spiralCount)
        # go down 2 * spiralCount times
        spiralTuple = spiral_down(spiralTuple, 2 * spiralCount)
        # go right 2 * spiralCount times
        spiralTuple = spiral_right(spiralTuple, 2 * spiralCount)

        spiralCount += 1

    return n

# top right, top left, bottom left, bottom right
# bottom right is the last number for the next spiral
def new_counterclockwise_spiral_diagonals(size):
    if size % 2 == 0:
        print("Size of spiral should be odd")
        size = size + 1

    n = None
    # set to last number of prev spiral
    count = (size-2)**2
    x = size
    y = size
    spiralCount = size // 2
    diagonals = []

    # spiralTuple is the spiral, it's x and y positions and the current value
    spiralTuple = n, x, y, count

    # go right once always
    spiralTuple = spiral_right(spiralTuple, 1)
    # go up (2 * spiralCount) -1 times
    spiralTuple = spiral_up(spiralTuple, (2 * spiralCount) - 1)
    diagonals.append(spiralTuple[3])

    # go left 2 * spiralCount times
    spiralTuple = spiral_left(spiralTuple, 2 * spiralCount)
    diagonals.append(spiralTuple[3])

    # go down 2 * spiralCount times
    spiralTuple = spiral_down(spiralTuple, 2 * spiralCount)
    diagonals.append(spiralTuple[3])

    # go right 2 * spiralCount times
    spiralTuple = spiral_right(spiralTuple, 2 * spiralCount)
    diagonals.append(spiralTuple[3])

    return diagonals


def spiral_right(spiralTuple, numTimes):
    spiral = spiralTuple[0]
    x = spiralTuple[1]
    y = spiralTuple[2]
    currentVal = spiralTuple[3]
    for i in range(0, numTimes):
        y += 1
        currentVal += 1
        if not spiral is None:
            spiral[x, y] = currentVal
    return spiral, x, y, currentVal


def spiral_down(spiralTuple, numTimes):
    spiral = spiralTuple[0]
    x = spiralTuple[1]
    y = spiralTuple[2]
    currentVal = spiralTuple[3]
    for i in range(0, numTimes):
        x += 1
        currentVal += 1
        if not spiral is None:
            spiral[x, y] = currentVal
    return spiral, x, y, currentVal


def spiral_left(spiralTuple, numTimes):
    spiral = spiralTuple[0]
    x = spiralTuple[1]
    y = spiralTuple[2]
    currentVal = spiralTuple[3]
    for i in range(0, numTimes):
        y -= 1
        currentVal += 1
        if not spiral is None:
            spiral[x, y] = currentVal
    return spiral, x, y, currentVal


def spiral_up(spiralTuple, numTimes):
    spiral = spiralTuple[0]
    x = spiralTuple[1]
    y = spiralTuple[2]
    currentVal = spiralTuple[3]
    for i in range(0, numTimes):
        x -= 1
        currentVal += 1
        if not spiral is None:
            spiral[x, y] = currentVal
    return spiral, x, y, currentVal


def get_top_left_to_bottom_right_diagonal(spiral, side_length):
    diagonal = []
    for i in range(side_length, 0, -1):
        diagonal.append(spiral[i - 1][side_length - i])
    return diagonal


def get_bottom_left_to_top_right_diagonal(spiral, side_length):
    diagonal = []
    for i in range(0, side_length):
        diagonal.append(spiral[i][i])
    return diagonal

    # if size is 5 then return values in the spiral with side length 7
    # def values_in_next_spiral(size):
    #
    #     # last number in the current spiral
    #     count = size*size
    #
    #     values = sc.SortedList()
    #     # go right once always
    #     count+=1
    #     values.append(count)
    #
    #         # go down (2 * spiralCount) -1 times
    #         for i in range(0, (2*spiralCount)-1):
    #             x+=1
    #             count+=1
    #             n[x,y]=count
    #
    #         # go left 2 * spiralCount times
    #         for i in range(0, (2*spiralCount)):
    #             y-=1
    #             count+=1
    #             n[x,y]=count
    #
    #         # go up 2 * spiralCount times
    #         for i in range(0, (2*spiralCount)):
    #             x-=1
    #             count+=1
    #             n[x,y]=count
    #
    #         # go right 2 * spiralCount times
    #         for i in range(0, (2*spiralCount)):
    #             y+=1
    #             count+=1
    #             n[x,y]=count
    #
    #         spiralCount += 1
    #
    #     return n
