"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def reference(arr):
    for i in range(2, len(arr)):
        arr[i] = max(arr[:i-1]) + arr[i]
    return arr[-1]


def solve(arr):
    if len(arr) == 2:
        return max(arr)
    if len(arr) == 3:
        return max(arr[0] + arr[2], arr[1])
    if len(arr) == 4:
        return max(arr[0] + arr[2], arr[0] + arr[3], arr[1] + arr[3], arr[0] + arr[3])
    while len(arr) > 4:
        arr[2] += arr[0]
        arr.pop(0)
    return arr[-1] + max(arr[0], arr[1])


# Optimize this to reach O(N). Can probably "chunk" the array from the left.

if __name__ == '__main__':
    for case in [
        [2, 4, 1, 2, 14, 2],
        [2, 914, 21, 1, 20, 23, 2]
    ]:
        assert solve(case) == reference(case)
