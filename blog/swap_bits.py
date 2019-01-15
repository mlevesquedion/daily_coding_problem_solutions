def swap_bits(x):
    b = bin(x)[2:].zfill(8)
    evens = [b[i] for i in range(0, 8, 2)]
    odds = [b[i] for i in range(1, 8, 2)]
    return int(''.join(intersperse(odds, evens)), 2)


def swap_bits(x):
    odd_bitmask = 0b10101010
    even_bitmask = 0b01010101
    return (x & odd_bitmask) >> 1 | (x & even_bitmask) << 1


def flatten(arr):
    if not arr:
        return []
    first, *rest = arr
    if isinstance(first, list) or isinstance(first, tuple):
        return flatten(first) + flatten(rest)
    else:
        return [first] + flatten(rest)


def intersperse(a, b):
    return flatten(x for x in zip(a, b))


def intersperse(xs, ys):
    if not xs or not ys:
        return []
    return [xs[0], ys[0]] + intersperse(xs[1:], ys[1:])


def intersperse(x, y):
    inter = []
    for a, b in zip(x, y):
        inter.append(a)
        inter.append(b)
    return inter


if __name__ == '__main__':
    for x, y in [
        (10, 5),
        (5, 10),
        (0, 0),
        (1, 2),
        (2, 1),
        (11, 7),
    ]:
        print(x, y, swap_bits(x))
