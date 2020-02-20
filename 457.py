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


assert solve("abxaba", "ab") == [0, 3, 4]

