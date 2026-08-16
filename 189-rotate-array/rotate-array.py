class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k%=n
        # nums = [1,2,3,4,5,6,7], k = 3
        # [7,6,5  ,4         ,3,2,1]
        # [5,6,7  ,4         ,3,2,1]
        # [7,6,5  ,1,2,3,4]
        
        # o/p1 -> [7,6,5,4,3,2,1] ''
        # o/p2 -> [5,6,7,4,3,2,1]
        # o/p3 -> [5,6,7,1,2,3,4]
        
        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
 