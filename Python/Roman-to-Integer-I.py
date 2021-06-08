# # 13
# Backward Iteration + Hashmap
# Time complexity : O(n) where n is the length of given string.
# Space complexity : O(1) 
# Accepted

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_int_map = {
            "I" :   1,
            "V" :   5,
            "X" :   10,
            "L" :   50,
            "C" :   100,
            "D" :   500,
            "M" :   1000
        }
        
        integer = 0
        
        previous_int = 0
        
        for roman in s[ :: - 1 ]:
            
            val = roman_int_map[roman]
            
            if previous_int <= val:
                integer += val
            else:
                integer -= val
            
            previous_int = val
            
        return integer