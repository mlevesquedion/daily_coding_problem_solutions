def solve(L):
    left, right = None, None
    while L:
        left, L = (L[0], left), L[1]
        if L is None:
            break
        right, L = (L[0], right), L[1]
    result = None
    while left:
        result, left = (left[0], result), left[1]
        if right is None:
            break
        result, right = (right[0], result), right[1]
    return result[0]


if __name__ == "__main__":
    L = (1, (2, (3, (4, None))))
    print(solve(L))
