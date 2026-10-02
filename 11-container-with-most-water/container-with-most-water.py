class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0
        while l<r:
            heightt = min(height[r],height[l])
            width =  r-l
            area = heightt * width
            maxWater = max(maxWater, area)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return maxWater