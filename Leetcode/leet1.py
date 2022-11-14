def twoSum_bruteforce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(list)):
        for j in range(i+1,index):
            if list[i]+list[j]==target:
                return [i,j]

def twoSum_onepass(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    prevMap={}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n]=i
    return
    


# print(twoSum([1,2,3],5))


list=[1,23,45,0]
target=23
index=len(list)
print(twoSum_bruteforce(list,target))
