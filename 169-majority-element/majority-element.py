class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        val = 1

        cur = nums[0]
        for i in range(1 , len(nums)) :
            if val == 0 :
                cur = nums[i]
                val = 1
            elif nums[i] == cur :
                val += 1
            
            else :
                val -= 1
        
        return cur