class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        ans = 0
        d = {}
        cur_sum = 0
        n = len(arr)
        for i in range(k) :
            if arr[i] not in d :
                d[arr[i]] = 1
            else :
                d[arr[i]] += 1
            cur_sum += arr[i]
        if len(d) == k :
            ans = cur_sum
        for i in range(k , n) :
            cur_sum = cur_sum - arr[i - k] + arr[i]
            d[arr[i - k]] -= 1
            if arr[i] not in d :
                d[arr[i]] = 1
            else :
                d[arr[i]] += 1
            if d[arr[i - k]] == 0 :
                del d[arr[i - k]]
            if len(d) == k :
                ans = max(ans , cur_sum)
        return ans
