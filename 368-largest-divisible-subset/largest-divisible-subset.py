class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        # dp = [[0 for i in range()]]

        return self.helper(nums , 0 , -1 , {})
        
    

    def helper(self , nums ,idx , cur_idx , dp) :

        if idx == len(nums) :
            return []
        if (idx , cur_idx) in dp : return dp[(idx , cur_idx)]

        not_take = self.helper(nums , idx + 1 , cur_idx , dp) 
        take = []
        if cur_idx == -1 or nums[idx] % nums[cur_idx] == 0 :
            take = self.helper(nums , idx + 1 , idx , dp)  + [nums[idx]]
        
        dp[(idx , cur_idx)] = take if len(take) > len(not_take) else not_take

        return dp[(idx , cur_idx)]