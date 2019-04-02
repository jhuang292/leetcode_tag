class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
        int l = 0;
        int r = nums.size()-1;
        while (l < r) 
        {
            int mid1 = l + (r-l)/2;
            int mid2 = mid1 + 1;
            
            if (nums[mid1] < nums[mid2])
                l = mid2;
            else
                r = mid1;
        }
        return l;
    }
};
