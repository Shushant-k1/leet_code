import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))

        # (total_cost, node, stops)
        heap = [(0, src, 0)]
        
        # cost[node][stops] = minimum cost to reach `node` with `stops`
        cost_matrix = [ [float('inf')] * (k + 2) for _ in range(n) ]
        cost_matrix[src][0] = 0

        while heap:
            total_cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return total_cost

            if stops > k:
                continue

            for neighbor, price in adj[node]:
                next_cost = total_cost + price
                if next_cost < cost_matrix[neighbor][stops + 1]:
                    cost_matrix[neighbor][stops + 1] = next_cost
                    heapq.heappush(heap, (next_cost, neighbor, stops + 1))

        return -1
