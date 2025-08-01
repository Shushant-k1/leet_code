import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        adj = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        min_cost = [float('inf')] * n
        ways = [0] * n
        min_cost[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (cost, node)

        while heap:
            cost, u = heapq.heappop(heap)

            if cost > min_cost[u]:
                continue

            for v, t in adj[u]:
                new_cost = cost + t

                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_cost, v))
                elif new_cost == min_cost[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n - 1]
