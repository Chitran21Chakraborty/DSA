class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # try code
        # l = 0
        # for r in range(len(nums)):
        #     if (nums[l] != nums[r]) and (nums[l] == 0):
        #         nums[l] = nums[r]
        #         nums[r] = 0
        #         l += 1
        #     r += 1
        # return nums

        # correct
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l] , nums[r]
                l += 1
        return nums

        