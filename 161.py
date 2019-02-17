def bits(x):
    return int('')


def flip(x):
    return bin(int(x, 2) ^ int('1' * 32, 2))


if __name__ == "__main__":
    print(flip('1010'))
