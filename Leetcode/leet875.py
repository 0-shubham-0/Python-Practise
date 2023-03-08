class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        def val(m):
            need=0
            for i in piles:
                if i<m:
                    need+=1
                else:
                    if i%m:
                        need+=(i//m)+1
                    else:need+=i//m
                if need>h:
                    return False
            return True
        while(left<right):
            mid=(left+right)//2
            if val(mid):
                right=mid
            else:left=mid+1
        return left