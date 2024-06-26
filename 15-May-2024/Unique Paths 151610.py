# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[1 for i in range(n)]for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

        