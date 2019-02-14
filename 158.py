def ways(matrix):
    paths = [[0 for _ in matrix[0]] for _ in matrix]
    paths[0][0] = 1
    for rowi, row in enumerate(matrix):
        for coli, col in enumerate(row):
            if rowi == coli == 0:
                continue
            if col == 1:
                paths[rowi][coli] = 0
            else:
                top = paths[rowi-1][coli] if rowi > 0 else 0
                left = paths[rowi][coli-1] if coli > 0 else 0
                paths[rowi][coli] = top + left
    return paths[-1][-1]


if __name__ == "__main__":
    mat = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
    assert ways(mat) == 2
