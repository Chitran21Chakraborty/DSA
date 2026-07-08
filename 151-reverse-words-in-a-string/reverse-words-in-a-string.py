class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # remove leading and traing zeros
        s = s.split() # create individual strings
        rev = s[::-1] # reverse the string's list
        return " ".join(rev)