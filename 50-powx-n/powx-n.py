class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        p = (n)
        n = abs(n)
        while n > 0 :
            if n & 1 :
                ans = ans * x
            
            x = x * x

            n = n >> 1
        return ans if p > 0 else 1 / ans
