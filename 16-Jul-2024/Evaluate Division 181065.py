# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        # Step 1: Create the graph
        graph = defaultdict(dict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2: DFS function to find path value
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                path_value = dfs(neighbor, end, visited)
                if path_value == -1.0:
                    continue
                return graph[start][neighbor] * path_value
            return -1.0

        # Step 3: Answer the queries
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))

        return results