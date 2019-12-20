from functools import lru_cache

# Given an existing palindrome, you can construct a longer palindrome by adding
# yourself to the other side, if it is available
# Each substring of length 1 is a palindrome

# Given 928K182A7Y82A290K000


@lru_cache(maxsize=None)
def naive(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    leftmost_match = s.find(s[-1], 0, len(s) - 1)
    if leftmost_match == -1:
        return naive(s[:-1])
    return max(naive(s[leftmost_match + 1 : -1]) + 2, naive(s[:-1]))


s = "MAPTPTMTPA"
assert naive(s) == 7
