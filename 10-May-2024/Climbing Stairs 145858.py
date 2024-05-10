# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        dic={0:1}
        def dp(n):
            if n==0:
                return 1
            if n<0:
                return 0
            if n in dic:
                return dic[n]
            
            case1= dp(n-1)
            case2= dp(n-2)
            dic[n]= case1 + case2
            return dic[n]
        
        return dp(n)