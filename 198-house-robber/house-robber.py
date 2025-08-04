class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return self.helper(nums , 0 , {})
    


    def helper(self , nums  , cur  , dp) :

        if cur >= len(nums) : return 0
        if cur in dp  : return dp[cur]

        dp[cur] =  max(self.helper(nums , cur + 2 , dp) + nums[cur] , self.helper(nums , cur + 1 , dp))

        return dp[cur]