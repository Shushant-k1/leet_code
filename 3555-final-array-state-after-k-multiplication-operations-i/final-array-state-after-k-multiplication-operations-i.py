class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        mod = 10 ** 9 + 7
        if multiplier == 1 :
            return nums
        
        m = max(nums)
        n = len(nums)
        pq = [[nums[i] , i] for i in range(n)]
        heapify(pq)
        while k and pq[0][0] * multiplier <= m :
            ele ,ind = heappop(pq)
            heappush(pq , [ele * multiplier , ind])
            k -= 1
        
        pq.sort()
        q , k = divmod(k , n)
        for i in range(n) :
            pq[i][0] = pq[i][0] * pow(multiplier , q , mod) % mod
        for i in range(k) :
            pq[i][0] = pq[i][0] * multiplier % mod
        
        for i in pq :
            ele , ind  = i
            nums[ind] = ele
        return nums 