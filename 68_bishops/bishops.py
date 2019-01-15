from itertools import chain


def bishops(B):
    d = left_diagonals(B)
    print(d)
    return len(B) - len(left_diagonals(B)) + len(B) - len(right_diagonals(B))


def left_diagonals(B):
    return {x-y for x, y in B}


def right_diagonals(B):
    return {(4-x) - y for x, y in B}


if __name__ == '__main__':
    B = [
        (0, 0),
        (1, 2),
        (2, 2),
        (4, 0)
    ]
    print(bishops(B))
