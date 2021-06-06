# Binary Search

**Problem Statement**

Search for an element `val` in the array of integers, `nums` of length `n`.

<p style='color:blue'> Return

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Index of `val` in `nums`.

<p style='color:green'> Implementation in Python</p>



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
