from collections import deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))

        q = deque()
        q.append((src, 0, 0))  # (node, cost, stops)
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        while q:
            node, cost, stops = q.popleft()

            if stops > k:
                continue

            for neighbor, price in adj[node]:
                if cost + price < min_cost[neighbor]:
                    min_cost[neighbor] = cost + price
                    q.append((neighbor, cost + price, stops + 1))

        return min_cost[dst] if min_cost[dst] != float('inf') else -1
