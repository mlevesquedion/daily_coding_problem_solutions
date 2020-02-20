from collections import Counter


# naive, O(|S| * |W|)
def solve(S, W):
    reference = Counter(W)
    counts = Counter(S[:len(W)])
    positions = []
    for i in range(len(S) - len(W) + 1):
        if all(reference[c] == counts[c] for c in reference):
            positions.append(i)
        if i == len(S) - len(W):
            break
        counts[S[i]] -= 1
        counts[S[i + len(W)]] += 1
    return positions

# optimized, O(|S|)
# the main idea is we only need to keep track of the difference between
# the counts and the reference.
# if the diffs are all zero, then we match the reference exactly
def solve(S, W):
    reference = Counter(W)
    diff = Counter(S[:len(W)]) - reference
    n_zeroes = len(reference) - len(diff)

    positions = []
    for i in range(len(S) - len(W) + 1):
        if n_zeroes == len(reference):
            positions.append(i)

        if i == len(S) - len(W):
            break

        if diff[S[i]] == 0 and S[i] in reference:
            n_zeroes -= 1
        diff[S[i]] -= 1
        if diff[S[i]] == 0 and S[i] in reference:
            n_zeroes += 1

        if diff[S[i + len(W)]] == 0 and S[i + len(W)] in reference:
            n_zeroes -= 1
        diff[S[i + len(W)]] += 1
        if diff[S[i + len(W)]] == 0 and S[i + len(W)] in reference:
            n_zeroes += 1

    return positions


assert solve("abxaba", "ab") == [0, 3, 4]

