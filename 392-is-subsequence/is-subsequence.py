class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r, l = 0, 0 
        res = []
        while l < len(s) and r<len(t):
            if s[l] == t[r]:
                res.append(s[l])
                l += 1
            r += 1
        res_str = "".join(res)
        if res_str == s:
            return True
        return False
        
            