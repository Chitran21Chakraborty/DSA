class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        maxEnding = nums[0]
        for i in range(1,len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            result = max(maxEnding,result)
        return result
        