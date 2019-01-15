class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree):
    return f'Node("{tree.val}"{","+serialize(tree.left) if tree.left else ""}{"," + serialize(tree.right) if tree.right else ""})'


deserialize = eval


def parse_string(s):
    first_quote = s.index('"')
    second_quote = s.index('"', first_quote+1)
    return s[first_quote+1:second_quote], s[second_quote+1:]


def deserialize(tree_string):
    node, _ = _deserialize(tree_string)
    return node


def _deserialize(tree_string):
    if tree_string[:5] == 'Node(':
        value, rest = parse_string(tree_string[5:])
        left, right = None, None
        if rest[0] == ",":
            left, rest = _deserialize(rest[1:])
            if rest[0] == ",":
                right, rest = _deserialize(rest[1:])
        while "(" in rest:
            rest = rest[1:]
        return Node(value, left, right), rest


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
