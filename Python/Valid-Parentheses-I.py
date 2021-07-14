# # 20

# Time complexity : O(n) where n is the length of s.
# Space complexity : O(n) 
# Accepted


class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        
        stack = []
        
        for bracket in s:
            
            if bracket in pairs:
                stack.append(bracket)
            else:
                if stack:
                    if bracket != pairs[stack.pop()]:
                        return False
                else:
                    return False
                
        return len(stack) == 0
