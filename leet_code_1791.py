class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph= defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            if len(graph[edge[0]])>1: return edge[0]
            graph[edge[1]].append(edge[0])
            if len(graph[edge[1]])>1: return edge[1]
        

        
