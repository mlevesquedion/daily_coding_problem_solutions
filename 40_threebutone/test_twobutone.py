from pytest import mark


def twobutone(nums):
    running_xor = 0
    for x in nums:
        running_xor ^= x
    return running_xor


@mark.parametrize(
    ['arr', 'expected'],
    [
        [
            [13, 19, 13], 19
        ],
        [
            [2, 2, 3], 3
        ],
        [
            [4, 4, 3], 3
        ],
        [
            [4, 3, 4], 3
        ],
        [
            [6, 1, 3, 3, 6], 1
        ],
        [
            [6, 2, 3, 6, 3], 2
        ],
    ]
)
def test(arr, expected):
    assert expected == twobutone(arr)
