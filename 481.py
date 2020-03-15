import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def evaluate(program):
    stack = []
    for data in program:
        if isinstance(data, int):
            stack.append(data)
        else:
            stack.append(operations[data](stack.pop(), stack.pop()))
    return stack.pop()


assert evaluate([5, 3, '+']) == 8
assert evaluate([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5

