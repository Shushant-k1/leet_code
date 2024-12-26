

class Solution:
    def helper(self, cur_ind, cur_sum, tar, nums,  dp):

        if cur_ind == len(nums):
            return 1 if cur_sum == tar else 0
        if (cur_ind, cur_sum) in dp :
            return dp[(cur_ind, cur_sum)]

        
        add = self.helper(cur_ind + 1, cur_sum + nums[cur_ind], tar, nums , dp)
        substract = self.helper(cur_ind + 1, cur_sum - nums[cur_ind], tar, nums , dp)
        
        dp[(cur_ind, cur_sum)] = add + substract
        
        return dp[(cur_ind, cur_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(0, 0, target, nums , {})
