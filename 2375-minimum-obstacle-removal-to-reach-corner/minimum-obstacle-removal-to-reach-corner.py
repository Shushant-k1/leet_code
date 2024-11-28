class Solution:
    dir = [( 0, 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def _is_valid(row , col) :
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        m , n = len(grid) , len(grid[0])
        
        min_obs = [[float('inf')] * n  for _ in range(m)]

        min_obs[0][0] = grid[0][0]

        pq = [(min_obs[0][0] , 0 , 0)]
        while pq :
            obs , row , col = heapq.heappop(pq)
            if row == m - 1 and col == n - 1 :
                return obs

            for dr , dc in self.dir :
                new_row , new_col = row + dr , col + dc
                if _is_valid(new_row , new_col) :
                    new_obs = obs + grid[new_row][new_col]
                    if new_obs < min_obs[new_row][new_col] :
                        min_obs[new_row][new_col] = new_obs
                        heapq.heappush(pq , (new_obs , new_row , new_col))
        return min_obs[m-1][n-1]