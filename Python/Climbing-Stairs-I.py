# # 70
# Recursion
# Time complexity : O(2^n) 
# Size of recursion tree will be 2^n
# Space complexity : O(n)

# Time Limit Exceeded

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)