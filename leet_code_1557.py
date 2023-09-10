class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seen=set()
        for edge in edges:
            seen.add(edge[1])
        arr=[]
        for i in range(n):
            if i not in seen:
                arr.append(i)
        return arr 


        
