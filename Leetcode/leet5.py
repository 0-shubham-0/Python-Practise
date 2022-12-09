class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resl=0
        p=len(s)
        left,right=0,0
        for i in range(p):
            #odd pali
            l,r=i,i
            while l>=0 and r<p and s[l]==s[r]:
                if resl<r-l+1:
                    resl=r-l+1
                    left,right=l,r
                l-=1
                r+=1
            #even pali
            l,r=i,i+1
            while l>=0 and r<p and s[l]==s[r]:
                if resl<r-l+1:
                    resl=r-l+1
                    left,right=l,r
                l-=1
                r+=1
        return s[left:right+1]