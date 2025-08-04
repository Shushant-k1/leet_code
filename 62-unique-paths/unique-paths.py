class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return self.helper(m , n , {})

    

    def helper(self , m , n , dp) :

        if m == 1 and n == 1 : return 1

        if m  <= 0  or n <= 0 : return 0
        if (m , n ) in dp : return dp[(m ,n)]

        dp[(m , n)] =  self.helper(m  , n - 1 , dp) + self.helper(m - 1 , n , dp)

        return dp[(m , n)]