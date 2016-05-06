
globalmax = float("-inf")
globalmin = float("inf")

def set_globalmax(m):
    globalmax = m

def get_globalmax():
    return globalmax

def set_globalmin(m):
    globalmin = m

def get_globalmin():
    return globalmin


def max_sum_of_branch(root):
    # If it has no children we have arrived at the end of the tree.
    # We return the value of this child.
    val = 0
    if root.getLeftChild() ==None and root.getRightChild()==None:
        return root.getNodeValue()
    else:
        # If it has children we calculate the sum of each branch.
        leftSum = max_sum_of_branch(root.getLeftChild())
        rightSum = max_sum_of_branch(root.getRightChild())
        # And return the maximum of them.
        if leftSum > rightSum:
            val = root.getNodeValue() + leftSum
        else:
            val = root.getNodeValue() + rightSum
        if (val > get_globalmax()):
            set_globalmax(val)
            print("New global max is {}".format(val))
        return val


def min_sum_of_branch(root):
    # If it has no children we have arrived at the end of the tree.
    # We return the value of this child.
    val = 0
    if root.getLeftChild() ==None and root.getRightChild()==None:
        return root.getNodeValue()
    else:
        # If it has children we calculate the sum of each branch.
        leftSum = min_sum_of_branch(root.getLeftChild())
        rightSum = min_sum_of_branch(root.getRightChild())
        # And return the maximum of them.
        if leftSum < rightSum:
            val = root.getNodeValue() + leftSum
        else:
            val = root.getNodeValue() + rightSum
        if (val < get_globalmin()):
            set_globalmin(val)
            print("New global min is {}".format(val))
        return val

