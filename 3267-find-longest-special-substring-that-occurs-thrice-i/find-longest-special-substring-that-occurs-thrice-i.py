def constructLps(pat, lps):
    len_ = 0
    m = len(pat)
    lps[0] = 0

    i = 1
    while i < m:
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        
        else:
            if len_ != 0:

                len_ = lps[len_ - 1]
            else:
                
                lps[i] = 0
                i += 1

def search(pat, txt):
    n = len(txt)
    m = len(pat)

    lps = [0] * m
    res = []

    constructLps(pat, lps)

    i = 0
    j = 0

    while i < n:
        
        if txt[i] == pat[j]:
            i += 1
            j += 1

            if j == m:
                res.append(i - j)

                j = lps[j - 1]
        
        else:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return len(res) 

class Solution:
    def maximumLength(self, s: str) -> int:
        good = set(s)
        i = 0
        n = len(s)
        good = set()

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            for length in range(1, j - i + 1):
                good.add(s[i:i + length])
            i = j
        ans = -1
        print(good)
        for i in good :
            temp = search(i , s)

            if (temp) > 2 :
                ans = max(ans , len(i))
        return ans