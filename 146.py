from quicktest import test


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


def is_leaf(tree):
    return tree.left is None and tree.right is None


def should_prune(tree):
    return tree is None or is_leaf(tree) and tree.val == 0


def prune(tree):
    if tree is None:
        return

    prune(tree.left)
    prune(tree.right)

    left, right = map(should_prune, [tree.left, tree.right])

    if left:
        tree.left = None

    if right:
        tree.right = None

    if should_prune(tree):
        return None

    return tree


if __name__ == "__main__":
    test(
        prune,
        [
            [
                Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0))),
                Node(0, Node(1), Node(0, Node(1)))
            ]
        ]
    )
