import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] indexes = new int[2];
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++) {
            
            int potentialTarget = target - nums[i];
            if(map.containsKey(potentialTarget))  {
                
                indexes[0] = (int)map.get(potentialTarget);
                indexes[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return indexes;
    }
}