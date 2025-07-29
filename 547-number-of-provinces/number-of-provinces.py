class Solution:
    def adj_mat(self , graph) :

        adj = []
        n , m = len(graph) , len(graph[0])
        for i in range(n) :
            temp = []
            for j in range(m) :
                if graph[i][j] == 1  and i != j:
                    temp.append(j)
            adj.append(temp)
        
        return adj
            


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = self.adj_mat( isConnected)
        print(adj)
        vis = set()
        cnt = 0
        for i in range(len(adj)) :
            if i not in vis :
                vis.add(i)
                cnt += 1
                self.dfs( i , adj , vis)
        return cnt

        
    def dfs(self , node , graph , vis) :

        for neigh in graph[node] :
            if neigh not in vis :
                vis.add(neigh)
                self.dfs(neigh , graph , vis)
        

