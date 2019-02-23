from collections import defaultdict


def solve(words):
    # Quadratic in |words|
    results = []
    for i, a in enumerate(words):
        for j in range(len(words)):
            if i == j:
                continue
            b = ''.join(reversed(words[j]))
            if a == b or a[:-1] == b:
                results.append((i, j))
    return results


_reversed = reversed


def reversed(s):
    return ''.join(_reversed(s))


def solve(words):
    # Best case is linear
    # Worst case is still quadratic, e.g. if all words are the same
    # Could be improved using a Trie
    """
    evens are candidates for even length palindromes, e.g. code + edoc
    odds are candidates for odd length palindromes, e.g. code + doc
    """
    evens = defaultdict(list)
    odds = defaultdict(list)
    results = []
    for i, w in enumerate(words):
        if reversed(w) in evens:
            results += [(i, j) for j in evens[reversed(w)]]
            results += [(j, i) for j in evens[reversed(w)]]
        if reversed(w) in odds:
            results += [(j, i) for j in odds[reversed(w)]]
        evens[w].append(i)
        odds[w[:-1]].append(i)
    return results


if __name__ == '__main__':
    words = ['code', 'edoc', 'da', 'd', 'doc']
    expected = [(0, 1), (0, 4), (1, 0), (2, 3)]
    print(solve(words))
