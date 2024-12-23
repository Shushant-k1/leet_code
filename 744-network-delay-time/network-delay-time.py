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
        
        _cost = [float(inf)] * n

        vis = set()
        dq = deque()
        dq.append([k,  0])
        _cost[k - 1]  = 0
        while dq :
            node ,  cost = dq.popleft()
            if node in vis :
                continue
            
            vis.add(node)
            if node in adj_mat :
                for neigh  , wei in adj_mat[node] :
                    if cost + wei <=  _cost[neigh - 1] :
                        _cost[neigh-1] = cost + wei
                        dq.append([neigh , cost + wei])
        print(_cost)
        return -1 if max(_cost) == float('inf') else max(_cost)
from collections import deque
from typing import List

class Solution:
    def adj(self, times):
        adj = {}
        for u, v, w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append([v, w])
        return adj

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = self.adj(times)
        
        # Initialize cost to reach each node
        _cost = [float('inf')] * n
        _cost[k - 1] = 0  # Distance to source is 0
        
        # BFS-like approach using a deque
        dq = deque([[k, 0]])  # (current node, current cost)
        
        while dq:
            node, cost = dq.popleft()
            
            if node in adj_mat:
                for neigh, wei in adj_mat[node]:
                    if cost + wei < _cost[neigh - 1]:  # Relaxation condition
                        _cost[neigh - 1] = cost + wei
                        dq.append([neigh, cost + wei])
        
        # If any node remains unreachable, return -1
        max_cost = max(_cost)
        return -1 if max_cost == float('inf') else max_cost
