import heapq
class Solution(object):
    def max_score(self, nums1, nums2, k):
        new=sorted(zip(nums1,nums2),key=lambda x:x[-1])
        best,h,curr_sum=0,[],0
        for nums1,nums2 in new:
            curr_sum+=nums1
            heapq.heappush(h,nums1)
            if len(h)>k:
                curr_sum-=heapq.heappop(h)
            if len(h)==k:
                best=max(best,(curr_sum*nums2))
        return best

# x = lambda x:x[-1]
# print((lambda x: x/2)(10))