class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val//2, val%2
            res += str(val)
            
        if carry:
            res += str(1)
        return res[::-1]
