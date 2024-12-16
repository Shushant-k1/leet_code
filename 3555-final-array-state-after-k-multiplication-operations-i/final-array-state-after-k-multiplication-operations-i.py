class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        _heap = [(nums[i] , i)for i in range(len(nums))]
        heapq.heapify(_heap)

        for i in range(k) :
            ele  , ind = heapq.heappop(_heap)
            heapq.heappush(_heap , (ele * multiplier , ind))
        

        for i in _heap :
            ele , ind = i
            nums[ind] = ele
        return nums
