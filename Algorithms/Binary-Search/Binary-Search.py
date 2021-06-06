'''
    Given.
    An Array of integers in a sorted order, nums.

    Problem Statement.
    Find the target integer, val in nums.
    If val does not found, return -1.
'''

# Approach.

def binary_search(nums :list[int], val :int):

    n = len(nums)

    left  = 0
    right = n - 1

    while left <= right :

        midpoint = left + ( right - left ) // 2

        if nums[ midpoint ] == val:
            return midpoint
        else:

            if nums[ midpoint ] < val:
                left  = midpoint + 1
            else:
                right = midpoint - 1

    return -1
    
