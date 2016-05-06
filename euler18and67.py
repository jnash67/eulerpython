from eulerutils import binary_tree as bt

globalmax = float("-inf")

def set_globalmax(m):
    globalmax = m

def get_globalmax():
    return globalmax

def sum_of_branch(root):
    # If it has no children we have arrived at the end of the tree.
    # We return the value of this child.
    val = 0
    if root.getLeftChild() ==None and root.getRightChild()==None:
        return root.getNodeValue()
    else:
        # If it has children we calculate the sum of each branch.
        leftSum = sum_of_branch(root.getLeftChild())
        rightSum = sum_of_branch(root.getRightChild())
        # And return the maximum of them.
        if leftSum > rightSum:
            val = root.getNodeValue() + leftSum
        else:
            val = root.getNodeValue() + rightSum
        if (val > get_globalmax()):
            set_globalmax(val)
            print("New global max is {}".format(val))
        return val

def create_list_of_nodes(listOfInt):
    nodeList = []
    listLen = len(listOfInt)
    #print("Number of ints on current line {}".format(currLineLen))
    for i in range(0,listLen):
        n = bt.BinaryTree(listOfInt[i])
        nodeList.append(n)
    return nodeList

# text_file = open("triangle1.txt", "r")
# lines = text_file.readlines()
#file = "triangle1.txt"
file = "p067_triangle.txt"
summax = 0
currNodeList = []
prevNodeList = []
first = True
for line in reversed(list(open(file))):
    print(line)
    line = line.strip()
    listOfStr = line.split(" ")
    listOfInt = list(map(int, listOfStr))
    if first:
        first = False
        currNodeList = create_list_of_nodes(listOfInt)
        for node in currNodeList:
            val = node.getNodeValue()
            node.setMaxTreePathSumForThisRoot(val)
        prevNodeList = currNodeList
    else:
        currNodeList = create_list_of_nodes(listOfInt)
        currNodeListLen = len(currNodeList)
        prevNodeListLen = len(prevNodeList)
        assert currNodeListLen+1 == prevNodeListLen, "prevNodeList should always be 1 bigger than nodeList"
        for i in range(0, currNodeListLen):
            currNodeList[i].setChildren(prevNodeList[i], prevNodeList[i+1])
        prevNodeList = currNodeList
    #
    # if (len(listOfStr)==1):
    #     break
    # nodeLists.insert(0, currNodeList)
    # currNodeListLen = len(currNodeList)
    # #print("Length of current node list is " + str(currNodeListLen))
    # if (len(nodeLists)>1):
    #     # prevNodeList should always be 1 bigger than nodeList
    #     prevNodeList = nodeLists.pop()
    #     prevNodeListLen = len(prevNodeList)
    #     print("Prev number of nodes is {} and current number of nodes is {}".format(prevNodeListLen, currNodeListLen))
    #     assert currNodeListLen+1 == prevNodeListLen, "prevNodeList should always be 1 bigger than nodeList"
    #     for i in range(0, currNodeListLen):
    #         prevNodeList[i].setRoot(currNodeList[i])
root = currNodeList[0]
print("The max path is " + str(root.getMaxTreePathSumForThisRoot()))
# root.setIsUltimateRoot(True)
# print(sum_of_branch(root))

        # for i in range(0, c):
        #     node = prevNodeList[0]
        #     node.


# for line in range(lines)
# for line in lines:
#     #print(line)
#     linemax = line_max(list)
#     print("line max is " + str(linemax))
#     summax = summax + linemax
#
# print("Sum of the maxes is " + str(summax));
# text_file.close()