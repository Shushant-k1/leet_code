class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 : return nums[0]
        if n == 2 : return max(nums)
        
        return max(self.rob1(nums[ :-1]) , self.rob1(nums[1:]))
        

    
    def rob1(self , nums) :
        n = len(nums)
        if n == 1 : return nums[0]


        a,  b  = nums[0] , max(nums[0] , nums[1])

        for i in range(2 , n)  :
            a , b = b , max(a + nums[i] , b)
        
        return b