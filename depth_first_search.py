# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

# Recursive solve
# array is the thing to return, I think
#
# Build up the array as we go by appending self.name in the array.
# Make recursive call to depthFirstSearch, passing:
#   (children.pop(), array)
# When self.children is empty, return the array up
# The recursive call returns the array
# Set the return value to the current array
    def depthFirstSearch(self, array):
        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)

        return array

# Time complexity is O(n) because we must visit each node
# Space complexity is O(n)

