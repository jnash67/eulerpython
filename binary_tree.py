# simple binary tree where we can define the children without the parent first
# that way we can load a tree from the bottom up
# in this implementation, a node is inserted between an existing node and the root
class BinaryTree():

    def __init__(self,nodeValue):
        self.left = None
        self.right = None
        self.nodeValue = nodeValue
        self.maxTreePathSumForThisRoot = None

    def setChildren(self, leftChild, rightChild):
        self.left = leftChild
        self.right = rightChild
        leftMaxSum = leftChild.getMaxTreePathSumForThisRoot()
        rightMaxSum = rightChild.getMaxTreePathSumForThisRoot()
        if not(leftMaxSum is None):
            assert not(rightMaxSum is None), "both left and right max sums should be not be None if either is not None"
            if (leftMaxSum > rightMaxSum):
                self.maxTreePathSumForThisRoot = self.nodeValue + leftMaxSum
            else:
                self.maxTreePathSumForThisRoot = self.nodeValue + rightMaxSum

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self,value):
        self.rootid = value

    def getNodeValue(self):
        return self.nodeValue

    def getMaxTreePathSumForThisRoot(self):
        return self.maxTreePathSumForThisRoot

    def setMaxTreePathSumForThisRoot(self, maxValue):
        self.maxTreePathSumForThisRoot = maxValue