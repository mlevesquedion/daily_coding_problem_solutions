class BinTree:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right
    def __str__(self):
        return f'({self.val} {self.left} {self.right})'

def prune(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        if tree.val == 0:
            return None
        else:
            return tree
    tree.left = prune(tree.left)
    tree.right = prune(tree.right)
    return tree


tree = BinTree(
        0,
        BinTree(1),
        BinTree(
            0,
            BinTree(1,
                BinTree(0),
                BinTree(0)
            ),
            BinTree(0)
        )
    )

pruned_tree = BinTree(
        0,
        BinTree(1),
        BinTree(
            0,
            BinTree(1)
        )
    )


assert prune(tree) == pruned_tree
