def solve(arr):
    """
    Horrible, quadratic complexity, no extra space though
    """
    return [
        len([y for y in arr[i+1:] if y < x])
        for i, x in enumerate(arr)
    ]


def _solve(arr):
    """
    Slightly faster, O(n log n) time complexity, but O(n) extra space
    Also, not valid Python, we are using an hypothetical balanced binary
    tree structure which has O(log n) inserts and O(log n) queries for
    the number of items smaller than a given item.
    """
    '''\
    t = BalancedBinarySearchTree()
    counts = []
    for i in range(len(arr)-1, -1, -1):
        counts.append(t.n_smaller(arr[i]))
        t.insert(arr[i])
    return counts
    '''


if __name__ == '__main__':
    entry = [3, 4, 9, 6, 1]
    expected = [1, 1, 2, 1, 0]
    assert solve(entry) == expected
