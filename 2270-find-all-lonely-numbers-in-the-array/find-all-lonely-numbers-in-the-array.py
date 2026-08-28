class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        res = []
        for num in nums:
            if freq[num] == 1 and (num-1) not in freq and (num+1) not in freq:
                res.append(num)
        return res