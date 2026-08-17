class Solution:
    def reverse(self, x: int) -> int:
        rem = 0
        current = x
        rev=  0
        sign = 0
        if x<0:
            sign=-1
        else:
            sign = +1
        x = abs(x)
        while x>0:
            rem = x%10
            rev = rev*10+rem
            x = x//10
        rev = sign*rev

        if -2**31 <= rev < 2**31:
            return rev
        else:
            return 0
            
