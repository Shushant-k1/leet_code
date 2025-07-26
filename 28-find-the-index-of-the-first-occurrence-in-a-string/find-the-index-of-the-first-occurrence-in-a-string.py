class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        base = 256
        mod = 10 ** 9 + 7

        n , m = len(haystack) , len(needle)

        if n < m : return -1

        hash = 0

        for chr in needle :
            hash = (hash * base  + ord(chr) ) % mod

        
        temp = 0

        for i in range(m) :
            temp = (temp * base + ord(haystack[i] )) % mod
        
        if temp == hash and haystack[0 : m] == needle :
            return 0
        
        power = pow(base , m -1  , mod)
        for i in range(1 , n- m + 1) :
            temp = (temp - ord(haystack[i - 1]) * power ) % mod
            temp = (temp * base + ord(haystack[i + m - 1])) % mod
            if temp == hash and needle == haystack[i : i + m] : return i
        return -1
