class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # summ = 0
        # sub = 0
        # for i in range(len(nums)):
        #     summ += nums[i]
        #     if summ == k:
        #         sub += 1
        #         summ = 0
        #         i -= 1
        # return sub
        # count = 0
        # sums = 0
        # d = dict()
        # d[0] = 1
        # # d = { 0:1}
        # for i in range(len(nums)):
        #     sums += nums[i]
        #     count += d.get(sums-k,0)
        #     d[sums] = d.get(sums,0) + 1
        # return count


        count = 0
        sums = 0
        d= dict()
        d[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        return count
        