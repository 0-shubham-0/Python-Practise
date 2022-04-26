i = 100
print('Nos from 100 to 200 divisible by 4 & 7 : ', end=' ')
while i < 201:
    if i % 4 == 0 and i % 7 == 0:
        print(i, end=' ')
    else:
        pass
    i = i + 1
