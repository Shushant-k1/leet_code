class Solution:
    def adj_mat(self , graph) :
        adj = { }
        for i in range(len(graph)) :
            cur = []
            for j in range(len(graph)) :
                if graph[i][j] == 1  and i != j:
                    cur.append(j)
            adj[i] = cur
        return adj

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        _adj_mat = self.adj_mat(isConnected)
        ans = 0
        vis = set()
        for i in range(len(isConnected)) :
            if i not in vis :
                vis.add(i)
                ans += 1
                self.dfs( i , _adj_mat , vis)
        return ans
        
    def dfs(self , node , graph , vis) :
        vis.add(node)
        for neigh in graph[node] :
            if neigh not in vis :
                self.dfs(neigh , graph , vis)


