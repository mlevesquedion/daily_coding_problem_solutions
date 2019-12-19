from collections import Counter, defaultdict


def sorted_signature(x):
    return tuple(sorted(x))


def counted_signature(x):
    return frozenset(Counter(x).items())


def solve(array, signature):
    groups = defaultdict(list)
    for x in array:
        groups[signature(x)].append(x)
    return [g for g in groups.values()]


expected = [["eat", "ate", "tea"], ["apt", "pat"], ["now"]]
assert (
    solve(["eat", "ate", "apt", "pat", "tea", "now"], sorted_signature)
    == expected
)
assert (
    solve(["eat", "ate", "apt", "pat", "tea", "now"], counted_signature)
    == expected
)
