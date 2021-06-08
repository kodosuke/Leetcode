# # 58
# Backward Iteration
# Time complexity : O(n) where n is the length of given string in worst case.
# Space complexity : O(1) 
# Accepted

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        
        for char in s[:: -1 ]:
            
            if char != ' ':
                length += 1
                
            else:
                if length != 0:
                    return length
                
        return length