class Solution:
        
    from collections import defaultdict
    def checkIfPrerequisite(self , numCourses, prerequisites, queries):
        # Build the graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # Precompute reachability using DFS
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for course in range(numCourses):
            stack = [course]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not reachable[course][neighbor]:
                        reachable[course][neighbor] = True
                        stack.append(neighbor)
        
        # Answer the queries
        answer = []
        for u, v in queries:
            answer.append(reachable[u][v])
        return answer