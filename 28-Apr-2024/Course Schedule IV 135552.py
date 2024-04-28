# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj= defaultdict(list)
        for prereq,crs in prerequisites:
            adj[crs].append(prereq)
        
        prereqmap= {}
        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs]=set()
                for prereq in adj[crs]:
                    prereqmap[crs] |= dfs(prereq)
            prereqmap[crs].add(crs)
            return prereqmap[crs]
        for crs in range(numCourses):
            dfs(crs)
        
        ans=[]
        for u,v in queries:
            if  u in prereqmap[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans 
