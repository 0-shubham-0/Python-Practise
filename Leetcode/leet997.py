class Solution(object):
    def findJudge(self, n, trust):
        t=[0 for _ in range(n)]
        for i in trust:
            t[i[1]-1]+=1
            t[i[0]-1]-=1
        print(t)
        for i in range(len(t)):
            if t[i]==n-1:
                return i+1
        return -1
