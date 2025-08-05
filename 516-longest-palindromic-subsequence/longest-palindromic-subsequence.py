class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:
        
        text2 = text1[::-1]        
        n1 , n2 = len(text1) , len(text2)
        dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
        for i in range(1 , n1 +1 ) :
            for j in range(1 , n2 + 1) :
                take = 0
                if text1[i-1] == text2[j-1] :
                    take = dp[i-1][j-1] + 1
                
                not_take = max(dp[i-1][j] , dp[i][j-1])
                dp[i][j] = max(take , not_take)
        return dp[n1][n2]