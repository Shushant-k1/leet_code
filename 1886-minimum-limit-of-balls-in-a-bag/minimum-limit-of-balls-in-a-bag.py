class Solution:
    def is_valid(self , nums , max_s, max_o) :
        cur = 0
        for i in nums :
            cur += math.ceil(i / max_s) - 1
            if cur > max_o :
                return False
        return True
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        while l < r :
            mid = (l + r ) // 2
            if self.is_valid(nums , mid , maxOperations) :
                r = mid 
            else :
                l = mid + 1
        return l