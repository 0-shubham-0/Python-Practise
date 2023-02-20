def help(s,e,nums,target):
    print(s,e)
    if s>=e:
        return s
    m=s+e
    m=int(m/2)
    if nums[m]==target:
        return m
    if nums[m]>target:
        return help(s,m-1,nums,target)
    else: return help(m,e,nums,target)
n=[1,3,5,6]
print(help(0,len(n)-1,n,0))