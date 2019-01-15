"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

INFINITY = 9999999999999


def solve(arr):
    tot = 0
    _min = INFINITY
    _max = 0
    seen = set()
    while arr:
        x = arr.pop()
        if x > 0 and x not in seen:
            tot += x
            _min = min(_min, x)
            _max = max(_max, x)
            seen.add(x)
    if _min > 1:
        return 1
    expected_sum = sum(range(_min, _max + 1))
    return (expected_sum - tot) if expected_sum != tot else _max + 1


if __name__ == '__main__':
    a, b = [3, 4, -1, 1], 2
    assert solve(a) == b
    a, b = [1, 2, 0], 3
    assert solve(a) == b
    a, b = [3, 3, 4, -1, 1], 2
    assert solve(a) == b
