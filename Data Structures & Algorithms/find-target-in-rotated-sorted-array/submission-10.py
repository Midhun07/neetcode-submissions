class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we keep l, r as two end pointers. We keep finding mid. If the target is
        # >mid and <r then l=mid else r=mid-1
        l, r = 0, len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[r]:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
        
        return -1
        