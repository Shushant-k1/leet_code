# class Solution:
#     import bisect
#     def countFairPairs(self, arr: List[int], lower: int, upper: int) -> int:
#         arr.sort()
#         n = len(arr)
#         ans = 0
#         for i in range(n) :
#             if arr[i] > upper :
#                 break
#             mini = lower - arr[i]
#             left = bisect.bisect_left(arr , mini)
#             right = bisect.bisect_left(arr , upper - arr[i])
#             if left >= i :
#                 ans += right - left
#             else :
#                 ans += right - i
#         return ans

class Solution:
    def lower_bound(self, nums, low, high, element):
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # Assume we have picked nums[i] as the first pair element.

            # `low` indicates the number of possible pairs with sum < lower.
            low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])

            # `high` indicates the number of possible pairs with sum <= upper.
            high = self.lower_bound(
                nums, i + 1, len(nums) - 1, upper - nums[i] + 1
            )

            # Their difference gives the number of elements with sum in the
            # given range.
            ans += high - low

        return ans