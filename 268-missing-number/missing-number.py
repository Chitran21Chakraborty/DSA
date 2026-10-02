class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        given_sum = sum(nums)
        actual_sum = n*(n+1)//2
        diff = actual_sum - given_sum
        return diff