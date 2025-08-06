class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        # dp = [[0 for i in range()]]

        return self.helper(nums , 0 , -1 , {})
        
    

    def helper(self , nums ,idx , cur_max , dp) :

        if idx == len(nums) :
            return []
        if (idx , cur_max) in dp : return dp[(idx , cur_max)]

        not_take = self.helper(nums , idx + 1 , cur_max , dp) 
        take = []
        if cur_max == -1 or nums[idx] % cur_max == 0 :
            take = self.helper(nums , idx + 1 , max(cur_max ,nums[idx] ) , dp)  + [nums[idx]]
        
        dp[(idx , cur_max)] = take if len(take) > len(not_take) else not_take

        return dp[(idx , cur_max)]