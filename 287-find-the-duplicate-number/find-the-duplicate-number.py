# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # nums_set = set(nums)
#         # set_sum = sum(nums_set)
#         # act_sum = sum(nums)
#         # diff = act_sum - set_sum
#         # return diff

#         seen = {}
#         for i in range(len(nums)):
#             if nums[i] in seen:
#                 nums[i] +=1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            