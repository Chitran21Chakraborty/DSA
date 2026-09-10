class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        original = x
        x= abs(x)
        rem =0
        while x>0:
            digit = x%10
            rem = rem*10+digit
            x //=10
        res = sign*rem
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res