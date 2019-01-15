from random import randint
from collections import Counter


def shuffle(arr):
    arr = list(arr)
    for i in range(len(arr)):
        swap_index = randint(0, len(arr) - 1)
        arr[i], arr[swap_index] = arr[swap_index], arr[i]
    return tuple(arr)


if __name__ == '__main__':
    arr = tuple(range(4))
    perms = Counter()
    for _ in range(100000):
        arr = shuffle(arr)
        perms.update(Counter([arr]))
    for count in perms.values():
        print(count)
