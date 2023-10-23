class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    nodeCount = countNodes(linkedList)
    midPoint = (nodeCount // 2)
    node = linkedList
    count = 1
    while node is not None and count <= midPoint:
        count += 1
        node = node.next
    return node

def countNodes(linkedList):
    count = 0
    node = linkedList
    while node is not None:
        count += 1
        node = node.next
    return count
