class BinaryTree:

    def __init__(self,nodeValue):
        self.left = None
        self.right = None
        self.nodeValue = nodeValue
        self.maxTreePathSumForThisRoot = None
        self.minTreePathSumForThisRoot = None


    def setChildren(self, leftChild, rightChild):
        self.left = leftChild
        self.right = rightChild
        self.calcMinMaxVals()


    def calcMinMaxVals(self):
        if self.left is None and self.right is None:
            self.maxTreePathSumForThisRoot = self.nodeValue
            self.minTreePathSumForThisRoot = self.nodeValue
        else:
            if self.left is None:
                leftMaxSum = float("-inf")
                leftMinSum = float("inf")
            else:
                leftMaxSum = self.left.getMaxTreePathSumForThisRoot()
                leftMinSum = self.left.getMinTreePathSumForThisRoot()
            if self.right is None:
                rightMaxSum = float("-inf")
                rightMinSum = float("inf")
            else:
                rightMaxSum = self.right.getMaxTreePathSumForThisRoot()
                rightMinSum = self.right.getMinTreePathSumForThisRoot()

            if not(leftMaxSum is None and rightMaxSum is None):
                if leftMaxSum > rightMaxSum:
                    self.maxTreePathSumForThisRoot = self.nodeValue + leftMaxSum
                else:
                    self.maxTreePathSumForThisRoot = self.nodeValue + rightMaxSum

            if not(leftMinSum is None and rightMinSum is None):
                if leftMinSum < rightMinSum:
                    self.minTreePathSumForThisRoot = self.nodeValue + leftMinSum
                else:
                    self.minTreePathSumForThisRoot = self.nodeValue + rightMinSum


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

    def getMinTreePathSumForThisRoot(self):
        return self.minTreePathSumForThisRoot

    def setMinTreePathSumForThisRoot(self, minValue):
        self.minTreePathSumForThisRoot = minValue