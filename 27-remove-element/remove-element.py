class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Input: nums = [2,2], val = 3
        # Output: 2, nums = [2,2,_,_]

        # Input: nums = [0,1,3,0,4], val = 2
        # Output: 5, nums = [0,1,4,0,3,_,_,_]
        j = 0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[i],nums[j] = nums[j], nums[i]
                j += 1
        return j
