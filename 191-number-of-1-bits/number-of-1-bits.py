class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = []
        while n>0:
            rem = n%2
            bin_num.append(str(rem))
            n = n//2
        count = 0
        for num in bin_num:
            if num == '1':
                count+=1
        return count