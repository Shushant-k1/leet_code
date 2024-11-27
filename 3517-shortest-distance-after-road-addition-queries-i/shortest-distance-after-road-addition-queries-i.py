
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        dist = [i for i in range(1 , n + 1)]
        for ini , next_ in queries :
            dist[ini] = max(next_ , dist[ini])
            print(dist)
            i = 0
            cnt = 0
            while i < n  :
                cnt += 1
                i += dist[i]
                if i == n - 1 :
                    break
            ans.append(cnt)
        return ans
class Solution:
    # Function to find the minimum distance from node 0 to node n-1
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0  # Base case: distance to destination (n-1) is 0

        # Iterate from the second last node down to the first node
        for current_node in range(n - 2, -1, -1):
            min_distance = n
            # Explore neighbors to find the minimum distance
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            # Store the calculated distance for the current node
            dp[current_node] = min_distance

        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]

        # Initialize edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        # Process each query to add new edges
        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)  # Add the directed edge from u to v

            # Calculate the minimum distance after adding the new edge
            answer.append(self.find_min_distance(adj_list, n))

        return answer