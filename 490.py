class BinTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solve(tree):
    bounds = [float("inf"), float("-inf")]
    bottom_view = {}

    def explore(node, distance=0):
        nonlocal bounds
        if node is None:
            return
        bottom_view[distance] = node.value
        bounds = [min(bounds[0], distance), max(bounds[1], distance)]
        explore(node.left, distance - 1)
        explore(node.right, distance + 1)

    explore(tree)

    return [bottom_view[i] for i in range(bounds[0], bounds[1] + 1)]


tree = BinTree(
    5,
    BinTree(3, BinTree(1, BinTree(0)), BinTree(4)),
    BinTree(7, BinTree(6), BinTree(9, BinTree(8))),
)

assert solve(tree) == [0, 1, 3, 6, 8, 9]
