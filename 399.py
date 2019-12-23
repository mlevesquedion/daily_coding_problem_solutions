def solve1(arr):
    """
    There are (n - 1) choose 2 ways to place two dividers between the numbers,
    yielding three contiguous partitions. Considering every partition puts us in
    O(n^2) [indeed, (n - 1) choose 2 = (n - 1)(n - 2)/2.
    Since there are O(n) outer loops, each requiring O(n) operations, this
    algorithm is in O(n^2).

    Additional supporting observations:
    - since the integers are strictly positive, we need not consider empty
      partitions
    """
    p1, p2, p3 = 0, arr[0], sum(arr[1:])
    for left in range(0, len(arr) - 2):
        p1, p2 = (p1 + arr[left], p2 - arr[left])
        for right in range(left + 1, len(arr) - 1):
            p2, p3 = (p2 + arr[right], p3 - arr[right])
            if len({p1, p2, p3}) == 1:
                return (
                    arr[: left + 1],
                    arr[left + 1 : right + 1],
                    arr[right + 1 :],
                )
        p2, p3 = arr[left + 1], sum(arr[left + 2 :])
    return None


def solve2(arr):
    """
    To be more efficient, we observe that we do not need consider all O(n^2)
    possible placements of the dividers. Indeed, if we first sort the integers,
    then starting with the left divider at the beginning and the right divider at
    the end, we need only increment the left divider when the first partition's sum is
    too small and decrement the right divider when the third partition's sum is too big.
    Since each divider will be moved at most O(n) times, the algorithm's complexity
    is dominated by the sort, giving a complexity of O(n log n). This can be
    improved in some cases by first finding the maximum of the list (which is in
    O(n)) and using counting sort if the maximum possible integer in the list is
    less than log n times greater than the length of the list.
    """
    arr = sorted(arr)
    p1, p2, p3 = arr[0], sum(arr[1:-1]), arr[-1]
    left, right = 0, -1
    while left < len(arr) - right:
        if len({p1, p2, p3}) == 1:
            return (
                arr[: left + 1],
                arr[left + 1 : right],
                arr[right:],
            )
        if p1 < p2:
            left += 1
            p1, p2 = p1 + arr[left], p2 - arr[left]
        else:
            right -= 1
            p2, p3 = p2 - arr[right], p3 + arr[right]
    return None


# Amusingly, the example is wrong, since the problem description
# says the integers are to be strictly positive
example = [3, 5, 8, 0, 8]
expected = ([3, 5], [8], [0, 8])
assert solve1(example) == expected
expected = ([0, 3, 5], [8], [8])
assert solve2(example) == expected
