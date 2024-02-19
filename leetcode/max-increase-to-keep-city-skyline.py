class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        totsum=0
        for row in range(len(grid)):
            for col in range(len(grid)):
                rowmax= max(grid[row])
                colmax= max([grid[val][col] for val in range(len(grid))] )
                if grid[row][col]!= rowmax and  grid[row][col]!= colmax:
                    if min(colmax,rowmax)> grid[row][col]:
                        totsum+= min(colmax,rowmax) - grid[row][col]
        
        return totsum