class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indrgerr = [0] * n
        for i in edges :
            indrgerr[i[1]] += 1
        cnt = 0
        ans = 0
        for i in range(n) :
            if indrgerr[i] == 0 :
                cnt += 1
                ans = i
        if cnt > 1 :
            return -1
        return ans