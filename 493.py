from collections import Counter
from random import random as rand01


def sample(nums, probs):
    position = rand01()
    prob_so_far = 0
    for n, p in zip(nums, probs):
        prob_so_far += p
        if position < prob_so_far:
            return n

nums = [1, 2, 3, 4]
probs = [0.1, 0.5, 0.2, 0.2]

distribution = dict(zip(nums, probs))
n_samples = 1_000_000
samples = [sample(nums, probs) for _ in range(n_samples)]
estimated_distribution = {n: count / len(samples) for n, count in Counter(samples).items()}

assert all(abs(distribution[n] - estimated_distribution[n]) < 1e-2 for n in nums)
