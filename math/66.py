class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        res = []
        for d in digits:
            s += str(d)
        s = int(s)
        s += 1
        s = str(s)
        for c in s:
            res.append(int(c))
        return res
