class NaryTree:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.clear_except_node_value()

    def clear_except_node_value(self):
        self.left = None
        self.right = None
        self.maxTreePathSumForThisRoot = None
        self.minTreePathSumForThisRoot = None
        self.areChildrenSet = False
        self.children = None

    def setChildren(self, childList):
        self.children = childList
        self.areChildrenSet = True
        self.calcMinMaxVals()

    def calcMinMaxVals(self):
        if self.children is None:
            self.maxTreePathSumForThisRoot = self.nodeValue
            self.minTreePathSumForThisRoot = self.nodeValue
        else:
            maxSum = float("-inf")
            minSum = float("inf")
            for c in self.children:
                if not c is None:
                    newMaxVal = c.getMaxTreePathSumForThisRoot()
                    newMinVal = c.getMinTreePathSumForThisRoot()
                    if not newMaxVal is None:
                        if newMaxVal > maxSum:
                            maxSum = newMaxVal
                    if not newMinVal is None:
                        if newMinVal < minSum:
                            minSum = newMinVal

            self.maxTreePathSumForThisRoot = self.nodeValue + maxSum
            self.minTreePathSumForThisRoot = self.nodeValue + minSum


    def getAreChildrenSet(self):
        return self.areChildrenSet

    def getChildren(self):
        return self.children

    def setNodeValue(self, value):
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
