# 78
# Time Complexity : O(n* (2 **n))
# Space Cmplexity : O(2 ** n)
# Cascading
# Difficulty level  : Medium

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        for num in nums:
            subsets += [ subset + [num] for subset in subsets]
            
        return subsets