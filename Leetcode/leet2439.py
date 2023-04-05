class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total,res=0,0
        for i,n in enumerate(nums):
            total+=n
            res=max(res,ceil(total/(i+1)))
        return res