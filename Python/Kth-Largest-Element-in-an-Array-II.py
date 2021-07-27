# # 215
# Quick Select with randomized Partition
# Time complexity : O(n) 
# Space complexity : O(1) 
# Accepted


import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left  = 0
        right = len(nums) - 1
        
        while left <= right :
            
            pivotIndex = self.randomPartition(nums, left, right)
            
            if pivotIndex == len(nums) - k:
                return nums[ pivotIndex ]
            else:
                
                if pivotIndex <= len(nums) - k:
                    left  = pivotIndex + 1
                else:
                    right = pivotIndex - 1
                    
        return
    
    def partition( self, nums: List[int], left : int, right : int) -> int:
        
        i = left
        pivot = nums[ right ]
        
        for j in range(left, right ):
            
            if nums[j] <= pivot:
                self.swap(nums, i, j)
                i += 1
                
        self.swap(nums, i, right)
        return i
    
    def swap( self, nums: List[int], left : int, right : int ) -> None:
        
        nums[left], nums[right] = nums[right], nums[left]
        
    def randomPartition( self, nums: List[int], left : int, right : int ) -> int:
        
        randIndex = random.randint(left, right)
        self.swap(nums, randIndex, right)
        
        return self.partition( nums, left, right )
        
                