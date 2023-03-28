from max import getmax


def something(nu):
    num = {
        ':)': '😄',
        ':(': '😞'
    }
    split = nu.split(' ')
    o = ''
    for s in split:
        o += num.get(s, s) + ' '
    print(o)


inp = input(">")
something(inp)
h = [1, 2, 3, 4, 62, 13, 32]
print(getmax(h))
