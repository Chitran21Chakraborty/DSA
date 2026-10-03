class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        d = set()
        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            w = r-l+1
            res = max(res,w)
            d.add(s[r])
        return res