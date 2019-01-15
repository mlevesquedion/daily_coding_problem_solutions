from collections import deque


class Node:

    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False
        self.locked_descendants = 0

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val, self)
        if val == self.val:
            return
        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val, self)

    def has_locked_ancestors(self):
        if self.parent:
            return self.parent.locked or self.parent.has_locked_ancestors()
        else:
            return False

    def traverse_ancestors(self, f):
        if self.parent:
            f(self.parent)
            self.parent.traverse_ancestors(f)

    def increment_ancestors(self):
        def increment_descendants(node):
            node.locked_descendants += 1
        self.traverse_ancestors(increment_descendants)

    def decrement_ancestors(self):
        def decrement_descendants(node):
            node.locked_descendants -= 1
        self.traverse_ancestors(decrement_descendants)

    def has_locked_descendants(self):
        return self.locked_descendants != 0

    def inorder(self):
        return (self.left.inorder() if self.left else []) + [self.val] + (self.right.inorder() if self.right else [])

    def can_lock(self):
        return not self.has_locked_ancestors() and not self.has_locked_descendants()

    def lock(self):
        if self.can_lock():
            self.locked = True
            self.increment_ancestors()
            return True
        return False

    def unlock(self):
        if self.can_lock():
            self.locked = False
            self.decrement_ancestors()
            return True
        return False


class Tree:

    @staticmethod
    def from_list(lst):
        tree = Tree()
        for x in lst:
            tree.insert(x)
        return tree

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def inorder(self):
        if self.root is None:
            return []
        else:
            return self.root.inorder()


def balance(tree):
    s = sorted(tree.inorder())
    x = []
    Q = deque([s])
    while Q:
        c = Q.popleft()
        if len(c) > 2:
            left, mid, right = split_mid(c)
            x.append(mid)
            Q.append(left)
            Q.append(right)
        else:
            x.extend(c)
    tree = Tree()
    for y in x:
        tree.insert(y)
    return tree


def split_mid(arr):
    i = len(arr) // 2
    return arr[:i], arr[i], arr[i+1:]


if __name__ == '__main__':
    tree = Tree.from_list([3, 2, 4, 5, 6, 1, 8])
    tree = balance(tree)
    print(tree.inorder())
    print(tree.root.right.val)
    tree.root.left.lock()
    print(tree.root.left.locked)
    print(tree.root.locked)
    tree.root.lock()
    print(tree.root.left.locked)
    print(tree.root.locked)
    tree.root.left.unlock()
    print(tree.root.left.locked)
    print(tree.root.locked)
    tree.root.lock()
    print(tree.root.left.locked)
    print(tree.root.locked)
    tree.root.left.lock()
    print(tree.root.left.locked)
    print(tree.root.locked)
