class Solution:
    def helper(self ,  nums , k , idx , used  , dp ) :
        if used == 3 :
            return 0 , []
        if idx - (used * k) >  (len(nums)) :
            return 0 , []
        
        if (idx , used ) in dp :
            return dp[(idx , used)]
        
        take_cur_sum , take_cur_ind = self.helper(nums , k , idx + k , used +1 ,dp )
        take_cur_sum += sum(nums[idx:idx + k])

        skip_cur_sum , skip_cur_ind = self.helper(nums , k , idx + 1 , used , dp)

        if take_cur_sum >= skip_cur_sum :

            dp[(idx , used)] =  take_cur_sum , ([idx] + take_cur_ind)
            return dp[(idx , used)]

        dp[(idx , used)] =  skip_cur_sum , skip_cur_ind
        return dp[(idx , used)]

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = self.helper(nums , k , 0 , 0 , { }) 
        return ans[1]