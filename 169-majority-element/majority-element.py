# from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        votes = 1
        for i in range(1,len(nums)):
            if votes == 0:
                majority = nums[i]
                votes += 1
            elif (majority == nums[i]):
                votes += 1
            else:
                votes -= 1
        return majority
#         count = Counter(nums)
#         return max(count, key = count.get)


#Boyer-Moore Voting Algorithm


 