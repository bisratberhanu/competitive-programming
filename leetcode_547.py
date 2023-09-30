class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph= defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and j!=i:
                    graph[i+1].append(j+1)
        
        visited= set()
        def dfs(graph,node,visited):
            if node in visited:
                return
            visited.add(node)
            for neh in graph[node]:
                dfs(graph,neh,visited)
            return True
        counter=0
        for i in range(1,len(isConnected)+1):
            if i not in graph:
                counter+=1
                continue
            if dfs(graph,i,visited)==True:
                counter+=1
        return counter 
            
        
