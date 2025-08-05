class Solution:
    def minInsertions(self, text1: str) -> int:
        
        m = len(text1)
        text2 = text1[::-1]

        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

    
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        

        return m - dp[m][m] 