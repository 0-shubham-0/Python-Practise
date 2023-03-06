class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        m=1
        while k and m<arr[0]:
            k-=1
            if k==0:return m
            m+=1
        for i in range(1,n):
            if arr[i-1]!= arr[i]-1:
                m=arr[i-1]
                while m<arr[i]-1:
                    m+=1
                    k-=1
                    if k==0:return m
        m=arr[-1]
        while k:
            m+=1
            k-=1
            if not k: return m