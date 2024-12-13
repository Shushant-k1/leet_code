class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        z = [[nums[i] , i] for i in range(len(nums))]
        z.sort()
        check = [True] * len(nums)
        for i in range(len(nums)) :
            val , ind = z[i]
            if check[ind]  :
                check[ind] = False
                ans += val
                if ind + 1 < len(nums) :
                    check[ind + 1] = False
                if ind - 1 >= 0 :
                    check[ind - 1] = False
        return ans