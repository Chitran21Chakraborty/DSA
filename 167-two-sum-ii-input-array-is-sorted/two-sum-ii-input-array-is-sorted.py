class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}
        # for i,num in enumerate(numbers):
        #     complement = target-num
        #     if complement in seen:
        #         return [seen[complement]+1,i+1]
        #     seen[num] = i

        left, right = 0,len(numbers)-1
        while left<right:
            curSum = numbers[left]+numbers[right]

            if curSum == target:
                return [left+1,right+1]
            elif curSum < target:
                left+=1
            else:
                right-=1 