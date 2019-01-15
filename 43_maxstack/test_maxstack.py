class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or self.max() < value:
            self.max_stack.append(value)

    def pop(self):
        popped = self.stack.pop()
        if popped == self.max():
            self.max_stack.pop()
        return popped

    def max(self):
        return self.max_stack[-1]

    def empty(self):
        return not self.stack


def test():
    s = MaxStack()
    s.push(10)
    s.push(30)
    s.push(20)
    assert s.max() == 30
    assert s.pop() == 20
