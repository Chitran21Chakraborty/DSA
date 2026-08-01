
class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        rev=0
        while (x>0) :
            rev=(rev*10)+x%10
            x=x//10
            
        if (org==rev) :
            return True
        return False
