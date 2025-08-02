class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        adj = [[] for i in range(n)]

        for i in range(n ) :
            for j in range(i + 1 , n) :
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1] :
                    adj[i].append(j)
                    adj[j].append(i)
        
        components = 0
        vis = set()
        for i in range(n) :
            if i not in vis :
                components += 1
                self.dfs(vis , i , adj)
        
        return n - components

    def dfs(self , vis , node , adj) :

        vis.add(node)
        for neigh in adj[node] :
            if neigh not in vis:
                vis.add(neigh)
                self.dfs(vis , neigh , adj)
    
