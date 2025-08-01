class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj = [[]  for i in range(n)]

        for u , v , cost in edges :
            adj[u].append((v , cost))
            adj[v].append((u , cost))
        print(adj)
        

        cities = [0] * n

        maxi = float('inf')
        ans = 0
        for i in range(n) :
            cities[i] = self.dijisktra(adj , i , distanceThreshold , n)
            if cities[i] <= maxi :
                ans = i
                maxi = cities[i]
        return ans
            
        
    def dijisktra(self , adj , src , threshold , n) :
                        

        heap = [ (0 , src)]

        min_cost = [float('inf')] * n
        min_cost[src] = 0
        while heap :
            cost , node = heapq.heappop(heap)
            if cost > threshold : continue
            for neigh , temp_cost in adj[node] :
                total_cost = cost + temp_cost
                if total_cost <= threshold and  min_cost[neigh] > total_cost:
                    heapq.heappush(heap , (total_cost , neigh))
                    min_cost[neigh] = total_cost
                
        return sum(1 for d in min_cost if d <= threshold and d != 0)




        