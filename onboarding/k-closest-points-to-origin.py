class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for i in points:
            d=math.sqrt((i[0]**2) +(i[1]**2))
            distance.append(d)
        distance.sort()
        copy= distance[0:k].copy()  # to prevent alaising of data 
        result=[]
        for i in points:
             d=math.sqrt((i[0]**2) +(i[1]**2))
             if d in copy:
                result.append(i)
        return result
