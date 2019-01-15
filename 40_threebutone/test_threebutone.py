from collections import Counter
from pytest import mark


def threebutone(arr):
    return [x for x in arr if arr.count(x) == 1][0]


def threebutone(nums):
    return (3 * sum(set(nums)) - sum(nums)) // 2


@mark.parametrize(
    ['arr', 'expected'],
    [
        [
            [13, 19, 13, 13], 19
        ],
        [
            [2, 2, 2, 3], 3
        ],
        [
            [4, 4, 4, 3], 3
        ],
        [
            [4, 3, 4, 4], 3
        ],
        [
            [6, 1, 3, 3, 3, 6, 6], 1
        ],
        [
            [6, 2, 3, 3, 3, 6, 6], 2
        ],
        [
            [6, 4, 3, 3, 3, 6, 6], 4
        ],
    ]
)
def test(arr, expected):
    assert expected == threebutone(arr)


if __name__ == '__main__':
    from random import shuffle, sample

    def gen_random():
        nums = list(range(1, 100))
        shuffle(nums)
        S = sample(nums, 50)
        arr = [S[0]] + [x for x in S for _ in range(3)]
        shuffle(arr)
        return arr, S[0]

    arr, expected = gen_random()

    print(arr, expected, threebutone(arr))

    assert threebutone(arr) == expected
