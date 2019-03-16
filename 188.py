def make_functions():
    return [(lambda x=i: print(x)) for i in range(1, 4)]


for f in make_functions():
    f()
