class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cnt = 1
        temp = a
        while len(a) < len(b):
            a += temp
            cnt += 1

        # Try current and 2 more repeats (handle edge overlaps)
        for i in range(3):
            if self.rabinkarp(a, b):
                return cnt
            a += temp
            cnt += 1

        return -1

    def rabinkarp(self, a, b):
        n, m = len(a), len(b)
        if n < m:
            return False

        base = 256
        mod = 10**9 + 7

        hash_b = 0
        for ch in b:
            hash_b = (hash_b * base + ord(ch)) % mod

        hash_a = 0
        for i in range(m):
            hash_a = (hash_a * base + ord(a[i])) % mod

        if hash_a == hash_b and a[0:m] == b:
            return True

        power = pow(base, m - 1, mod)
        for i in range(1, n - m + 1):
            hash_a = (hash_a - ord(a[i - 1]) * power) % mod
            hash_a = (hash_a * base + ord(a[i + m - 1])) % mod
            if hash_a == hash_b and a[i:i + m] == b:
                return True

        return False
