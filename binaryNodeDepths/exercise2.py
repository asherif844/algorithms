# f(n, d) => d + f(l, d+1) + f(r, d+1)


def nodeDepth(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepth(root.left, depth+1) + nodeDepth(root.right, depth+1)


