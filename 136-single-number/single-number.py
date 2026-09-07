class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rem = 0
        for num in nums:
            rem=rem^num
        return rem