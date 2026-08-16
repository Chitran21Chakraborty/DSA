class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        n = len(nums)
        a = min(min_idx,max_idx)
        b = max(min_idx,max_idx)

        frm_left = b+1
        frm_right = n-a
        frm_both =(a+1)+(n-b)

        return min(frm_left,frm_right,frm_both)