class Solution:
    def xorAllNums(self, num1: List[int], num2: List[int]) -> int:
        n1 = len(num1)
        n2 = len(num2)
        if n1 % 2 == 0 and n2 % 2 == 0 :
            return 0
        ans = 0
        if n1 & 1 and n2 % 2 == 0: 
            for i in num2 :
                ans = ans ^ i
        elif n1 % 2 == 0 and n2 & 1 :
            for i in num1 :
                ans = ans ^ i
        
        else :
            for i in num1 :
                ans = ans ^ i
            
            for i in num2 :
                ans = ans ^ i
        
        return ans
