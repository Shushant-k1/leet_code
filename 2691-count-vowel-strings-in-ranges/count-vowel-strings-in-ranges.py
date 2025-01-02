class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pre = [0]
        
        vow = { "a" , "e" , "i" , "o" , "u" }
        for word in words :
            if word[0] in vow and word[-1] in vow :
                pre.append(pre[-1] + 1)
            else :
                pre.append(pre[-1])

        ans = [ ]

        for star , end  in queries :
            ans.append(pre[end  + 1] - pre[star ] )
        
        return ans