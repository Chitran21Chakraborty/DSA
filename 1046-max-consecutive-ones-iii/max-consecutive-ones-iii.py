class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_zeros = 0
        max_length = 0
        left = 0
        for right in range(n):
                if nums[right] == 0:
                    num_zeros += 1
                while num_zeros > k:
                    if nums[left] == 0:
                        num_zeros -= 1
                    left += 1
                max_length = max(max_length, right - left + 1)
        return max_length


