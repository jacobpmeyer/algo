def findClosestValueInBst(tree, target):
    closest = float('inf')
    node = tree
    while node is not None:
        if node.value == target:
            return node.value
        elif abs(node.value - target) < abs(closest - target):
            closest = node.value

        if node.value > target:
            node = node.left
        else:
            node = node.right

    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
