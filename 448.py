def do_swaps(arr, color, start=0):
    first_diff = start
    while arr[first_diff] == color:
        first_diff += 1
    color_i = first_diff
    for i in range(first_diff + 1, len(arr)):
        if arr[i] == color:
            arr[color_i], arr[i] = arr[i], arr[color_i]
            color_i += 1
    return color_i

# simple 2-pass algorithm, O(n)
def solve(arr):
    next_i = do_swaps(arr, 'R')
    do_swaps(arr, 'G', next_i)
    return arr


solution = ''.join(solve(list('GBRRBRG')))
assert solution == 'RRRGGBB'

