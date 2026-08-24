class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = float('inf')
        maxProf=0
        for price in prices:
            if price<minBuy:
                minBuy = price
            profit = price - minBuy
            if profit>maxProf:
                maxProf = profit
        return maxProf

