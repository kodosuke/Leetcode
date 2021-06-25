# # 14
# Horizontal scanning
# Time complexity : O(mn) where m and n is the number of strings in given list and number of characters in the first string.
# Space complexity : O(1) 
# Accepted

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        end = len(strs[0])
        
        for i in range(1, len(strs)):
            
            while strs[0][:end] != strs[i][:end] :
                
                end -= 1
                if end == -1:   
                    return ''
                
        return strs[0][:end]
        