from pytest import mark
from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    mat = [
        [1, 1, 1, 2, 2],
        [2, 3, 3, 3, 4],
        [4, 4, 5, 5, 5],
        [6, 6, 6, 7, 7],
        [7, 0, 0, 0, 0]
    ]
    result = 0
    while result == 0:
        x = rand5()
        y = rand5()
        result = mat[x-1][y-1]
    return result

    return rand5() + rand5() % 3


if __name__ == '__main__':
    nums = [rand7() for _ in range(70000)]
    for x in range(1, 8):
        print(x, nums.count(x))
