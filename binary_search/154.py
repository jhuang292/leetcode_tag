class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end-start) // 2
            if nums[mid] < nums[end]:
                end = mid 
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end -= 1
        return nums[start]
