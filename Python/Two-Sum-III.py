# # 01
# Hash table
# Time complexity : O(n) where n is length of nums.
# Space complexity : O(n)

# Accepted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_indices = {}
        
        for index, num in enumerate(nums):
            
            if target - num in num_indices:
                return num_indices[ target - num ], index
            
            num_indices[num] = index