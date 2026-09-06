class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        st = set()
        longest = 0 
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            w = r-l+1
            longest = max(longest,w)
            st.add(s[r])
        return longest