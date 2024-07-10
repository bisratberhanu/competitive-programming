# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ar = [x[0] for x in points]
        
        ar.sort()
        ans=0
        for i in range(0,len(ar)-1):
            ans= max(ans, ar[i+1]-ar[i])
        return ans 
        