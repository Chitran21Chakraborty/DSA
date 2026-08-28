class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        minn = min(a,b)
        arr = []
        for i in range(minn):
            arr.append(i+1)
        print(arr)
        for num in arr:
            if a%num == 0 and b%num==0:
                count +=1
        return count