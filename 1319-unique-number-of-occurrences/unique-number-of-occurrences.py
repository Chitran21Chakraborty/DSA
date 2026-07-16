from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        occur = list(count.values())
        return len(occur) == len(set(occur))
        # 1:3
        # 2:2
        # 3:1
        