class Solution:
    def validMountainArray(self, arr):
        n = len(arr)

        if n < 3:
            return False

        i = 0

        # Go uphill
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False

        # Go downhill
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # Must reach the end
        return i == n - 1