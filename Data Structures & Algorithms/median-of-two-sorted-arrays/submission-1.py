class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        # 2. Binary search on number of elements taken from nums1: [0, m]
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2       # Cut in nums1
            j = total_left - i     # Cut in nums2

            # 3. Read boundary elements safely
            mal1 = nums1[i - 1] if i > 0 else -float('inf')
            mir1 = nums1[i] if i < m else float('inf')

            mal2 = nums2[j - 1] if j > 0 else -float('inf')
            mir2 = nums2[j] if j < n else float('inf')

            # 4. Partition verification
            if mal1 > mir2:
                # Took too many elements from nums1, move left
                r = i - 1
            elif mal2 > mir1:
                # Took too few elements from nums1, move right
                l = i + 1
            else:
                # Found valid partition
                if (m + n) % 2 == 1:
                    return float(max(mal1, mal2))
                else:
                    return (max(mal1, mal2) + min(mir1, mir2)) / 2.0