import random

min_, max_ = 1, 1_000_000
sample_size = 999_000
nums = list(range(min_, max_))
sample = random.sample(nums, sample_size)

all_nums = set(nums)
for n in sample:
    all_nums.remove(n)

print(sorted(all_nums))

# O(1) space and time because the input is bounded...
