from itertools import combinations
from collections import Counter
from collections import defaultdict

pairs = [('a', 1), ('a', 3), ('a', 5), ('b', 2), ('b', 6),
         ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
         ('d', 4), ('d', 5), ('d', 6), ('d', 7),
         ('e', 1), ('e', 3), ('e', 5), ('e', 6)]


def k_most_similar_sites(pairs, k):
    n_users = len({p[1] for p in pairs})
    by_user = [set() for _ in range(n_users)]
    for site, user in pairs:
        by_user[user - 1].add(site)
    counts = defaultdict(int)
    for group in by_user:
        sites = [p[0] for p in list(group)]
        site_pairs = combinations(sites, 2)
        for site1, site2 in site_pairs:
            counts[frozenset(sorted([site1, site2]))] += 1
    print(counts)
    return Counter(counts).most_common(k)


print(k_most_similar_sites(pairs, 1))
