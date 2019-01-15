class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinTree:

    def __init__(self):
        self.root = None
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while 1:
            if current.value == value:
                return
            elif current.value < value:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right

    def remove(self, value):
        if self.root.value == value:
            if self.root.left is not None:
                self.root = self.root.left
                return
            if self.root.right is not None:
                self.root = self.root.right
                return
            self.root = None
        else:
            parent = self.root
            while 1:
                if parent.left is not None:
                    if parent.left.value == value:
                        if parent.left.left is not None:
                            parent.left = parent.left.left
                            return
                        if parent.left.right is not None:
                            parent.left = parent.left.right
                            return
                    else:
                        parent = parent.
