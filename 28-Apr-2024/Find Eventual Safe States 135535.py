# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n= len(graph)
        safe= {}
        res=[]
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]= False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i]= True
            return True 
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res


        