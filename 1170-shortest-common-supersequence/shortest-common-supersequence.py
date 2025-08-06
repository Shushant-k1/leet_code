class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
    
        n , m = len(text1) , len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = n, m
        lcs = []

        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcs.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        common = ''.join(reversed(lcs))
        k = 0
        ans = ""
        j = 0
        pre = ""
        i = 0
        while j < m and k < len(common) and i < n:

            while i < n and text1[i] != common[k]  :
                ans += text1[i]
                i += 1
            
            while j < m  and text2[j] != common[k] :
                ans += text2[j]
                j += 1
            
            ans += common[k]
            i += 1
            k += 1
            j += 1
        
        return ans + text1[i:] + text2[j:]




