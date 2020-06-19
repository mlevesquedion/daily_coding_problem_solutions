from itertools import product


def throw_dice(N, faces, total):
    return sum(
        sum(throws) == total
        for throws in product(*(range(1, faces + 1) for _ in range(N)))
    )


assert throw_dice(3, 6, 7) == 15
