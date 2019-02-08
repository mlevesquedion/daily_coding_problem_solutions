import random


def solve(nums, probs):
    chosen = random.random()
    threshold = 0
    for n, p in zip(nums, probs):
        threshold += p
        if chosen < p:
            return n
