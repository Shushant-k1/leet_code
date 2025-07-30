from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rotten = deque()
        fresh_count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        time = 0
        
        while rotten and fresh_count:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # mark as rotten
                        rotten.append((nx, ny))
                        fresh_count -= 1
            time += 1
        
        return -1 if fresh_count > 0 else time
