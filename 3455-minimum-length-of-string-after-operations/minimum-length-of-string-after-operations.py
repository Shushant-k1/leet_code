class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26
        n = len(s)
        for char in s :
            freq[ord(char) - ord("a")] += 1
        
        
        ans = 0
        print(freq)
        for fre in freq :

            if fre & 1 : 
                ans += 1
            elif fre != 0:
                ans += 2

        return ans