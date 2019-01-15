def parens(s):
    stack = []
    count = 0
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                count += 1
            else:
                stack.pop()
    return count + len(stack)


if __name__ == '__main__':
    for case, expected in [
        ('()())()', 1),
        (')(', 2)
    ]:
        print(case, parens(case), expected)
