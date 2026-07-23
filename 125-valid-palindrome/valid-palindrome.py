class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]","",s).strip().lower()

        #s = re.sub(r"[^a-zA-Z0-9]", "",s).lower().strip()
        s_rev = s[::-1]
        if s == s_rev:
            return True
        return False
