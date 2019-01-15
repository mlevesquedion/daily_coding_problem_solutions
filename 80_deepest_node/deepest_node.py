class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_deepest_node(tree):
    return _get_deepest_node(0, tree)[1]


def _get_deepest_node(depth, tree):
    if tree is None:
        return (depth, None)
    (left_depth, left_val) = _get_deepest_node(depth + 1, tree.left)
    (right_depth, right_val) = _get_deepest_node(depth + 1, tree.right)
    if left_val is None:
        left_val = tree.val
    if right_val is None:
        right_val = tree.val
    if left_depth > right_depth:
        return (left_depth, left_val)
    else:
        return (right_depth, right_val)


if __name__ == '__main__':
    tree = Node(
        'a',
        Node(
            'b',
            Node('d')
        ),
        Node('c')
    )
    print(get_deepest_node(tree))
