class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        arr = [0]*101
        for log in logs:
            by = log[0]
            dy = log[1]
            arr[by-1950]+=1
            arr[dy-1950]-=1
        max_pop =arr[0]
        maxYear = 1950
        for i in range(1,101):
            arr[i]+=arr[i-1]
            if max_pop < arr[i]:
                max_pop = arr[i]
                maxYear =i+1950
        return maxYear