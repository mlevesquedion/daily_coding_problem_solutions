def solve(denominations, amount):
    counts = list(range(amount + 1))
    counts[0] = 0

    denominations += [0]

    for i in range(1, len(counts)):
        counts[i] = 1 + min(counts[i - d] for d in denominations if d <= i)

    return counts[amount] if counts[amount] else None


if __name__ == "__main__":
    assert solve([1, 5, 10], 56) == 7
    assert solve([5, 8], 15) == 3
