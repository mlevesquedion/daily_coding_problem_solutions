from collections import defaultdict


def group(words, prefix_size):
    groups = defaultdict(list)
    prefixes = []
    for w in words:
        if len(w) < prefix_size:
            prefixes.append([w])
        else:
            groups[w[:prefix_size]].append(w)
    return prefixes + list(groups.values())


def solve(words):
    results = []
    prefix_size = 1
    groups = group(words, prefix_size)
    while groups:
        words = []
        for g in groups:
            if len(g) == 1:
                results.append(g[0][:prefix_size])
            else:
                words += g
        prefix_size += 1
        groups = group(words, prefix_size)
    return results


if __name__ == "__main__":
    words = 'dog cat car apple apple apricot fish'.split()
    print(solve(words))
