def solve(grid):
    def neighbors(i, j):
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                yield (i + di, j + dj)

    def neighbor_sum(i, j):
        return sum(grid[ni][nj] for (ni, nj) in neighbors(i, j))

    perimeter = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:
                ns = neighbor_sum(i, j)
                if ns == 4:
                    ns = 0
                perimeter += ns
    return perimeter


grid = [[0, 1, 1, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]]

assert solve(grid) == 14
