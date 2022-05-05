# Even Odd
beginning = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))
even = []
odd = []
while beginning <= end:
    if beginning % 2 == 0:
        even.append(beginning)
    else:
        odd.append(beginning)
    beginning = beginning + 1
print('Even nos. are ', even)
print('Odd nos. are ', odd)
