from quicktest.quicktest import test


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_sorted(arr):
    return all(x <= y for x, y in zip(arr, arr[1:]))


def in_order(tree):
    if tree is not None:
        return in_order(tree.left) + [tree.data] + in_order(tree.right)
    else:
        return []


def is_binsearch_tree(t):
    return is_sorted(in_order(t))


if __name__ == '__main__':
    binsearchtree = Node(
        3,
        Node(1),
        Node(4)
    )
    notbinsearchtree = Node(
        1,
        Node(2)
    )
    test(
        is_binsearch_tree,
        [
            (binsearchtree, True),
            (notbinsearchtree, False)
        ]
    )
