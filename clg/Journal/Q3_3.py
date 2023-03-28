def gross_p(ns):
    gs = ns + ns * 0.15
    return gs


ns = int(input('Enter Net salary : '))
ch = int(input('\n\n1.Temporarily Employee\t\t2.Permanent Employee\t\t3.Exit \n'))
if ch == 1:
    print('Gross Salary : ', ns)
elif ch == 2:
    print('Gross Salary : ', gross_p(ns))
elif ch == 3:
    exit()
else:
    print("Invalid choice")
