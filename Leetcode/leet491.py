def findSubsequences(nums):
    ret=[]
    ans_count={}
    def comb(num):
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                if ans_count.get(str(num[i:j+1]),0)==0:
                    print(1)
                    ret.append([num[i:j+1]])
                    ans_count[str(num[i:j+1])]=1+ans_count.get(str(num[i:j+1]),0)
    
    for i in range(1,len(nums)):
        if nums[i]>=nums[i-1]:
            comb(nums[0:i+1])
    print(ret,ans_count)

nums=[1,2,3,4,5]
findSubsequences(nums)

# print(nums[1:5])
# str(nums[1:5])
# dict={[1,2,3]:1}
# # dict[]
# print(dict.get([1,2,3]))
