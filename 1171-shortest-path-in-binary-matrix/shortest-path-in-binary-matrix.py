from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1),
                      (-1, -1), (1, 1), (-1, 1), (1, -1)]

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        q = deque([(0, 0)])
        path_length = 1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        if nx == n - 1 and ny == n - 1:
                            return path_length + 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
            path_length += 1

        return -1
