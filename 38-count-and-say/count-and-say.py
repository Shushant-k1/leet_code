class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for j in range(1 , n) :
            tem = ""
            cnt = 1
            for i in range(1 ,len(ans)) :
                if ans[i] != ans[i-1] :
                    tem += str(cnt)
                    tem += str(ans[i-1])
                    cnt = 1
                else :
                    cnt += 1
            tem += str(cnt)
            tem += str(ans[-1])
            ans =  tem
        return ans

