class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        component = 2
        count = {}

        # Label all components directly in the grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    count[component] = self.dfs(i, j, grid, component)
                    component += 1

        ans = max(count.values(), default=0)  # case when grid is all 1's or 0's

        # Try flipping every 0 to 1 and check connected components
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    temp = 1 + sum(count[k] for k in seen)
                    ans = max(ans, temp)

        return ans

    def dfs(self, i, j, grid, component):
        grid[i][j] = component
        cnt = 1
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj] == 1:
                cnt += self.dfs(ni, nj, grid, component)
        return cnt
