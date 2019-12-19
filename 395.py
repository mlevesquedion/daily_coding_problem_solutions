from collections import Counter, defaultdict


def sorted_signature(x):
    return tuple(sorted(x))


def Counter_signature(x):
    return frozenset(Counter(x).items())


# For sorted, O([k log k] * n)
# For Counter, O(kn)
# In the general case, O(sig(k) * n)
def solve(array, signature):
    groups = defaultdict(list)
    for x in array:
        groups[signature(x)].append(x)
    return [g for g in groups.values()]


expected = [["eat", "ate", "tea"], ["apt", "pat"], ["now"]]
for signature in [sorted_signature, Counter_signature]:
    assert (
        solve(["eat", "ate", "apt", "pat", "tea", "now"], signature)
        == expected
    )
