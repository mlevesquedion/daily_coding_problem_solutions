# transpose, then flip horizontally
def solve(matrix):
    return [list(row[::-1]) for row in zip(*matrix)]


matrix = [list(range(i, i + 3)) for i in range(1, 10, 3)]
expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

assert solve(matrix) == expected
