class Solution(object):
    def restoreIpAddresses(self, s):
        n=len(s)
        ret=[]
        if n>12 or n<4:
            return
        def help(i, dots, curr):
            if dots==4 and i==n:
                ret.append(curr[:-1])
                return
            if dots>4:
                return
            for j in range(i, min(i+3,n)):
                if int(s[i:j+1])<256 and (i==j or s[i]!='0'):
                    help(j+1,dots+1,curr+s[i:j+1]+'.')
        help(0,0,'')
        return ret

# s="aw.daw.ad.ad"
# print(s.split('.'))
