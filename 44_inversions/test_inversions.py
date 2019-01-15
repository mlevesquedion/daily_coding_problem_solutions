from collections import deque
from pytest import mark


def merge(A, B, count):
    if not A:
        return B, count
    if not B:
        return A, count
    if A[0] < B[0]:
        rest_merged, rest_count = merge(A[1:], B, count)
        return [A[0]] + rest_merged, rest_count
    else:
        rest_merged, rest_count = merge(A, B[1:], len(A) + count)
        return [B[0]] + rest_merged, rest_count


def inversions(arr):
    deq = deque([[x] for x in arr])
    total_count = 0
    for i in range(len(arr) - 1):
        merged, merge_count = merge(deq.popleft(), deq.popleft(), 0)
        deq.appendleft(merged)
        total_count += merge_count
    return total_count


@mark.parametrize(
    ['arr', 'expected'],
    [
        [
            [1, 2, 3, 4, 5], 0
        ],
        [
            [2, 4, 1, 3, 5], 3
        ],
        [
            [2, 4, 5, 3, 1], 6
        ],
        [
            [5, 4, 3, 2, 1], 10
        ],
        [
            [1, 2, 3], 0
        ],
        [
            [2, 1, 3], 1
        ]
    ]
)
def test_inversions(arr, expected):
    assert inversions(arr) == expected
