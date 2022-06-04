"""
in: binary search tree
out: closest value to that target value contained in the BST
assumptions:
    there will only be one closest value
"""

def findClosestValueInBst(tree, target):
    currentNode = tree
    closestValue = tree.value

    while currentNode is not None:
        if abs(currentNode.value - target) < abs(closestValue - target):
            closestValue = currentNode.value

        if currentNode.value == target:
            return currentNode.value
        elif currentNode.value < target:
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

