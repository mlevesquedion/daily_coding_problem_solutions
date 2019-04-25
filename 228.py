def solve(nums):
    padding = max(nums, key=lambda x: len(str(x)))

    def pad(s):
        return (s + padding * '9')[:padding]

    return int(''.join(sorted(map(str, nums), key=pad, reverse=True)))


if __name__ == "__main__":
    print(solve([10, 7, 76, 415]))
