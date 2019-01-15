from operator import mul
from functools import reduce


def solve(arr):
    prod = reduce(mul, arr)
    return [prod//x for x in arr]


def solve(arr):
    ascending_products = [arr[0]]
    descending_products = [arr[-1]]
    length = len(arr)
    result = []
    for i in range(1, length):
        ascending_products.append(arr[i] * ascending_products[-1])
        descending_products.append(arr[length-i-1] * descending_products[-1])
    for i in range(length):
        if i == 0:
            asc = 1
        else:
            asc = ascending_products[i-1]
        if i == length - 1:
            dsc = 1
        else:
            dsc = descending_products[length-i-2]
        result.append(asc * dsc)
    return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    assert solve(arr) == expected
    arr = [3, 2, 1]
    expected = [2, 3, 6]
    assert solve(arr) == expected
