class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sub = max(nums)

        cur_sum = 0

        for i in nums :
            cur_sum += i
            max_sub = max(max_sub , cur_sum)

            if cur_sum < 0 :
                cur_sum = 0
        
        return max_sub
