def getmax(list):
    max=list[0]
    for num in list:
        if max<num:
            max=num
    return max