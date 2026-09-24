class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_splitted = text.split()
        broken_set = set(brokenLetters)
        n = len(text_splitted)
        for s in text_splitted:
            if any(char in brokenLetters for char in s):
                n-=1
        return n
                