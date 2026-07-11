class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0
        max_avg = float('-inf')
        for i in range(k):
            curr_sum += nums[i]
        max_avg = max(max_avg, curr_sum/k)
        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            max_avg = max(max_avg,curr_sum/k)
        return max_avg
        