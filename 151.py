def flood_fill(matrix, point, color):
    stack = [point]
    color_to_replace = matrix[point[0]][point[1]]
    while stack:
        row, col = stack.pop()
        matrix[row][col] = color
        for row, col in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]:
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                if matrix[row][col] == color_to_replace:
                    stack.append((row, col))


if __name__ == "__main__":
    matrix = list(map(lambda s: s.split(), """\
B B W
W W W
W W W
B B B""".splitlines()))
    point = (2, 2)
    color = "G"
    flood_fill(matrix, point, color)
    print(matrix)
