class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __str__(self):
        return f"({self.val} {self.left} {self.right})"


def solve(postorder):
    def find_split_point(lo, hi, val):
        while hi >= lo and postorder[hi] > val:
            hi -= 1
        return hi

    def fast_find_split_point(lo, hi, val):
        while lo < hi:
            mid = (lo + hi) // 2
            if postorder[mid] < val:
                lo = mid
                if postorder[hi] > val:
                    hi -= 1
            elif postorder[mid] > val:
                hi = mid - 1
            else:
                raise RuntimeError("not a binary search tree")
        if postorder[lo] > val:
            return lo - 1
        else:
            return lo

    def helper(lo, hi):
        if lo > hi:
            return None
        if lo == hi:
            return Node(postorder[lo])
        val = postorder[hi]
        split_point = fast_find_split_point(lo, hi - 1, val)
        return Node(
            val, helper(lo, split_point), helper(split_point + 1, hi - 1)
        )

    return helper(0, len(postorder) - 1)


assert solve([2, 4, 3, 8, 7, 5]) == Node(
    5, Node(3, Node(2), Node(4)), Node(7, None, Node(8))
)
