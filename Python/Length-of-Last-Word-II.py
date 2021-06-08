# # 58
# Python in-built functions
# Time complexity : O(n) where n is the length of given string in worst case.
# Space complexity : O(n) 
# Accepted

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])