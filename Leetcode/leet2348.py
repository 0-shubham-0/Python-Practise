class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr,ret=0,0
        for i in nums:
            if not i:
                curr+=1
                ret+=curr
            else:curr=0
        return ret