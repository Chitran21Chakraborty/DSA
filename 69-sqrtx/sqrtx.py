# class Solution(object):
#     def mySqrt(self, x):
#         if x < 2:
#             return x
        
#         left, right = 1, x // 2
        
#         while left <= right:
#             mid = (left + right) // 2
#             square = mid * mid
            
#             if square == x:
#                 return mid
#             elif square < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return right 
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1,x+1):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1
        return 0