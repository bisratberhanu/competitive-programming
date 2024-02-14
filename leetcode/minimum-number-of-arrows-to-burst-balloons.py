class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # greedy
        points.sort()
        ans=1
        
        if len(points)==1: return 1
        start, end= points[0][0], points[0][1]
        for i in range(1,len(points)):
            start= max(start,points[i][0])
            end= min(end, points[i][1])
            if start>end:
                ans+=1
                start, end= points[i][0], points[i][1]
        return ans 
            


        