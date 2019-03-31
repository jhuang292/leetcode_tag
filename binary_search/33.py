class Solution:
    def search(self, nums: List[int], target: int) -> int:
            if len(nums) == 0:
	                return -1
			        
				        start, end = 0, len(nums)-1
					        while start <= end:
						            mid = (start + end) // 2
							                if nums[mid] == target:
									                return mid
											            elif nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
												                    end = mid - 1
														                else:
																                start = mid + 1
																		        return -1
