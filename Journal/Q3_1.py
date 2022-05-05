def fact(no):
    i = 1
    factorial = 1
    while i <= no:
        factorial = factorial * i
        i = i + 1
    print("factorial of ", no, ' is ', factorial)


num = int(input('Enter Number : '))
fact(num)
