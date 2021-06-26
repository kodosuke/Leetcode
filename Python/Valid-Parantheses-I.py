# # 20
# Time Complexity O(n) where n is number of characters in s.
# Space Complexity O(n) for stack

# Accepted

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        parantheses = { '(':')', '[':']', '{':'}'}
        
        for char in s:
            if char in { '[', '(', '{' } :
                stack.append(char)
            else:
                if len(stack) != 0:
                    if char != parantheses[stack.pop()]:
                        return False
                else:
                    return False
                    
        
        return len(stack) == 0