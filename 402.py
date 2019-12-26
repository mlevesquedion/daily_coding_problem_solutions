from itertools import product


strobes = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}


def flip_180(n):
    return strobes.get(n, -1)


def digits(n):
    if n == 0:
        return []
    div, mod = divmod(n, 10)
    return digits(div) + [mod]


def is_strobogrammatic(n):
    digits_ = digits(n)
    return digits_ == [flip_180(d) for d in reversed(digits_)]


assert is_strobogrammatic(16891)


# O(10^n)
def naive(n_digits):
    for i in range(10 ** (n_digits - 1), 10 ** (n_digits)):
        if is_strobogrammatic(i):
            yield i


[print(i) for i in naive(4)]


"""
We can save time by generating just the numbers we care about.
Still exponential though: O(|S|^(N/2)) where S is the set of numbers that
have a corresponding "flipped" number and N is the number of digits.
"""


def optimized(n_digits):
    half = product(*(list(strobes) for _ in range(n_digits // 2)))
    for h in half:
        digits_ = list(h)
        digits_flipped = [strobes[n] for n in reversed(digits_)]
        if n_digits % 2:
            for s in strobes:
                yield digits_flipped + [s] + digits_
        else:
            yield digits_flipped + digits_


[print(i) for i in optimized(4)]
