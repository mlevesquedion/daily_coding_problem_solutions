import random

BIAS = random.randrange(1, 100) / 100


def toss_biased():
    return random.random() > BIAS


def toss_coin():
    first = toss_biased()
    second = toss_biased()
    if first == second:
        return toss_coin()
    return first


def mean(arr):
    return sum(arr) / len(arr)


def is_biased(coin):
    throws = [coin() for _ in range(10000)]
    return abs(mean(throws) - 0.5) > 0.01


if __name__ == '__main__':
    print(BIAS)
    print(toss_biased())
    print(is_biased(toss_coin))
