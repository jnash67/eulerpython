import numpy as np
from eulerutils import binary_tree as bt

def set_children(parent, x, y):
    global nodes
    global size
    global globalmin

    if y == size - 1:
        rightChild = None
    else:
        rightChild = nodes[x][y + 1]
    if x == size - 1:
        downChild = None
    else:
        downChild = nodes[x + 1][y]

    parent.setChildren(downChild, rightChild)


file = "p081_matrix.txt"
size = 80
# file = "matrix1.txt"
# size = 5
# num = np.zeros((size,size))
nodes = np.empty((size, size), dtype=object)
lineCount = 0
for line in list(open(file)):
    line = line.strip()
    listOfStr = line.split(",")
    listOfInt = list(map(int, listOfStr))
    numCount = -1
    for i in listOfInt:
        numCount += 1
        nodes[lineCount][numCount] = bt.BinaryTree(i)
    lineCount += 1

# set the children from the bottom on up
bottom_right = nodes[size - 1, size - 1]
# going along the diagonal from bottom right to top left, set the
# children for each row and column above the diagonal
for i in range(size-1,0,-1):
    # set the diagonal
    print("[{},{}]".format(i, i))
    set_children(nodes[i,i],i,i)
    for j in range(1, i+1):
        print("[{},{}]".format(i,i-j))
        set_children(nodes[i,i-j],i,i-j)
        print("[{},{}]".format(i-j,i))
        set_children(nodes[i-j,i],i-j,i)

root = nodes[0,0]
set_children(root,0,0)
print("The min path is " + str(root.getMinTreePathSumForThisRoot()))
