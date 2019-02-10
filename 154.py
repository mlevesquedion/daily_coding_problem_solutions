from heapq import *


class Stack:

    def __init__(self):
        self.counter = 0
        self.heap = []

    def push(self, val):
        heappush(self.heap, (-self.counter, val))
        self.counter += 1

    def pop(self):
        return heappop(self.heap)[1]


if __name__ == "__main__":
    s = Stack()
    vals = [1, 2, 3]
    for v in vals:
        s.push(v)
    assert list(reversed(vals)) == [s.pop() for _ in range(len(vals))]
