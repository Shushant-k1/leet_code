class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if len(stones) == 1 : return True
        if stones[1] != 1 : return False
        d = set(stones)
        end = stones[-1]


        @cache
        def helper( cur  , k  ) :

            if cur == end : return True
            if cur not in d : return False
            for i in (k - 1 , k + 1 , k) :
                if i > 0 :
                    if helper( cur + i, i , ) : 
                        return True
            return False
        
        return helper( 0 , 0 )


        
