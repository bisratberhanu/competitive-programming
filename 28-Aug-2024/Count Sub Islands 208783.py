# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(r, c):
            # Check bounds
            if r < 0 or c < 0 or r >= len(grid2) or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0
            
            is_sub_island = grid1[r][c] == 1
            
            is_sub_island &= dfs(r + 1, c)
            is_sub_island &= dfs(r - 1, c)
            is_sub_island &= dfs(r, c + 1)
            is_sub_island &= dfs(r, c - 1)
            
            return is_sub_island
        
        sub_islands_count = 0
        
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        sub_islands_count += 1
        
        return sub_islands_count
