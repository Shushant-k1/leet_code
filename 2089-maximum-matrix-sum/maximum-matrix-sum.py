class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cnt = 0
        min_ele = 100000
        ans = 0
        zer = False
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j] == 0 :
                    zer = True
                if matrix[i][j] <  0:
                    cnt += 1
                min_ele = min(min_ele , abs(matrix[i][j]))
                ans += abs(matrix[i][j])

        if cnt & 1 and not zer :
            ans -= 2 * min_ele
        
        return ans