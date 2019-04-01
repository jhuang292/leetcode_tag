class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end-start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid 
        return nums[start]
