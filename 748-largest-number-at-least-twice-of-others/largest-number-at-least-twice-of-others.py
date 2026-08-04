class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxx = max(nums)
        idx = nums.index(maxx)
        for i in range(len(nums)):
            if i==idx:
                continue
            if maxx<2*nums[i]:
                return -1
        return idx