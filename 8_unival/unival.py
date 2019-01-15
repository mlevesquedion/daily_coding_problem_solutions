class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_leaf(tree):
    return [tree.left, tree.right] == [None] * 2


def same_value(tree):
    return len({
        tree.value,
        tree.left.value if tree.left else tree.value,
        tree.right.value if tree.right else tree.value
    }) == 1


def unival_count(tree):
    count, _ = _unival_count(tree)
    return count


def _unival_count(tree):
    if tree is None:
        return 0, True
    if is_leaf(tree):
        return 1, True
    else:
        left_count, left_unival = _unival_count(tree.left)
        right_count, right_unival = _unival_count(tree.right)
        all_conditions_met = same_value(tree) and left_unival and right_unival
        return (left_count + right_count + all_conditions_met), all_conditions_met


if __name__ == '__main__':
    node = Node(
        0,
        Node(1),
        Node(
            0,
            Node(
                1,
                Node(1),
                Node(1)
            ),
            Node(0)
        )
    )
    print(unival_count(node))
