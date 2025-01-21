class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        import re
        cnt = 0
        pat = "^" + pref
        for i in (words) :
            if re.findall(pat , i) : 
                cnt += 1
        return cnt