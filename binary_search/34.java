class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = {-1,-1};
        if (nums.length == 0) {
            return res;
        }
        
        int l = 0;
        int r = nums.length-1;
        while (l < r) {
            int m = l + (r-l)/2;
            if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        if (nums[l] != target) {
            return res;
        }
        
        int index1 = l;
        int index2 = l;
        while (index1 >= 0 && nums[index1] == target) {
            index1--;
        }
        while (index2 <= nums.length-1 && nums[index2] == target) {
            index2++;
        }
        res[0] = index1 + 1;
        res[1] = index2 -1;
        return res;
    }
}
