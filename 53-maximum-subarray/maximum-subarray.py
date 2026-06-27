class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # result = nums[0]
        # maxEnding = nums[0]
        # for i in range(1,len(nums)):
        #     maxEnding = max(maxEnding + nums[i], nums[i])
        #     result = max(maxEnding,result)
        # return result

        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub,curSum)
        return maxSub
        