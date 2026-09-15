class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l=0
        r=len(height)-1
        while l<r:
            heightt = min(height[l],height[r])
            width = r-l
            area = heightt*width
            maxWater = max(maxWater,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxWater
