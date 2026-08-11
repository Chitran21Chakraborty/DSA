class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        n = len(nums)
        a = min(min_idx,max_idx)
        b = max(min_idx,max_idx)

        from_left = b+1
        from_right = n-a
        from_both = (a+1)+(n-b)

        return min(from_left,from_right,from_both)