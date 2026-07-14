class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowel = {'a','e','i','o','u'}
        count = 0
        max_vowel = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
            max_vowel = max(max_vowel,count)
        for i in range(k,n):
            if s[i] in vowel:
                count += 1
            if s[i-k] in vowel:
                count -= 1
            max_vowel = max(max_vowel,count)
        return max_vowel