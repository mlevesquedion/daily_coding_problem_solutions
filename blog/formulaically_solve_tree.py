class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def __str__(self):
        return str(self.left) + str(self.value) + str(self.right)


def count_nodes(tree):
    return count_nodes(tree.left) + count_nodes(tree.right) + 1 if tree else 0


def deepest_node_depth(tree):
    return _deepest_node_depth(tree, 0)


def _deepest_node_depth(tree, depth):
    return max(_deepest_node_depth(tree.left, depth+1), _deepest_node_depth(tree.right, depth+1)) if tree else depth - 1


def largest(tree):
    if not tree:
        return None
    if not tree.right:
        return tree.value
    return largest(tree.right)


if __name__ == '__main__':
    tree = Node(5)
    for x in [2, 4, 8, 3, 10, 6]:
        tree.insert(x)
    print(count_nodes(tree))
    print(deepest_node_depth(tree))
    print(largest(tree))
    print(tree)
