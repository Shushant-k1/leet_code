class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])


        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        heap = [(0 , 0 , 0)]

        effort = [[float('inf') for _ in range(m)] for i in range(n)]
        effort[0][0] = 0

        while heap :
            cur_effort , x , y = heapq.heappop(heap)
            if x == n -1 and y == m - 1 :
                return cur_effort
            
            for dx , dy in dirs :
                nx , ny = dx + x , dy + y
                if (0 <= nx < n ) and (0 <= ny < m) :
                    net_effort = max(cur_effort , abs(grid[x ][y] - grid[nx][ny]))
                    if effort[nx][ny] > net_effort :
                        effort[nx][ny] = net_effort
                        heapq.heappush(heap,(net_effort , nx , ny))

        return -1
