from pprint import pprint
from math import ceil
from collections import Counter
from functools import partial
from random import randint

rand5 = partial(randint, 1, 5)


def rand7():
    roll = ceil((5 * (rand5() - 1) + rand5()) / 3)
    return roll if roll <= 7 else rand7()


pprint(sorted(Counter(rand7() for _ in range(100_000)).items()))
