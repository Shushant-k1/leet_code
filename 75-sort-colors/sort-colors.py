class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j , k = 0 , 0 , len(nums) - 1

        while j <= k :
            if nums[j] == 1 :
                j += 1

            
            elif nums[j] == 2 :
                nums[j] , nums[k] = nums[k] , nums[j]
                k -= 1
            
            else :
                nums[i] , nums[j] = nums[j] , nums[i]
                j += 1
                i += 1
        
        