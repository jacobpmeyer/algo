class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    return traverseTree(tree)


def traverseTree(node):
    if node.value == -1:
        return traverseTree(node.left) + traverseTree(node.right)
    if node.value == -2:
        return traverseTree(node.left) - traverseTree(node.right)
    if node.value == -3:
        value = traverseTree(node.left) / traverseTree(node.right)
        return int(value)
    if node.value == -4:
        return traverseTree(node.left) * traverseTree(node.right)
    else:
        return node.value
