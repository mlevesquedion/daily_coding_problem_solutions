from operator import add, mul

ops = {
    '+': add,
    '*': mul
}


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self):
        if isinstance(self.val, int):
            return self.val
        else:
            return ops[self.val](self.left.evaluate(), self.right.evaluate())


if __name__ == '__main__':
    tree = Node(
        '*',
        Node('+', Node(3), Node(2)),
        Node('+', Node(4), Node(5))
    )
    print(tree.evaluate())
