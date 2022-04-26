# reverse
number = int(input('Enter no : '))
print('Reverse No : ', end='')
while number > 1:
    reverse_digit = number % 10
    number = number / 10
    print(int(reverse_digit), end='')
