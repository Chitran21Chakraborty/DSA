class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # l = m -1
        # r = n -1
        # s = m+n-1
        # while l<r:
        #     if nums2[r] > nums1[l]:
        #         nums1[s] = nums2[r]
        #         s -=1
        #         r -=1
        #     else:
        #         nums1[s] = nums1[l]
        #         l -=1
        #         s -=1

        # last index of nums1
        last = m+n-1
        #merge in reverse order
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
            else:
                nums1[last] = nums2[n-1]
                n -=1
            last -=1
        #fill nums1 with leftover nums2 elements 
        while n>0:
            nums1[last] = nums2[n-1]
            n -=1
            last -=1



        
        