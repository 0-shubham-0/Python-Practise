def fifteen(nums):
    nums.sort()
    sol=[]
    n,i=len(nums),0
    while(i<n):
        a,s,e=-nums[i],i+1,len(nums)-1
        while(s<e):
            if nums[s]+nums[e]==a:
                sol.append([-a,nums[s],nums[e]])
                while(s<e and nums[s]==nums[s+1]):s+=1
                while(s<e and nums[e]==nums[e-1]):e-=1
                s+=1
                e-=1
            elif nums[s]+nums[e]>a:
                e-=1
            else:s+=1
        while i is not len(nums)-1 and nums[i]==nums[i+1]:
            i+=2
        i+=1
    print(sol)
# i=0
# while(i<10):
#     i+=1
#     if i==5:
        
#     print(i)
nums=[-1,0,1,2,-1,-4]
fifteen(nums)

# for i in range(10):
#     print(i)
#     if i==5:
#         i+-