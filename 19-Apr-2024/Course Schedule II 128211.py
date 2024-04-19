# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph= [[] for node in range(numCourses)]
        for next, prev in prerequisites:
            graph[prev].append(next)
        
        order=[]
        colors= [0]* numCourses

        def dfs(node):
            if colors[node]==1:
                return False 
            colors[node]= 1
            for next in graph[node]:
                if colors[next]==2:
                    continue
                if not dfs(next):
                    return False
            colors[node]=2
            order.append(node)
            return True
        
        for node in range(numCourses):
            if colors[node]!=0:
                continue
            if not dfs(node):
                return []
        order.reverse()
        return order 
