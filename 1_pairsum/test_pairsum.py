def solve(arr, k):
    seen = set()
    for x in arr:
        if k - x in seen:
            return True
        seen.add(x)
    return False


if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    k = 17
    expected = True
    assert solve(arr, k) == expected
