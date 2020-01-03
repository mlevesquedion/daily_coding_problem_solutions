from functools import lru_cache
import numpy as np


def solve(X):
    def helper(i, S):
        if i < 0:
            if np.isclose(0, S):
                return 0, []
            return float("inf"), []
        else:
            last = X[i]
            decimal = last % 1
            Sd, Xd = helper(i - 1, S - decimal)
            Su, Xu = helper(i - 1, S + (1 - decimal))
            if Sd < Su:
                return Sd, Xd + [last - decimal]
            return Su, Xu + [last + (1 - decimal)]

    return helper(len(X) - 1, 0)[1]


X = [1.3, 2.3, 4.4]
Y = solve(X)
print(Y)
print(np.sum(np.abs(np.array(X) - np.array(Y))))
