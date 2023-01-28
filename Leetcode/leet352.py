class SummaryRanges(object):

    def __init__(self):
        self.ans=set()
    def addNum(self, value):
        self.ans.add(value)
        

    def getIntervals(self):
        ret,l,r=[],-1,-1
        for a in self.ans:
            if l<0:
                l=r=a
            elif r+1==a:
                r=a
            else:
                ret.append([l,r])
                l=r=a
            ret.append([l,r])
            return(ret)

a=set()
a.add(0)
a.add(6)
a.add(6)
a.add(4)
a.add(8)
a=set(sorted(a))
print(a)