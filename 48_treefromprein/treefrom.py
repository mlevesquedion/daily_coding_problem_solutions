class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self):
        return [self.val] + (self.left.preorder() if self.left else []) + (self.right.preorder() if self.right else [])

    def inorder(self):
        return (self.left.inorder() if self.left else []) + [self.val] + (self.right.inorder() if self.right else [])


def tree_from(preorder, inorder):
    print(preorder, inorder)
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return Node(preorder[0])
    if len(preorder) == 2:
        if preorder == inorder:
            return Node(preorder[0], None, Node(preorder[1]))
        else:
            return Node(preorder[0], Node(preorder[1]), None)
    root, *rest = preorder
    in_left, in_right = split_without(root, inorder)
    pre_left, pre_right = split_pre(set(in_left), set(in_right), rest)
    return Node(root, tree_from(pre_left, in_left), tree_from(pre_right, in_right))


def split_without(x, arr):
    for i, y in enumerate(arr):
        if y == x:
            return arr[:i], arr[i + 1:]


def split_pre(left, right, arr):
    if not left:
        return [], arr
    pre_left = []
    index = 0
    while index < len(arr) and arr[index] in left:
        pre_left.append(arr[index])
        index += 1
    return pre_left, arr[index:]


if __name__ == '__main__':
    inorder = 'cebad'
    preorder = 'abced'
    tree = tree_from(preorder, inorder)
    print(list(preorder) == tree.preorder())
    print(list(inorder) == tree.inorder())

    inorder = list('dcbaeghf')
    preorder = list('abcdefgh')
    tree = tree_from(preorder, inorder)
    print(list(preorder) == tree.preorder())
    print(list(inorder) == tree.inorder())
