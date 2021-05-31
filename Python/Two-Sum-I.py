# # 01
# Brute force
# Time complexity : O(n**2) where n is length of nums.
# Space complexity : O(1)

# Time Limit Exceeded

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i, j