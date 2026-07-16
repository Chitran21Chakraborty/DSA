from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)

        # k  v
        # 3: 2
        # 2: 1