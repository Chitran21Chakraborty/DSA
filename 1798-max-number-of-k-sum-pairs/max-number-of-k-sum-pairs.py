class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # max_count = 0
        # needed = []
        # for i in range(len(nums)):
        #     rem = k - nums[i]
        #     needed.append(rem)
        #     nums.pop(nums[i])
        #     if needed in nums:
        #         max_count += 1
        # return max_count
        nums.sort()
        left = 0
        right = len(nums)-1
        max_count = 0
        while left<right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                max_count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return max_count

