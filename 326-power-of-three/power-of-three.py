class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_pow = 1162261467  # 3^19, max power of 3 in 32-bit integer
        return n > 0 and max_pow % n == 0