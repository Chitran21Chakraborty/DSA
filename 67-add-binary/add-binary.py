class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_bin= int(a,2)
        b_bin = int(b,2)
        summ = a_bin+b_bin
        binn = bin(summ)[2:]
        return binn