"""
in: binary search tree
out: closest value to that target value contained in the BST
assumptions:
    there will only be one closest value
"""

def findClosestValueInBst(tree, target):
    # track the current node.
    currentNode = tree

    # track the closest value
    closestValue = tree.value

    #iterate over the tree nodes
    while currentNode is not None:
        currentValue = currentNode.value
        #check if the current node's value is closer to the target than closestValue
        if abs(currentValue - target) < abs(closestValue - target):
            closestValue = currentValue

        if currentValue == target:
            return currentValue
        elif currentValue < target:
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left

    return closestValue


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

