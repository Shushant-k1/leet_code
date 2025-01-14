class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        n = len(A)
        cnt = 0
        ans = []
        for i in range(n) :
            if A[i] == B[i] :
                cnt += 1
            else :
                if A[i] in d2 and B[i] in d1 :
                    cnt += 2
                elif A[i] in d2 or B[i] in d1 :
                    d1[A[i]] = 1
                    d2[B[i]] = 1
                    cnt += 1
                else :
                    d1[A[i]] = 1
                    d2[B[i]] = 1
            ans.append(cnt)
        
        return ans