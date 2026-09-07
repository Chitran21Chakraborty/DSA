class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            rem = n % 2               # Extract the last bit
            ans = (ans * 2) + rem     # Shift accumulated value left by multiplying by 2 and adding remainder
            n = n // 2                # Integer division by 2 to move to next bit
        return ans