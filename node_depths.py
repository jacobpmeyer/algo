def nodeDepths(root):
    depthSum = 0
    queue = [[root, 0]]
    pointer = 0
    while pointer < len(queue):
        currentNode = queue[pointer][0]
        currentDepth = queue[pointer][1]

        if currentNode.left is not None:
            queue.append([currentNode.left, currentDepth + 1])

        if currentNode.right is not None:
            queue.append([currentNode.right, currentDepth + 1])

        depthSum += currentDepth
        pointer += 1


    return depthSum
# Time complexity is O(n) because each node must be visited
# Space complexity for this solve is O(n) because at worst, we fill up an
# array with every node


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

