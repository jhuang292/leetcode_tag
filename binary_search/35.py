ass Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            if len(nums) == 0:
	                return 0
			        if target < nums[0]:
				            return 0
					            if target > nums[-1]:
						                return len(nums)
								        
									        start, end = 0, len(nums) - 1
										        while start <= end:
											            mid = (start + end) // 2
												                if nums[mid] == target:
														                return mid
																            elif nums[mid] < target:
																	                    start = mid + 1
																			                else:
																					                end = mid - 1
																							        return start
