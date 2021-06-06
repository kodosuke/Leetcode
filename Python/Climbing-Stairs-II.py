# # 70
# Recursion + Memoization
# Time complexity : O(n) 
# Space complexity : O(n) for memo

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