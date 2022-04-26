x = 'global'


def f():
    x = 2
    # x = x + 2 will an give error
    print(x)


f()
