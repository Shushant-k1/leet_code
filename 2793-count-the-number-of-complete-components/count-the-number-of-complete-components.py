class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = [[]  for i in range(n)]

        componet_freq = defaultdict(int)

        for vertex in range(n) :
            adj[vertex] = [vertex]
        

        for v1 , v2 in edges :
            adj[v1].append(v2)
            adj[v2].append(v1)
        

        for vertex in range(n) :
            neigh = tuple(sorted(adj[vertex]))
            componet_freq[neigh] += 1
        
        return sum(1 for neigh , freq in componet_freq.items() if len(neigh) == freq)