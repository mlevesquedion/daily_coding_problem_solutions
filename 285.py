def solve(arr):
    max_so_far = float('-inf')
    have_view = 0
    for x in arr:
        if x > max_so_far:
            have_view += 1
            max_so_far = x
    return have_view

arr = [3, 7, 8, 3, 6, 1]
print(solve(arr))