class Solution:
    def arraySign(self, nums: List[int]) -> int:
        for i in nums[1:]:
            nums[0]*=i
        if nums[0]>0:return 1
        if nums[0]<0:return -1
        return 0