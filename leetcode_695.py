class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions= [(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()
        rows,cols= len(grid), len(grid[0])
        self.countr=0
        def dfs(grid,start,visited):
            if start in visited:
                return
            visited.add(start)
            self.countr+=1
            row,col= start[0],start[1]
            for dr,dc in directions:
                new_row,new_col= row+dr, col+dc
                if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1:
                    
                    dfs(grid,(new_row,new_col), visited)
                    
            return self.countr
        counter=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    dfs(grid,(i,j),visited)
                    print(self.countr)
                    counter= max(counter,self.countr)
                    self.countr=0
        return counter


        
