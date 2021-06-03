# # 09
# Pop and Push Digits
# Time complexity : O(n) where n is number of digits in x.
# Space complexity : O(1)

# Accepted

class Solution:
    def isPalindrome(self, x: int) -> bool: 
        
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_number = 0 
        
        while x > reversed_number:        
            
            reversed_number = reversed_number * 10 + ( x % 10) 
            x //= 10  
            
        return x == reversed_number or x == reversed_number // 10
             
            
            