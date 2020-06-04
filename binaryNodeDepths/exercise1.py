def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth+1)

class binaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
