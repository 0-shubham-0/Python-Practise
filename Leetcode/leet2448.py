class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getcost(mid):
            return sum(abs(mid-num)*c for num,c in zip(nums,cost))
        
        l,r=min(nums),max(nums)
        ans=getcost(nums[0])
        while l<r:
            mid=(l+r)//2
            cost_1 = getcost(mid)
            cost_2 = getcost(mid+1)
            ans=min(cost_1,cost_2)
            if cost_1>cost_2: l=mid+1
            else:r=mid
        return ans