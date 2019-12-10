from collections import Counter


def solve(s):
    return "".join(
        [
            char
            for char, count in sorted(
                Counter(s).items(), key=lambda x: x[1], reverse=True
            )
            for _ in range(count)
        ]
    )


assert solve("tweet") in {"tteew", "eettw"}
