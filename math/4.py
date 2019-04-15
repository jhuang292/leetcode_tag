class Solution:
        def longestPalindrome(self, s: str) -> str:
                    
                    def expand(s, l, r):
                                    while l >= 0 and r < len(s) and s[l] == s[r]:
                                                        l -= 1
                                                                        r += 1
                                                                                    return r - l - 1
                                                                                        
                                                                                        if s == None or len(s) < 1:
                                                                                                        return ""
                                                                                                            
                                                                                                            start, end = 0, 0
                                                                                                                    for i in range(len(s)):
                                                                                                                                    l1 = expand(s, i, i)
                                                                                                                                                l2 = expand(s, i, i+1)
                                                                                                                                                            maxLen = max(l1, l2)
                                                                                                                                                                        if maxLen > (end - start + 1):
                                                                                                                                                                                            start = i - (maxLen-1) // 2
                                                                                                                                                                                                            end = i + maxLen // 2
                                                                                                                                                                                                                    if end == len(s)-1:
                                                                                                                                                                                                                                    return "".join(s[start:])
                                                                                                                                                                                                                                        return "".join(s[start:end+1])
                                                                                                                                                                                                                                                
