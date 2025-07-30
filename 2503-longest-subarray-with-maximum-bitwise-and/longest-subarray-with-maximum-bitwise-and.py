class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_ele = max(nums)
        i = j = 0
        cur_and = 0
        ans = 0
        while i < len(nums) :
            if nums[i] == max_ele :
                j = i
                while i < len(nums) and nums[i] == max_ele :
                    i += 1
                    ans = max(ans , i - j )
            else :
                i += 1
        return ans
