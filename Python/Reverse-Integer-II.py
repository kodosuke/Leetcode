# # 07
# Slicing + Typecasting
# Time complexity : O(n) where n is number of digits in x.
# Space complexity : O(n)

# Accepted

class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1
        
        if x < 0 :
            sign = - 1
            
        x = abs(x)
        
        reversed_integer = 0
        
        if x < pow(2, 31):
            
            reversed_integer = int(str(x)[:: -1])
                
            if reversed_integer >= pow(2, 31):
                return 0
                
            else:    
                return reversed_integer * sign

        else:
            return 0
  
