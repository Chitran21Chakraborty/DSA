class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = n*(n+1)/2
        nums_sum = sum(nums)
        diff = actual_sum - nums_sum
        return int(diff)