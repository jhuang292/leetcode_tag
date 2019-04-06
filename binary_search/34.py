class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        # find target index l 
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        
        if nums[l] != target:
            return [-1,-1]
        
        index1, index2 = l, l
        while index1 >= 0 and nums[index1] == target:
            index1 -= 1
        while index2 <= len(nums)-1 and nums[index2] == target:
            index2 += 1
        return [index1+1, index2-1]
