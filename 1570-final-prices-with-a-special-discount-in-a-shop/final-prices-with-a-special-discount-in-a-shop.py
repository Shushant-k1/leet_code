class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        next_small = [prices[-1]]
        n = len(prices)
        st = [prices[-1]]
        for i in range( n - 2 , -1 , -1 ) :
            while st and st[-1] > prices[i] :
                st.pop() 
            if st :
                next_small.append(prices[i] - st[-1])
            else :
                next_small.append(prices[i])
            st.append(prices[i])
        return next_small[::-1]