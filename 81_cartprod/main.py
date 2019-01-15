a = 'abcd'
b = 'efg'
c = 'hi'

x = [a, b, c]


def cart_prod(arr):
    return [x + p for x in arr[0] for p in cart_prod(arr[1:])] if arr else ['']


if __name__ == '__main__':
    for p in cart_prod(x):
        print(p)
