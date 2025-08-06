class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        return self.helper(prices , 0 , 0 ,0 ,{})
    
    

    def helper(self , prices , cur_idx , buy , cnt , dp) :

        if cur_idx >= len(prices)  :
            return 0
        
        if (cur_idx , buy , cnt) in dp :
            return dp[(cur_idx , buy , cnt)]
        
        take = 0
        not_take = 0
        if buy == 0 :
            take = self.helper(prices , cur_idx + 1, 1 , cnt , dp ) + - prices[cur_idx]
            not_take = self.helper(prices , cur_idx + 1 , 0 , cnt , dp )
            dp[(cur_idx , buy , cnt)] = max(take , not_take)

        else :
            take = self.helper(prices , cur_idx + 2 , 0 , cnt + 1 , dp) + prices[cur_idx] 
            not_take = self.helper(prices , cur_idx  + 1 , buy , cnt , dp )
            dp[(cur_idx , buy , cnt)] = max(take , not_take)

        dp[(cur_idx , buy , cnt)] = max(take , not_take)

        return dp[(cur_idx , buy , cnt)]


