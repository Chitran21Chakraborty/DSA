class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. strip , 2. split 3. reverse 4.join
        s = s.strip()
        # "hello world"
        s = s.split()
        # "hello", "world"
        rev = s[::-1]
        # "world","hello"
        return " ".join(rev)



