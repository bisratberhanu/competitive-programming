# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]],quiet: List[int]) -> List[int]:
        graph= [[] for i in range(len(quiet))]
        output= [None for i in range(len(quiet))]
        for conn in richer:
            graph[conn[1]].append(conn[0])
        
        def dfs(graph, source,quiet, output):
            minn= source #qq reprsents intial quitness
            for neh in graph[source]:
                if output[neh] is None:
                    dfs(graph, neh,quiet,output)
                minn= min(minn, output[neh], key= lambda x:quiet[x])
            output[source]= minn
        
        for person in range(len(quiet)):
            if output[person] is None:
                dfs(graph, person, quiet, output)
        return output 


