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

# Insight into the solution
"""
A signature is a representation that is shared by words that are anagrams of
each other. For example, all words that are anagrams of each other become the
same string when sorted, and they have the same character counts (indeed, this
second example is the definition of an anagram). Therefore grouping the words
by their signatures produces the groups of anagrams.
"""
