class Solution:
    def minimumLength(self, s: str) -> int:
        d = {}
        n = len(s)
        for char in s :
            if char in d :
                d[char] += 1
            else :
                d[char] = 1
        
        ans = 0

        for freq in d :

            if d[freq] & 1 : 
                ans += 1
            else :
                ans += 2

        return ans