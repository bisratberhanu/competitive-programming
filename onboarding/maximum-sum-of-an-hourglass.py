class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                temp_sum= grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+ grid[i+2][j]+grid[i+2][j+1]+ grid[i+2][j+2]
                maxsum= max(temp_sum,maxsum)
        return maxsum


        