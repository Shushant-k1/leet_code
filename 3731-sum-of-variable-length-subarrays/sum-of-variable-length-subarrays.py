class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans= 0
        for i in range(len(nums)) :
            st =  max(0 ,i -  nums[i])
        
            ans += sum(nums[st:i+1])
        return ans