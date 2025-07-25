class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""

        mini = float('inf')

        for str in strs :
            mini = min(mini , len(str))

        for i in range(mini) :
            for j in range(len(strs)) :
                if strs[j][i] != strs[0][i] :
                    return ans


            ans += strs[0][i]

        return ans