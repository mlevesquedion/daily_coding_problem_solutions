import numpy as np


def ispow4(n):
    mask = 0x55555555
    antimask = 0xAAAAAAAA
    return n == 1 or (n & n - 1) == 0 and (n & mask) != 0 and (n & antimask) == 0

powers = 4**np.arange(16)

assert all(ispow4(n) for n in powers)
for _ in range(10_000):
    not_powers = set(np.random.permutation(16) + powers) - set(powers)
    assert all(not ispow4(n) for n in not_powers)

