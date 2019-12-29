def solve(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    if (tree.left and tree.left.val > tree.val) or (
        tree.right and tree.right.val < tree.val
    ):
        return max(solve(tree.left), solve(tree.right))
    else:
        return 1 + solve(tree.left) + solve(tree.right)
