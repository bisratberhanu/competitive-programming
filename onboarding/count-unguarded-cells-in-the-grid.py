class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # the dfs approach
        direction= [(1,0),(0,1),(-1,0),(0,-1)]
        wallset= set()
        guardset= set()
        guardsetmain= set()
        for wall in walls:
            wallset.add((wall[0],wall[1]))
        for guard in guards:
            guardsetmain.add((guard[0],guard[1]))

        for guard in guards:
            
            
            for dx,dy in direction:
                xn,yn= guard[0],guard[1]
                xn= xn+dx
                yn= yn+dy
                
                while 0<=xn<m and 0<=yn<n and (xn,yn) not in wallset  and (xn,yn) not in guardsetmain:
                    guardset.add((xn,yn))
                    xn= xn+dx
                    yn= yn+dy
        
        
        maxval= n*m- len(wallset)-len(guardset)- len(guardsetmain)
        if maxval<0:
            return 0
        return maxval


             
        