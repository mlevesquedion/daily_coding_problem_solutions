from re import sub


class BinTree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.val} {self.left} {self.right})'


def solve(tree, a, b):

    def visit(node):
        if not node:
            return 0
        if a <= node.val <= b:
            return node.val + visit(node.left) + visit(node.right)
        if node.val < a:
            return visit(node.right)
        if node.val > b:
            return visit(node.left)

    return visit(tree)


tree_string = '(5 (3 (2) (4)) (8 (6) (10)))'

tree = eval(sub(' ', ',', sub(r'\(', 'BinTree(', tree_string)))

assert solve(tree, 4, 9) == 23
