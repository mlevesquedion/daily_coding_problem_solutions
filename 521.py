def solve(s, k):
    table = [[" " for _ in s] for _ in range(k)]
    row, increment = 0, 1
    for column, char in enumerate(s):
        table[row][column] = char
        row += increment
        if row in (0, k - 1):
            increment *= -1
    print("\n".join(map("".join, table)))


solve("thisisazigzag", 4)
