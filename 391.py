from pprint import pprint


# Speeds up subsequent "word" comparisons, saves time overall if URLs are very long
# Does not affect time complexity
def tokenize(user1, user2):
    vocab = set(user1) | set(user2)
    ix2w = dict(enumerate(vocab))
    w2ix = {w: i for i, w in ix2w.items()}
    user1 = [w2ix[w] for w in user1]
    user2 = [w2ix[w] for w in user2]
    return user1, user2, ix2w


# O(n^2) dynamic programming solution
# This problem is simply the LCSubstring problem in (very slight) disguise
def solve(user1, user2):
    user1, user2, ix2w = tokenize(user1, user2)

    table = [[0 for _ in range(len(user1) + 1)] for _ in range(len(user2) + 1)]

    max_length = 0
    max_length_coords = None

    for i in range(1, len(user2) + 1):
        for j in range(1, len(user1) + 1):
            if user1[j - 1] == user2[i - 1]:
                max_so_far = max(
                    table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]
                )
                table[i][j] = max_so_far + 1
                if max_so_far == max_length:
                    max_length = max_so_far + 1
                    max_length_coords = (i, j)
            else:
                table[i][j] = 0

    solution = []
    i, j = max_length_coords
    while table[i][j] > 0:
        solution.append(user1[i - 1])
        i, j = i - 1, j - 1

    return [ix2w[w] for w in reversed(solution)]


user1 = "/home /register /login /user /one /two".split()
user2 = "/home /red /login /user /one /pink /two".split()
expected = "/login /user /one".split()
assert solve(user1, user2) == expected
