class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = { }
        for i , j  in enumerate(words1) :
            x = {}
            for k in j :
                if k not in x :
                    x[k] = 1
                else :
                    x[k] += 1
            d[i] = x

        required = {}
        for word in words2:
            temp_freq = {}
            for char in word:
                temp_freq[char] = temp_freq.get(char, 0) + 1
            for char, count in temp_freq.items():
                required[char] = max(required.get(char, 0), count)

        ans = []

        for k in range(len(words1)) :
            p = d[k]
            bool = True

            for i in required :
                if i not in p or p[i] < required[i] :
                    bool = False
                    break
            
            if bool:
                ans.append(words1[k])
        
        return ans

            