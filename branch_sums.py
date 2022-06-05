# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Add self to current total
# if left and right are None, push current total to totals array and return
# if left or right aren't empty, then call traverseLeftAndRight with:
#       runningTotal, branchTotals, and whichever child isn't nil.

def branchSums(root):
    currentNode = root
    branchTotals = traverseLeftAndRight(tree, 0, [])

    return branchTotals

def traverseLeftAndRight(node, runningTotal, branchTotals):
    newTotal = runningTotal + node.value

    if node.left is not None:
        traverseLeftAndRight(node.left, newTotal, branchTotals)

    if node.right is not None:
        traverseLeftAndRight(node.right, newTotal, branchTotals)

    if node.left is None and node.right is None:
        branchTotals.append(newTotal)

    return branchTotals

# Time complexity:
# O(n) because you have to visit every node
#
# Space complexity:
# O(n)
# Worst case senario you have n calls on the stack
# and with the return array, worst case is that you have O(n / 2) length array
# which reduces to O(n)
