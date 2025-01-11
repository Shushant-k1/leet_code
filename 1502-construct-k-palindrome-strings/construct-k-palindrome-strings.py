class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k :
            return False
        
        if n == k :
            return True
        

        freq = [0] * 26

        for char in s :
            freq[ord(char) - ord("a")] += 1
        

        odd_cnt = 0
        for count in freq :

            if count & 1 :

                odd_cnt += 1
            
        return odd_cnt <= k