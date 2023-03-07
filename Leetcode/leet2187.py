class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 0, min(time) * totalTrips
        def val(m):
            total=0
            for i in time:
                total+=m//i
                if total>=totalTrips:return True
            return False
        while lo <= hi:
            mid = (lo+hi) // 2
            tt = val(mid)
            if tt:hi = mid - 1
            else:lo = mid + 1
        return lo