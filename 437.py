# O(|s|^2 * |chars|)
def brute(s, chars):
    return min(
            filter(
                lambda s: not (chars - set(s)),
                (s[i:j] for i in range(len(s) - len(chars) + 1) for j in
                    range(i + len(chars), len(s) + 1))
            ),
        key=len)


# O(|s| * |chars|)
# could improve to O(|s| * log(|chars|)) by using a binary search tree
def better(s, chars):
    closest_occurrence = {}
    min_length = float('inf')
    min_interval = None
    for i, c in enumerate(s):
        if c in chars:
            closest_occurrence[c] = i
        if len(closest_occurrence) == len(chars):
            closest = min(closest_occurrence.values())
            if i - closest < min_length:
                min_length = i - closest
                min_interval = (closest, i)
    return min_interval is not None and s[min_interval[0]:min_interval[1]+1] or None


assert brute('figehaeci', set('aei')) == 'aeci'
assert better('figehaeci', set('aei')) == 'aeci'
