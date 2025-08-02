class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1  # Not enough cables to connect all computers
        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Merge components

        for u, v in connections:
            union(u, v)

        # Count unique roots
        components = sum(1 for i in range(n) if find(i) == i)

        # We need (components - 1) operations to connect them
        return components - 1
