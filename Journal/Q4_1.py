import sys
ch=0
while ch!=2:
    ch=int(input('1.Input\t\t2.Exit'))
    if ch==1:
        i=int(input('Enter Index : '))
        try:
            my_list = [3,7, 9, 4, 6]
            print(my_list[i])
        except IndexError as e:
            print (e)
            