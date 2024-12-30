class Solution:
    def helper(self , low , high , zer , one , dp , cur) :
        MOD = 10**9 + 7
        # Base case: if current length exceeds high, stop recursion
        if cur > high:
            return 0
        # Check if current length is a valid string length
        if cur in dp:
            return dp[cur]
        count = 0
        if cur >= low:
            count += 1
       
        
        count += self.helper(low , high , zer , one , dp , cur + one)
        count += self.helper(low, high , zer , one , dp , cur +  zer )

        dp[cur] = count
        return dp[cur] % MOD

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return self.helper(low , high , zero , one , {} , 0)