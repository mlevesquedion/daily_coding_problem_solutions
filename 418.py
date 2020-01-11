def solve(sloc):
    pays = [1 for _ in sloc]
    positions = range(1, len(sloc) - 1)

    for i in positions:
        candidates = [0]
        if sloc[i - 1] < sloc[i]:
            candidates.append(pays[i - 1])
        if sloc[i + 1] < sloc[i]:
            candidates.append(pays[i + 1])
        pays[i] = max(candidates) + 1

    return pays


sloc = [10, 40, 200, 1000, 60, 30]
assert solve(sloc) == [1, 2, 3, 4, 2, 1]
