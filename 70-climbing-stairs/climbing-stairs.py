class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n , {})
        
 

        
    def helper(self , n , dp) :
        if n == 0 : return 1
        if n < 0 : return 0
        if n in dp : return dp[n]

        dp[n] =  self.helper(n - 1 , dp) + self.helper(n -2 , dp)
        return dp[n]