def kClosest(self, points,k):
    list=[]
    for value in points:
        x=value[0]**2
        y=value[1]**2
        d= math.sqrt(x+y)
        list.append(d)
    list.sort()
    list2=list[0:k].copy()
    list3=[]
    for value in points:
        x=value[0]**2
        y=value[1]**2
        d= math.sqrt(x+y)
        if d in list2:
            list3.append(value)
    return list3