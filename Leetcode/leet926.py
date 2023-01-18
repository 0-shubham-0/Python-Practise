def minFlipsMonoIncr(s):
    ans=[]
    temp=0

    for i in range(len(s)):
        
        if s[i]=='1':
            for j in range(i+1,len(s)):
                if s[j]=='0':
                    temp+=1
            print(temp)
            ans.append(temp)
        temp=len(ans)
    print(ans)


def minFlipsMonoIncr(self, s):
    ans1=[]
    ans2=[]
    temp=0
    for i in range(len(s)):
        if s[i]=='1':
            for j in range(i+1,len(s)):
                if s[j]=='0':
                    temp+=1
            ans1.append(temp)
            print(temp)
        temp=len(ans)
    temp=0
    for i in range(len(s)):
        if s[i]=='0':
            for j in range(i+1,len(s)):
                if s[j]=='1':
                    temp+=1
            ans.append(temp)
            print(temp)
        temp=len(ans)
    return(min(min(ans1),min(ans2))
s = "010110"
mono=False
temp=False
for i in range(len(s)):
    if s[i]=='1':
        temp=True
minFlipsMonoIncr(s)
