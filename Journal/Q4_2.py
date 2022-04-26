import sys
ch=0
while ch!=2:
    ch=int(input('1.Input\t\t2.Exit'))
    if ch==1:
        a=int(input('Enter First No. : '))
        b=int(input('Enter Second No. : '))
        try:
            i = a/b 
            print('division : ',i)
        except ZeroDivisionError as e:
            print (e)