class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # nums = [float('-inf')] + nums +[ float('-inf')]
        # for i in range(1,len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i-1
        # return 0

        l,r = 0,len(nums)-1
        while l<=r:
            m = l + ((r-l)//2)
            # left is greater
            if m>0 and nums[m] < nums[m-1]:
                r = m-1
            # right is greater
            elif m < len(nums)-1 and nums[m] < nums[m+1]:
                l = m+1
            else:
                return m

