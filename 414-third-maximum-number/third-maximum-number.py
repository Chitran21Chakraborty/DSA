class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -inf
        for i in range(len(nums)):
            if(nums[i] > max1):
                max1, max2, max3 = nums[i], max1, max2
            elif(nums[i] > max2 and nums[i] != max1):
                max3 = max2
                max2 = nums[i]
            elif(nums[i] > max3 and nums[i] != max1 and nums[i] != max2):
                max3 = nums[i]
        return max3 if max3 != float("-inf") else max1
        



