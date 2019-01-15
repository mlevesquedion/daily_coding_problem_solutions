from collections import deque
from pytest import mark


# O(nk)
def sub_maxes(arr, k):
    if not arr or not k:
        return []
    sub_maxes = []
    i = 0
    while i + k <= len(arr):
        sub_maxes.append(max(arr[i:i+k]))
        i += 1
    return sub_maxes


@mark.parametrize(
    ['arr', 'k', 'expected'],
    [
        [
            [10, 5, 2, 7, 8, 7], 3, [10, 7, 8, 8]
        ],
        [
            [], 10, []
        ],
        [
            [1], 0, []
        ],
        [
            [1, 2, 3], 4, []
        ],
        [
            [1, 2, 3], 1, [1, 2, 3]
        ],
        [
            [1, 2, 3, 5], 4, [5]
        ]
    ]
)
def test(arr, k, expected):
    assert sub_maxes(arr, k) == expected
