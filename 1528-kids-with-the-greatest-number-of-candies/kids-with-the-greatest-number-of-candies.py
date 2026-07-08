class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        result = []
        n = len(candies)
        for i in range(n):
            max_candies = max(max_candies, candies[i])
        for i in range(n):
            result.append(candies[i] + extraCandies >= max_candies)
        return result
