from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False  # Cannot partition an odd sum

        target = total // 2
        n = len(nums)
        dp = [[ False for i in range(target + 1)] for j in range(n)]
        for i in range(n) :
            dp[i][0] = True
        for i in range(n) :
            for j in range(1 , target + 1) :
                take = False
                if j - nums[i] >= 0 :
                    take = dp[i - 1][j - nums[i]]

                not_take = dp[i - 1][j]
                if take or not_take :
                    dp[i][j] = True
        
        return dp[n-1][target]



    def helper(self, nums, idx, target, current_sum, memo):
        if current_sum == target:
            return True
        if current_sum > target or idx >= len(nums):
            return False

        if (idx, current_sum) in memo:
            return memo[(idx, current_sum)]

        # Two choices: take or don't take the current number
        take = self.helper(nums, idx + 1, target, current_sum + nums[idx], memo)
        not_take = self.helper(nums, idx + 1, target, current_sum, memo)

        memo[(idx, current_sum)] = take or not_take
        return memo[(idx, current_sum)]
