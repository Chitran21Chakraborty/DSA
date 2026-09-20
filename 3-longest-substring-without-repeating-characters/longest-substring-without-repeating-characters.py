class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = r-l+1
            maxLen = max(maxLen,w)
            sett.add(s[r])
        return maxLen
