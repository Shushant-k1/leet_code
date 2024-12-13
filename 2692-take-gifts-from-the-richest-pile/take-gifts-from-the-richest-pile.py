class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ans = 0
        nums = [-i for i in gifts]
        heapq.heapify(nums)
        for i in range(k) :
            x = -1 * heapq.heappop(nums)
            x = int(math.sqrt(x))
            heapq.heappush(nums , -1 * x)
        ans =  -1 * sum(nums)
        del  nums
        return ans