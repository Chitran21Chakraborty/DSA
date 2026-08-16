class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_nums = [1]*n
        right_nums = [1]*n
        answer = [1]*n
        for i in range(1,n):
            left_nums[i] = left_nums[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right_nums[i] = right_nums[i+1]*nums[i+1]
        for i in range(n):
            answer[i]= left_nums[i]*right_nums[i]
        return answer



# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left = [1]*n
#         right = [1]*n
#         ans = [1]*n
#         for i in range(1,n):
#             left[i] = left[i-1]*nums[i-1]
#         for i in range(n-2,-1,-1):
#             right[i] = right[i+1]*nums[i+1]
#         for i in range(n):
#             ans[i] = left[i]* right[i]
#         return ans