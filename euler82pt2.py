import numpy as np
from eulerutils import nary_tree as nt

# it's possible with 3 ways movement, there's no longer optimal substructure
# let's treat as a dijkstra graph

globalmin = float("inf")

def set_globalmin(m):
    globalmin = m

def get_globalmin():
    return globalmin

def min_sum_of_branch(root):
    # If it has no children we have arrived at the end of the tree.
    # We return the value of this child.
    if root is None:
        return float("inf")

    val = 0
    if root.getChildren() is None:
        return root.getNodeValue()
    else:
        # If it has children we calculate the sum of each branch.
        min_sum = 0
        for child in root.getChildren():
            new_child_sum  = min_sum_of_branch(child)
            if new_child_sum < min_sum:
                min_sum = new_child_sum

        val = root.getNodeValue() + min_sum
        if val < get_globalmin():
            set_globalmin(val)
            print("New global min is {}".format(val))
        return val


def load():
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

# let's try starting at the beginning and just not continuing with route
# if we're past some better bound

file = "matrix1.txt"
size = 5
# file = "tinymatrix.txt"
# size = 2

# n = np.zeros((size,size))
nodes = np.empty((size, size), dtype=object)
load()

# for some starting spot to some ending spot, calculate a path cost
bound = 0
for col in range(0, size):
    val = nodes[0][col].getNodeValue()
    bound = bound + val
set_globalmin(bound)

min_min_result = float("inf")
end_row_of_min_min_result = 0
start_row_of_min_min_result = 0

# for ending_row in range(0, size):
for start_row in range(0, size):
    min = min_sum_of_branch(nodes[start_row][0])
    print("for row {} the min is {}".format(start_row, min))
