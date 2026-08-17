class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rem = 0
        rev = 0
        sign = 0
        if x<0:
            return False
        else:
            while x>0:
                rem = x%10
                rev = rev*10+rem
                x = x//10
        if original == rev:
            return True
        else:
            return False