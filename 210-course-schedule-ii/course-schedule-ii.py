class Solution:

    def adj(self , equations):
        d = {}
        for node in (equations):
            en , st = node
            
            if st not in d:
                d[st] = []
            d[st].append((en))
            
            # if en not in d :
            #     d[en] = []
            # d[en].append(st)
        return d
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mat = self.adj(prerequisites)
        indegree = [0] * numCourses 
        for i , j  in prerequisites :
            indegree[i] += 1
        ind_zer_ele = deque()
        ans = []
        for i in range(numCourses)  :
            if indegree[i] == 0 : 
                ind_zer_ele.append(i)
                ans.append(i)


        while ind_zer_ele :
            ele = ind_zer_ele.popleft()
            if ele not in adj_mat :
                continue
            for neigh in adj_mat[ele] :
                indegree[neigh] -= 1
                if indegree[neigh] == 0 :
                    ans.append(neigh)
                    ind_zer_ele.append(neigh)
    
        for i in indegree :
            if i != 0 : return []
        return ans
