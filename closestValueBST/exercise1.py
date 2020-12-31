import json 


with open('sample.json', 'rb') as f:
    data = json.load(f)

def findClosestValueBST(tree, target):
    return findClosestValueBSTHelper(tree, target, float('inf'))

def findClosestValueBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) >  abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueBSTHelper(tree.right, target, closest)
    else:
        return closest



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# root = BST(10)
root = BST(int(data['root']))
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

target = 12
tree = root

findClosestValueBST(tree, target)