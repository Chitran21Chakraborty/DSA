from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        sorted_keys = sorted(freq.keys())
        
        n = len(sorted_keys)
        for i in range(n):
            x = sorted_keys[i]
            for j in range(i + 1, n):
                y = sorted_keys[j]
                if freq[x] != freq[y]:
                    return [x, y]
                    
        return [-1, -1]