from functools import lru_cache


def solve(arr, k):
    @lru_cache(None)
    def sell(i, k):
        if i == len(arr) - 1:
            return 0
        bought = arr[i]
        return max(arr[j] - bought + buy(j + 1, k - 1) for j in range(i + 1, len(arr)))

    @lru_cache(None)
    def buy(i, k):
        if i == len(arr) or k == 0:
            return 0
        return max(sell(i, k), buy(i + 1, k))

    return buy(0, k)


assert solve([5, 2, 4, 0, 1], 2) == 3
