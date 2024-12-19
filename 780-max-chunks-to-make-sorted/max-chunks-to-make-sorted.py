class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        cur = 0
        pref = 0
        for i in range(len(arr)) :
            cur += arr[i]
            pref += i
            if cur == pref : ans += 1
        return ans