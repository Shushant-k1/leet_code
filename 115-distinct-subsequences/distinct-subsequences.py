class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.helper(s , t , 0, 0 , {})

    def helper(self , s , t , cur_t,cur_s ,dp) :

        if cur_t == len(t)  :
            return 1

        if cur_s >= len(s)  or cur_t >= len(t):
            return 0

        if (cur_t , cur_s) in dp : return dp[(cur_t , cur_s)]
        pick = not_pick = 0
        if s[cur_s] == t[cur_t] :   
            pick = self.helper(s , t , cur_t + 1 , cur_s + 1 , dp) + self.helper(s , t ,cur_t , cur_s +1, dp)
        else :
            not_pick = self.helper(s , t , cur_t , cur_s + 1 , dp)

        dp[(cur_t , cur_s)] =  pick + not_pick
        return dp[(cur_t , cur_s)]