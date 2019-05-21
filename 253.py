def zigzag(s, k):
    mat = [[' ' for _ in s] for _ in range(k)]
    row = 0
    step = 1
    for i, c in enumerate(s):
        mat[row][i] = c
        row += step
        if row == 0 or row == k - 1:
            step = -step
    return '\n'.join(''.join(row) for row in mat)


if __name__ == "__main__":
    print(zigzag('thisisazigzag', 4))
