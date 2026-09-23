class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = [[]]
        for i in nums:
            output += [lst + [i] for lst in output]
        return output