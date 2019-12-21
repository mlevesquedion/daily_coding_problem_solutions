# DP, O(n^2)
def solve(intervals):
    table = [0 for _ in range(len(intervals) + 1)]
    parents = [None for _ in table]
    for i in range(1, len(intervals) + 1):
        best_so_far = 0
        parent_so_far = None
        for j in range(i):
            if intervals[j - 1][1] <= intervals[i - 1][0]:
                best_so_far, parent_so_far = table[j], j
        table[i] = 1 + best_so_far
        parents[i] = parent_so_far

    solution = []
    i = max(range(len(intervals) + 1), key=lambda j: table[j])
    while i is not None:
        solution.append(intervals[i - 1])
        i = parents[i]
    return solution


intervals = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]

print(solve(intervals))
