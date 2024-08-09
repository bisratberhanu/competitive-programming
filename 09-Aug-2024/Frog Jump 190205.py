# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1: return False 						
        
        ind = {v:i for i,v in enumerate(stones)}		
        
        @cache
        def dfs(i,lastStep):
            if i==len(stones)-1: 							
                return True
            res = False
            for curStep in range(lastStep-1,lastStep+2):	
                if stones[i]+curStep in ind and ind[stones[i]]+curStep>i:	
                    res = res or dfs(ind[stones[i]+curStep],curStep)
            return res
        
        return dfs(1,1)


        