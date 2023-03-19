class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        count,r = 0,0
        n= len(nums)
        for i in range(n):
            while r<n and nums[r]<=nums[i]:
                r+=1
            if r<n:
                count+=1
                r+=1
        return count