class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)-1):
            val1= abs(points[i][0]- points[i+1][0])
            val2= abs(points[i][1]- points[i+1][1])
            ans+= max(val1,val2)
        return ans 