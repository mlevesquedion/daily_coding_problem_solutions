import random
from functools import reduce
from operator import xor


def oneupto(n):
    return range(1, n+1)


def find_duplicate(arr, n):
    return reduce(xor, arr) ^ reduce(xor, oneupto(n))


if __name__ == "__main__":
    n = 100
    arr = list(oneupto(n))
    arr.append(random.choice(arr))
    random.shuffle(arr)
    print(find_duplicate(arr, n))
