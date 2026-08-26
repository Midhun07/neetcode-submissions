class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we will begin with 2 pointers, shift the pointer to max element always
        # assign it to the mid of current 2 pointers and keep doing this until l>=r.

        l, r = 0, len(nums)-1
        mine = min(nums[l], nums[r])

        while l < r:
            mid = (l + r) // 2
            mine = min(mine, nums[mid])
            if nums[mid] <= nums[r] or nums[mid] <= nums[l]:
                r = mid
            elif nums[mid] >= nums[r] or nums[mid] >= nums[l]:
                l = mid
            else:
                pass

        return mine
        