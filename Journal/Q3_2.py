def si(n,p,r):
    sim=float((n*p*r)/100)
    return sim
p=int(input('Enter principle amount  : '))
n=int(input('Enter Time period : '))
r=int(input('Enter Rate of interest : '))
sim=si(n,p,r)

print('Simple Interest : ',sim)