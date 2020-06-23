class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(tree):
    return list(reversed(helper(tree)[0]))


def helper(tree):
    if tree is None:
        return [], 0

    if tree.left is None and tree.right is None:
        return [tree.val], tree.val

    left_path, left_sum = helper(tree.left)
    right_path, right_sum = helper(tree.right)

    if not left_path:
        return right_path + [tree.val], right_sum + tree.val

    if not right_path:
        return left_path + [tree.val], left_sum + tree.val

    if left_sum < right_sum:
        return left_path + [tree.val], left_sum + tree.val
    else:
        return right_path + [tree.val], right_sum + tree.val


tree = Tree(10, Tree(5, None, Tree(2)), Tree(5, None, Tree(1, Tree(-1), None)))
print(solve(tree))
assert solve(tree) == [10, 5, 1, -1]
