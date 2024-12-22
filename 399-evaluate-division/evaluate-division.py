class Solution:
    
    def adj(self , equations, values):
        d = {}
        for node, val in zip(equations, values):
            st, en = node
            
            if st not in d:
                d[st] = []
            d[st].append((en, val))
            
            if en not in d:
                d[en] = []
            d[en].append((st, 1 / val))
        return d

    def bfs(self , start , end , adj_mat) :
        vis = set()
        # vis.add(start)
        dq = deque()
        dq.append([start, 1])
        while dq :
            ind , val = dq.popleft()
            if ind in vis :
                continue
            vis.add(ind)
            for neighbour , cur_val in adj_mat[ind] :
                if neighbour == end :
                    return round(val * cur_val , 6)
                else :
                    dq.append([neighbour , val * cur_val])
        return -1.00000

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_mat = self.adj(equations , values)
        ans = []
        for i , j in queries :
            if i in adj_mat and j in adj_mat :
                ans.append(self.bfs( i , j , adj_mat))
            else :
                ans.append(-1.00000)
        return ans
        
        