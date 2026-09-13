class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0 
        end = len(nums)-1
        while beg < end:
            mid = beg + ((end - beg)//2)
            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[beg]:
                if nums[beg] <= target <= nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            else:
                if nums[mid]<=target<=nums[end]:
                    beg = mid+1
                else:
                    end = mid-1
        return -1 if nums[end]!= target else end