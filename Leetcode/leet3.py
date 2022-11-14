def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    longest=[]
    temp=[]
    for i in s:      
        print(temp)
        if i not in temp:
            temp.append(i)
        else:
            if len(temp)>1:
                temp=temp[temp.index(i)+1:]
                temp.append(i)
            else:
                temp=[]
                temp.append(i)
        if len(temp)>len(longest):
            longest=temp  
    
    return len(longest)



p=lengthOfLongestSubstring("dvdf")
print(p)











# s="abcdbf"
# print(s[s.index("b")+1:])
# for i,n in enumerate(s):
#     print()


# l=[2,123,4,35,223]
# n=[]
# n=l
# print(n)