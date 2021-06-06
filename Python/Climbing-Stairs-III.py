# # 70
# Recursion + Memoization
# Time complexity : O(n) 
# Space complexity : O(n) for memo

# Accepted
# 

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        x = 1
        y = 2
        
        for i in range(3, n + 1):
            
            z = x + y 
            x = y
            y = z
            
        return y