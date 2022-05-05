p = [1, 2.3, 'a', 'last', 21, 'first']
ints = 0
strings = 0
floats = 0
bools = 0
for item in p:
    if type(item) == int:
        ints += 1
    elif type(item) == str:
        strings += 1
    elif type(item) == float:
        floats += 1
    elif type(item) == bool:
        bools +=1

print('number of integers in list is =', ints,
      'float =', floats,
      'strings =', strings,
      'booleans =', bools)
