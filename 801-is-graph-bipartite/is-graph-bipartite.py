class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = {}
        
        for i in range(len(graph)) :
            if i not in vis :
                if not self.dfs(graph , vis , i , 1) : return False
        return True



    def dfs(self , graph , vis , cur , prevcol) :

        vis[cur] = prevcol
        for neigh in graph[cur] :
            if neigh in vis :
                if vis[neigh] == vis[cur]:

                    return False
            else :
                if not self.dfs(graph , vis , neigh , prevcol ^ 1) :
                    return False
        
        return True