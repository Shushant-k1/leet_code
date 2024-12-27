class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        cur_max = values[0]
        cur_ind = 0
        for i in range(1 , len(values)) :
            ans = max(ans , cur_max + cur_ind + values[i] - i)
            if cur_max + cur_ind <= values[i] + i :
                cur_max = values[i]
                cur_ind = i
        return ans
            
