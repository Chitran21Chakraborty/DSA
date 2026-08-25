class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        l = m+n-1
        while p>=0 and q>=0:
            if nums2[q] > nums1[p]:
                nums1[l] = nums2[q]
                q -=1
            else:
                nums1[l] = nums1[p]
                p-=1
            l -=1
        while q>=0:
            nums1[l] = nums2[q]
            q -=1
            l-=1
        