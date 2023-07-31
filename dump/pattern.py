n=5
i=1
f1=True
while i>0:
    t=i
    f=True
    for j in range(1,n-i+1):
        print(" ",end="")
    while t<i+1:
        print(t,end="")
        if t==1:f=False
        if f:t-=1
        if not f:t+=1
    print()
    if i==n:f1=False
    if f1:i+=1
    if not f1:i-=1
