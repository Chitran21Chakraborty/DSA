class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original = x
        rem = 0
        while x>0:
            digit =x% 10
            rem = rem*10+ digit
            x //=10
        return rem == original
        

