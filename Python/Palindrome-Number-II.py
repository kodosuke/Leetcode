# # 09
# Typecasting
# Time complexity : O(n) where n is number of digits in x.
# Space complexity : O(1)

# Accepted

class Solution:
    def isPalindrome(self, x: int) -> bool: 
        
        return str(x) == str(x)[::-1]