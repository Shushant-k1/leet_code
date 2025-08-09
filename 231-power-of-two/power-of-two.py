class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            if n == (1 << i):
                return True
        return False