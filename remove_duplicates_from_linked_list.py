class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
    while node is not None:
        while node.next is not None and node.next.value == node.value:
            node.next = node.next.next
        node = node.next
    return linkedList
