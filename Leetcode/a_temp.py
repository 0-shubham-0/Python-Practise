nums = [0,1,2,2,3,0,4,2]
val = 2
ind=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[ind]=nums[i]
        ind+=1
print(nums)