def maxPoints(points: list[list[int]]) -> int:
    if len(points) == 1:
        return 1
    if len(points) == 2:
        return 2
    dict={}
    max=0
    for i in range(len(points)):
        t_slope=0
        for j in range(i+1,len(points)):
            if points[i][0] == points[j][0]:
                slope=100000
            else:
                slope=(points[j][1]- points[i][1])/(points[j][0]- points[i][0])
            if dict.__contains__(slope):
                dict[slope]+=1
            else:
                dict[slope]=1
            t_slope=t_slope if t_slope>dict[slope] else dict[slope]
            print(dict)
        dict.clear()
        max=max if max>t_slope else t_slope
    print(max+1)






points=[[1,1],[2,2],[3,3]]
# print(points[2][1]- points[1][1]/points[2][0]- points[1][0])
maxPoints(points)