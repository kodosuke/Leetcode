# # 01
# Brute force
# Time complexity : O(n**2) where n is length of nums.
# Space complexity : O(1)

# Accepted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):
            for j in range( i + 1, n):

                if nums[i] + nums[j] == target:
                    return i, j

#     n - 1 + n - 2 +  ... + 1
#     n - 1 + n - 2 +  ... + n - n + 1   + 0
#     n - 1 + n - 2 +  ... + n - (n - 1) + n - n
#     n * n + ( - 1 - 2 - .. - n )  
#     n * n - ( 1 + 2 + ... + n) 
#     n * n  - ( n (n + 1) / 2)
#     n ( 2n - n - 1 ) / 2
#     n ( n - 1) / 2