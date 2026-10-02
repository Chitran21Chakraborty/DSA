class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,num in enumerate(nums):
            complement = target- num
            if complement in seen:
                return [i,seen[complement]]
            seen[num] = i
            