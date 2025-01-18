import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        n, m = len(grid), len(grid[0])

        pq = [(0, 0, 0)]  
        min_cost = [[float('inf')] * m for _ in range(n)] 
        min_cost[0][0] = 0

        while pq:
            cost, i, j = heapq.heappop(pq)

            if min_cost[i][j] != cost:
                continue
            
            for d, (dx, dy) in enumerate(directions):
                new_row, new_col = i + dx, j + dy

                if 0 <= new_row < n and 0 <= new_col < m:
                    new_cost = cost + (d != (grid[i][j] - 1))  #direction doesn't match
                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))

        return min_cost[n-1][m-1]
