def getindex(l1, n):
    l = -1
    index = []
    for item in l1:
        l += 1
        if item == n:
            index.append(l)
    return index


def get_sum(l):
    sum=0
    for n in l:
        sum+=n
    return sum

def get_avg(l):
    sum=get_sum(l)
    return sum/len(l)