from itertools import chain


def pascal(k):
    pascal = [1, 0]
    for i in range(1, k):
        pascal = [
            pascal[(j - 1) % (i + 1)] + pascal[j] for j in range(i + 1)
        ] + [0]
    return pascal[:-1]


assert pascal(5) == [1, 4, 6, 4, 1]
