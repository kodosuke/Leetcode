# Binary Search

**Problem Statement**

Search for an element `val` in a __sorted__ array of integers, `nums` of length `n`.

**Return**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Index of `val` in `nums`.

If `val` not found in `nums`, return `-1`.

**Implementation in Python**

```python

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
