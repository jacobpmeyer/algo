# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None and currentNode.next is not None:
        while currentNode.next is not None and currentNode.value == currentNode.next.value:
            currentNode.next = currentNode.next.next
        currentNode = currentNode.next
    return linkedList
