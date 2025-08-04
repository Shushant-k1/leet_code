class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 :
            return 0
        n , m = len(grid) , len(grid[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1

        for i in range(1 , n) :
            if grid[i][0] == 0 :
                dp[i][0] = dp[i-1][0]
            else :
                dp[i][0] = 0

        for i in range(1 ,m) :
            if grid[0][i] == 0 :
                dp[0][i] = dp[0][i-1]
            else :
                dp[0][i] = 0

        for i in range(1 , n) :
            for j in range(1 , m) :
                if grid[i][j] == 0 :
                    dp[i][j] = dp[i-1][j] + dp[i][j -1 ]

        return dp[n-1][m-1]