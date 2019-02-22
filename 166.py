class Iter2D:
    def __init__(self, two_d):
        self.two_d = two_d
        self.i = 0
        self.j = 0

    def next(self):
        ret = self.two_d[self.i][self.j]
        self.j += 1
        while self.has_next() and self.j == len(self.two_d[self.i]):
            self.j = 0
            self.i += 1
        return ret

    def has_next(self):
        return self.i < len(self.two_d)


if __name__ == '__main__':
    mat = [[1, 2], [3], [], [4, 5, 6]]
    it = Iter2D(mat)
    while it.has_next():
        print(it.next())
