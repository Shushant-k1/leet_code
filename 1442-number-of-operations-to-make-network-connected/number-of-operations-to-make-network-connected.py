class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1 :
            return  - 1 

        adj = [[] for i in range(n)]

        for u , v in connections :
            adj[u].append(v)
            adj[v].append(u)
        
        vis = set()

        cnt = 0
        for i in range(n) :
            if i not in vis:
                self.dfs(i , adj , -1 , vis)
                cnt += 1
        
        return cnt - 1
        
        
    def dfs(self , node , adj , par ,vis) :
        
        vis.add(node)
        
        for neigh in adj[node] :
            if neigh not in vis :
                self.dfs(neigh , adj ,node ,vis)
