class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = l + (r-l) // 2
            total = 0
            for row in matrix:
                for item in row:
                    if item <= m:
                        total += 1
            if total >= k:
                r = m
            else:
                l = m + 1
        return l
