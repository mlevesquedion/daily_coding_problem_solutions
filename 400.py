class Sum:
    def __init__(self, arr):
        self.arr = arr

    def __call__(self, i, j):
        return self.arr[i][j - i]


# O(n^2) time + space, lookups are O(1)
# Fenwick tree would be O(n) space but O(log n) for lookups
def preprocess(arr):
    sum = [[0 for _ in arr] for _ in arr]
    for i in range(len(arr)):
        running = 0
        for j in range(i, len(arr)):
            running += arr[j]
            sum[i][j] = running
    return Sum(sum)


sum = preprocess([1, 2, 3, 4, 5])
assert sum(1, 3) == 5
