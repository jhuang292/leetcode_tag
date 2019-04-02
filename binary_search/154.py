class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def findMin(nums, l, r):
            if l+1 >= r: return min(nums[l],nums[r])
            
            if nums[l] < nums[r]: return nums[l]
            
            mid = l + (r-l) // 2
            return min(findMin(nums, l, mid-1), findMin(nums, mid, r))
        
        return findMin(nums, 0, len(nums)-1)
