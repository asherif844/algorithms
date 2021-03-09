import json


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    
    inOrderTraversalOrder = getInOrderTraveralOrder(tree)
    for idx, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode != node:
            


def getInOrderTraveralOrder(node, order=[]):
    if node is None:
        return order
    getInOrderTraveralOrder(node.left, order)
    order.append(node)
    getInOrderTraveralOrder(node.right, order)
    return order

