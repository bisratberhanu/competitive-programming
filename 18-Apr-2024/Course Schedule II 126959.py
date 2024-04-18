# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph= [[] for node in range(numCourses)]
        indegree= [0]* numCourses
        for next, prev in prerequisites:
            graph[prev].append(next)
            indegree[next]+=1
        queue= deque()
        for node in range(numCourses):
            if not indegree[node]:
                queue.append(node)
        
        order= []

        while queue:
            cur= queue.popleft()
            order.append(cur)
            for neigh in graph[cur]:
                indegree[neigh]-=1
                if not indegree[neigh]:
                    queue.append(neigh)

        if len(order) < numCourses:
            return []
        return order          