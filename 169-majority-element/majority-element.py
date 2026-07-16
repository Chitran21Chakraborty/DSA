from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return max(count, key=count.get)

        element = None
        count = 0
        for num in nums:
            if count == 0:
                element = num
            count += 1 if element == num else -1
        return element

