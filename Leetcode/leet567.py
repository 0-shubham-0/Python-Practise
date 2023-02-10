def checkInclusion( s1, s2):
    l1,l2=len(s1),len(s2)
    dict1={}
    for i in s1:
        if not dict1.get(i,0):
            dict1[i]=1
        else: dict1[i]+=1
    new_dict=dict1.copy()
    a = True
    for i in range(len(s2)):
        print(i)
        if s2[i] in new_dict:
            print(new_dict)
            new_dict[s2[i]]-=1
            l1-=1
            while(a):
                if l1==0:
                    return True
                i+=1
                if new_dict.get(s2[i],0):
                    new_dict[s2[i]]-=1
                    l1-=1
                else: a=False
            a,l1=True,len(s1)
        new_dict=dict1.copy()
    return False
        
#     print(dict1)

s1 ="hello"
s2 ="ooolleoooleh"
print(checkInclusion(s1,s2))
# new(s,s)
# a={"a":1,"b":2}
# b={}
# b=a.copy()
# print(a,b)


arr= ["dwaf",2,4,5]

print(arr[0][1:])

s=set(arr)
print(s)
print(1 in s)