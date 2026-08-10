# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         ans = []
#         for i in range(n):
#             if sum(int(digit) for digit in str(i)) % 3 == 0 and (i % 10 == 0 or i % 10 == 5):
#                 ans.append("FizzBuzz")
#             elif sum(int(digit) for digit in str(i)) % 3 == 0:
#                 ans.append("Fizz")
#             elif (i%10 == 0 or i%10 == 5):
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i+1))
#         return ",".join(ans)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i%15==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans