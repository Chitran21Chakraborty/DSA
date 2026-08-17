class Solution:
    def reverse(self, x: int) -> int:
        # rem = 0
        # current = x
        # rev=  0
        # sign = 0
        # if x<0:
        #     sign=-1
        # else:
        #     sign = +1
        # x = abs(x)
        # while x>0:
        #     rem = x%10
        #     rev = rev*10+rem
        #     x = x//10
        # rev = sign*rev

        # if -2**31 <= rev < 2**31:
        #     return rev
        # else:
        #     return 0
        # x = -123
        # abs_x = 123
        # x_str = "123"
        # rev_x = "321"
        # int_x = 321

        abs_x = abs(x)
        x_str = str(abs_x)
        rev_x = x_str[::-1]
        int_x = int(rev_x)
        if x<0 and -2**31 <= int_x < 2**31:
            return -1*int_x
        elif x>0 and -2**31 <= int_x < 2**31:
            return int_x
        else:
            return 0

            
