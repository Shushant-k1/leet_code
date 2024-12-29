class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(1 ,len(grid)) :
            for j in range( len(grid[0])) :
                if grid[i-1][j] >= grid[i][j] :
                    ans += grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] = grid[i-1][j] + 1

        return ans
