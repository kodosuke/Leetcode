
# # 215
# Quick Select
# Time complexity : O(n**2) 
# Space complexity : O(1) 
# Accepted

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left  = 0
        right = len(nums) - 1
        
        while left <= right :
            
            pivotIndex = self.partition(nums, left, right)
            
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
        
        nums[ left ], nums[ right ] = nums[ right ], nums[ left ]