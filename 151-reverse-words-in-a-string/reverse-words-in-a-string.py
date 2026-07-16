class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        rev = s[::-1]
        return " ".join(rev)