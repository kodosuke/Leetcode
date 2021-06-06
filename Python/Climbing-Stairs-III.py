# # 70
# Fibonacci Number with itertive Approach.
# Time complexity : O(n) 
# Space complexity : O(1) 
# Accepted
# 

class Solution:
    
    memo = {}
    def climbStairs(self, n: int) -> int:
        
        if n not in self.memo:
            
            if n < 3:
                self.memo[n] = n
                
            else:
                self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                  
        return self.memo[n]