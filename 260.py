import random
from collections import deque


def sequence(clues):
    numbers = deque(range(len(clues) + 1))
    answer = deque()
    for i in range(len(clues) - 1, 0, -1):
        if clues[i] == '+':
            answer.appendleft(numbers.pop())
        else:
            answer.appendleft(numbers.popleft())
    return list(numbers) + list(answer)


def is_valid(sequence, clues):
    for i in range(len(clues) - 1, 0, -1):
        if clues[i] == '+' and sequence[i + 1] <= sequence[i] \
                or clues[i] == '-' and sequence[i + 1] >= sequence[i]:
            return False
    return True


def generate_clues(n):
    return ''.join('-+'[random.randint(0, 1)] for _ in range(n))


if __name__ == "__main__":
    for i in range(100):
        clues = generate_clues(i)
        solution = sequence(clues)
        if not is_valid(solution, clues):
            print(solution, clues)
            exit(1)
