class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry,sum=0,0
        for i in range(len(num)-1,-1,-1):
            sum=num[i]+int(k%10)+carry
            num[i]=sum%10
            if sum>9:carry=1
            else: carry=0
            sum=0
            k=int(k/10)
        while(k):
            sum=int(k%10)+carry
            num=[sum%10]+num
            if sum>9:carry=1
            else: carry=0
            k=int(k/10)
        if carry:return [1]+num
        return num