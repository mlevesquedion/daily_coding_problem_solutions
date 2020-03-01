import math


def sqrt(n, epsilon=1e-10):
    lo, hi = 1, n
    mid = 1
    while abs(mid*mid - n) > epsilon:
        mid = (lo + hi) / 2
        if mid * mid > n:
            hi = mid
        else:
            lo = mid
    return mid


assert all(abs(sqrt(x) - math.sqrt(x)) < 1e-9 for x in [1, 9, 13])
