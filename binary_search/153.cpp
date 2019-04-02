class Solution {
public:
    int findMin(vector<int>& nums) {
        return findMin(nums, 0, nums.size()-1);        
    }
private:
    int findMin(const vector<int>& nums, int l, int r)
    {
        // only 1 or 2 elements
        if (l+1 >= r) return min(nums[l], nums[r]);
        
        // sorted
        if (nums[l] < nums[r]) return nums[l];
        
        int mid = l + (r - l) /2;
        return min(findMin(nums, l, mid-1), findMin(nums, mid, r));
    }

};
