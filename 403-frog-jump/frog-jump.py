class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if len(stones) == 1 : return True
        if stones[1] != 1 : return False
        d = set(stones)
        end = stones[-1]
        dp = {}
        return self.helper(d , 0 , 0, end ,dp)

    
    def helper(self , d , cur  , k  , end , dp) :

        if cur == end : return True
        if (cur , k) in dp : return dp[(cur , k )]

        if cur not in d :  return False

        for i in (k - 1 , k + 1 , k) :
            if i > 0 :
                if self.helper(d , cur + i, i , end  , dp) : 
                    dp[(cur , k)] = True
                    return True
        dp[(cur , k)] = False
        return dp[(cur , k)]

        
