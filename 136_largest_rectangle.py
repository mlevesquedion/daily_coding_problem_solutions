from quicktest import test

deltas = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]


def solve(matrix):
    _max = 0

    def in_bounds(i, j):
        return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

    def explore(i, j):
        if in_bounds(i, j) and matrix[i][j] == 1:
            matrix[i][j] = 0
            return 1 + sum(explore(i+di, j+dj) for di, dj in deltas)
        return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            _max = max(explore(i, j), _max)

    return _max


if __name__ == "__main__":
    test(
        solve,
        [
            (
                [
                    [1, 0, 0, 0],
                    [1, 0, 1, 1],
                    [1, 0, 1, 1],
                    [0, 1, 0, 0]
                ],
                4
            ),
            (
                [
                    [1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]
                ],
                8
            ),
            (
                [
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]
                ],
                9
            ),
        ]
    )
