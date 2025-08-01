from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        adj = self.adj_mat(n, roads)
        min_cost = self.dijkstra(adj, n)

        ways = [0] * n
        ways[0] = 1

        heap = [(min_cost[0], 0)]  # (cost, node)

        while heap:
            cost, node = heapq.heappop(heap)

            for neigh, edge_cost in adj[node]:
                if min_cost[node] + edge_cost == min_cost[neigh]:
                    if ways[neigh] == 0:  # push only first time
                        heapq.heappush(heap, (min_cost[neigh], neigh))
                    ways[neigh] = (ways[neigh] + ways[node]) % mod

        return ways[n - 1]

    def dijkstra(self, adj, n):
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        heap = [(0, 0)]

        while heap:
            cost, node = heapq.heappop(heap)
            if cost > min_cost[node]:
                continue
            for neigh, c in adj[node]:
                new_cost = cost + c
                if new_cost < min_cost[neigh]:
                    min_cost[neigh] = new_cost
                    heapq.heappush(heap, (new_cost, neigh))

        return min_cost

    def adj_mat(self, n, roads):
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        return adj
