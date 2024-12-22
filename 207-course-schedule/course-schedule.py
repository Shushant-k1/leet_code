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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mat = self.adj(prerequisites)
        indegree = [0] * numCourses 
        for i , j  in prerequisites :
            indegree[i] += 1
        ind_zer_ele = deque()
        print(indegree)
        for i in range(numCourses)  :
            if indegree[i] == 0 : ind_zer_ele.append(i)
        if len(ind_zer_ele) == 0 : return False
        print(adj_mat)
        print(ind_zer_ele)
        while ind_zer_ele :
            ele = ind_zer_ele.popleft()
            if ele not in adj_mat :
                continue
            for neigh in adj_mat[ele] :
                indegree[neigh] -= 1
                if indegree[neigh] == 0 :
                    ind_zer_ele.append(neigh)
        print(indegree)
        for i in indegree :
            if i != 0 : return False
        return True
                
        # Perform BFS-based topological sort
        # visited_count = 0
        # while ind_zer_ele:
        #     ele = ind_zer_ele.popleft()
        #     visited_count += 1  # Count how many nodes we can visit
            
        #     if ele not in adj_mat:
        #         continue
        #     for neigh in adj_mat[ele]:
        #         indegree[neigh] -= 1
        #         if indegree[neigh] == 0:
        #             ind_zer_ele.append(neigh)
        
        # # If we visited all courses, return True; otherwise, there's a cycle
        # return visited_count == numCourses


