from collections import Counter


def solve(s):
    counts = Counter(s)
    arr = [""] * len(s)
    i = 0
    for char, count in sorted(
        counts.items(), key=lambda x: x[1], reverse=True
    ):
        for j in range(i, i + count):
            arr[j] = char
        i += count
    return "".join(arr)


assert solve("tweet") in {"tteew", "eettw"}
