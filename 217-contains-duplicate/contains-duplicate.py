class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_num_set=len(set(nums))
        len_nums = len(nums)
        if len_num_set == len_nums:
            return False
        return True
