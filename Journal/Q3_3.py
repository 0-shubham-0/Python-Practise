def gross_p(ns):
    gs=ns + ns *0.15
    return gs
ch=0
while ch!=3:
    ch=int(input('\n\n1.Temporarily Employee\t\t2.Permanent Employee\t\t3.Exit \n'))
    if ch==2:
        ns=int(input('Enter Net salary : '))
        print('Gross Salary : ',gross_p(ns))
    elif ch==3:
        exit()
    else :

        ns=int(input('Enter Net salary : '))
        print('Gross Salary : ',ns)

