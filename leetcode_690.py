"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph= defaultdict(list)
        visited= set()
        self.total_importance=0
        for relation in employees:
            ids, importance= relation.id,relation.importance
            subordinates= relation.subordinates
            graph[ids].append(importance)
            graph[ids].append(subordinates)
        
        def bfs(graph,startid,visited):
            queue= deque()
            queue.append(startid)
            while queue:
                popped= queue.pop()
                self.total_importance+= graph[popped][0]
                for neh in graph[popped][1]:
                    if neh not in visited:
                        visited.add(neh)
                        queue.appendleft(neh)
            return self.total_importance
        return bfs(graph,id,visited)
        
        
        
