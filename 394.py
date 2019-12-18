class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(tree, k):
    if tree is None:
        return False
    if tree.left is None and tree.right is None:
        return tree.val == k
    return solve(tree.left, k - tree.val), solve(tree.right, k - tree.val)


tree = Node(8, Node(4, Node(2), Node(6)), Node(13, None, Node(19)))
assert solve(tree, 18)
