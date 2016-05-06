import numpy as np
from eulerutils import nary_tree as nt


def set_children_of_parent(x, y):
    global nodes
    global bound

    if not (x < 0 or y < 0 or x > size - 1 or y > size - 1):
        parent = nodes[x, y]
        if y == size - 1:
            rightChild = None
        else:
            rightChild = nodes[x][y + 1]
            if not rightChild.getAreChildrenSet():
                set_children_of_parent(x, y + 1)
        if x == size - 1:
            downChild = None
        else:
            downChild = nodes[x + 1][y]
            if not downChild.getAreChildrenSet():
                set_children_of_parent(x + 1, y)
        if x == 0:
            upChild = None
        else:
            upChild = nodes[x - 1][y]
            if not upChild.getAreChildrenSet():
                set_children_of_parent(x - 1, y)

        parent.setChildren([downChild, rightChild, upChild])
        if y == 0:
            if parent.getMinTreePathSumForThisRoot() < bound:
                bound = parent.getMinTreePathSumForThisRoot()


def clear_nodes():
    global nodes
    global size
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            nodes[i, j].clear_except_node_value()


def reload():
    global nodes
    nodes = np.empty((size, size), dtype=object)
    lineCount = 0
    for line in list(open(file)):
        line = line.strip()
        listOfStr = line.split(",")
        listOfInt = list(map(int, listOfStr))
        numCount = -1
        for i in listOfInt:
            numCount += 1
            nodes[lineCount][numCount] = nt.NaryTree(i)
        lineCount += 1


# file = "p082_matrix.txt"
# size = 80
#file = "matrix1.txt"
#size = 5
file = "tinymatrix.txt"
size = 2

# n = np.zeros((size,size))
nodes = np.empty((size, size), dtype=object)
reload()

# find a random path from top left, right and down (if necessary) to get an upper bound
bound = 0

# set the children from the end on back
# for each ending spot, do an n-ary tree working backward
min_min_result = float("inf")
end_row_of_min_min_result = 0
start_row_of_min_min_result = 0
# for ending_row in range(0, size):
for ending_row in range(1, 2):

    bound = 0
    for col in range(0, size):
        val = nodes[0][col].getNodeValue()
        bound = bound + val
    for row in range(1, ending_row + 1):
        val = nodes[row][col].getNodeValue()
        bound = bound + val

    # we have to be careful to process nodes properly starting with the last one
    # so we don't process nodes whose children have not already been processed
    # from the ending row go out in concentric semicircles
    ending_row_node = nodes[ending_row, size - 1]
    # we're ending here (although technically we might be able to continue)
    print("[{},{}]".format(ending_row, size-1))
    ending_row_node.setChildren(None)

    for col in range(size - 1, -1, -1):
        if (col < size - 1):
            # we don't want to do this the first time since we've already terminated the row above
            print("[{},{}]".format(ending_row, col))
            set_children_of_parent(ending_row, col)
        # go up
        for j in range(ending_row - 1, -1, -1):
            print("[{},{}]".format(j, col))
            set_children_of_parent(j, col)
        # go down
        for j in range(ending_row + 1, size):
            print("[{},{}]".format(j, col))
            set_children_of_parent(j, col)

    min_result = float("inf")
    start_row_of_min_result = 0
    for row in range(0, size):
        res = nodes[row, 0].getMinTreePathSumForThisRoot()
        if res < min_result:
            min_result = res
            start_row_of_min_result = row
    print("The min result when ending on row {} is {} when beginning on row {}".format(ending_row + 1, min_result,
                                                                                       start_row_of_min_result + 1))
    if (min_result < min_min_result):
        min_min_result = min_result
        end_row_of_min_min_result = ending_row
        start_row_of_min_min_result = start_row_of_min_result

    # clear_nodes()
    reload()

print("The min min result happens when beginning on row {} and ending on row {} with min value {}".format(
    start_row_of_min_min_result + 1, end_row_of_min_min_result + 1, min_min_result))
