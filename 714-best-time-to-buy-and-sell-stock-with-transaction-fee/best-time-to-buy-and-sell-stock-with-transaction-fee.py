class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        

        
        return self.helper(prices , 0 , 0 ,{} , fee)
    
    

    def helper(self , prices , cur_idx , buy  , dp , fee) :
        
        if cur_idx == len(prices)  :
            return 0
        
        if (cur_idx , buy ,) in dp :
            return dp[(cur_idx , buy )]
        
        take = 0
        not_take = 0
        if buy == 0 :
            take = self.helper(prices , cur_idx + 1, 1  , dp , fee ) + - prices[cur_idx] 
            not_take = self.helper(prices , cur_idx + 1 , 0  , dp  , fee)
            

        else :
            take = self.helper(prices , cur_idx + 1 , 0 , dp , fee) + prices[cur_idx] - fee
            not_take = self.helper(prices , cur_idx  + 1 , buy , dp  , fee)

        dp[(cur_idx , buy )] = max(take , not_take)

        return dp[(cur_idx , buy ,)]


