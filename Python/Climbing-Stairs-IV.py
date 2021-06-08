# # 70
# Bottom up Approach in constant space
# Time complexity : O(n) 
# Space complexity : O(1) 
# Accepted
# 
class Solution:
    def climbStairs(self, n: int) -> int:
        
        x = 0
        y = 1
        
        for i in range(1, n + 1):
            z = x + y
            x = y
            y = z
            
        return y