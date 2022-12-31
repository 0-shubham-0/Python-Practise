class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # res = 0
        # for L in range (len(height)):
        #     for r in range(L + 1, len(height)):
        #         area = (r - L) * min(height[L], height[r])
        #         res = max(res, area)

        # return res
        
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            area = (r - l) * min (height[l], height[r])
            res = max (res, area)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return res