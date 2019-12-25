def solve(arr, ixs):
    return [arr[i] for i in ixs]


arr = "abc"
ixs = [2, 1, 0]
assert solve(arr, ixs) == "c b a ".split()
