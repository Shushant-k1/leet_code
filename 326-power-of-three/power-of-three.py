class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_pow = 1162261467 
        return n > 0 and max_pow % n == 0