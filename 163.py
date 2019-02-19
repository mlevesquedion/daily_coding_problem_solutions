from operator import add, sub, truediv, mul

ops = {symb: func for symb, func in zip('+-*/', [add, sub, mul, truediv])}


def rpn(expression):
    stack = []
    for x in expression:
        if isinstance(x, int):
            stack.append(x)
        else:
            stack.append(ops[x](stack.pop(), stack.pop()))
    return stack.pop()


if __name__ == "__main__":
    print(rpn([5, 3, '+']))
    print(rpn([
        15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'
    ]))
