n = int(input('Enter digit : '))
num=int(input('Enter no : '))
i=0
print('Reverse No : ',end='')
while i<n:
    di=num%10
    num=num/10
    print(int(di),end='')
    i=i+1
