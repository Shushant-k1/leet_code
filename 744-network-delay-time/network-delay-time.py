class Solution:
    def adj(self , times) :
        ad = { }
        for i , j , cost in times :
            if i not  in ad :
                ad[i] = []
            ad[i].append([j , cost])
        return ad



    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = self.adj(times)
        if k not in adj_mat :
            return -1
        
        _cost = [float('inf')] * n
        dq = deque()
        dq.append([k,  0])
        _cost[k - 1]  = 0
        while dq :
            node ,  cost = dq.popleft()

            if node in adj_mat :
                for neigh  , wei in adj_mat[node] :
                    if cost + wei <  _cost[neigh - 1] :
                        _cost[neigh-1] = cost + wei
                        dq.append([neigh , cost + wei])

        return -1 if max(_cost) == float('inf') else max(_cost)

