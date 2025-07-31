class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.adj_mat(prerequisites , numCourses)
        print(adj)
        vis = set()
        restack = set()
        cnt = 0
        for i in range(numCourses) :
            if i  not in vis :
                if  self.dfs(adj , vis ,i, restack) :
                    return False
        return True
    

    def dfs(self ,adj , vis , cur , restack)   :
        vis.add(cur) 
        restack.add(cur)

        for neigh in adj[cur] :
            if neigh not in vis :
                if self.dfs(adj , vis , neigh  , restack ) : 
                    return True
            elif neigh in restack :
                return True
        restack.remove(cur)
        return False
    
    def adj_mat(self , prerequisites, numCourses) :

        adj = [[] for i in range(numCourses)]

        for i , j in (prerequisites) :
            adj[j].append(i)

        return adj

