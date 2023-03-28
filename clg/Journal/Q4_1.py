my_list = [3, 7, 9, 4, 6]
print(my_list)
i = int(input('Enter Index : '))
try:
    print(my_list[i])
except IndexError as e:
    print(e)

try:
    print(0/0)
except Exception as e:
    print(e)