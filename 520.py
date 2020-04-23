from itertools import accumulate


def solve(tree):
    return max(accumulate(({"(": 1, ")": -1}.get(c, 0) for c in tree)))


print(solve("((((00)0)0)0)"))
