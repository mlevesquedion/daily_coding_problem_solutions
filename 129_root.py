from quicktest import test


def root(n):
    return n**0.5


def root(n):
    from math import sqrt as root
    return root(n)


if __name__ == '__main__':
    test(
        root,
        [
            [1, 1],
            [9, 3],
            [81, 9],
        ]
    )
