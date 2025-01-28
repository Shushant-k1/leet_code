class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)) :
            ind = abs(nums[i])
            if nums[ind - 1] < 0 : 
                return abs(nums[i])
            else :
                nums[ind - 1] = -1 * nums[ind - 1]