# # 01
# Pop and Push Digits & Check before Overflow
# Time complexity : O(n) where n is number of digits in x.
# Space complexity : O(1)

# Accepted

class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1
        
        if x < 0 :
            sign = - 1
            
        x = abs(x)
        
        reversed_integer = 0
        
        if x < pow(2, 31):
            
            while x:
                
                reversed_integer = ( reversed_integer * 10 ) + x % 10
                
                if reversed_integer > pow(2, 31):
                    return 0
                
                x = x // 10
                
            return reversed_integer * sign
        
        else:
            return 0
                