class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median always occurs in the middle of the list
        # if list is N then median is N/2 if N is odd else (N + N + 1) / 2

        # find the total length of the combined array, is it odd or even?
        # Begin with the smaller array so prevent out of bound
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)

        hl = (m + n + 1) // 2

        l, r = 0, len(nums1)

        while l <= r:
            i = (l + r) // 2
            j = hl - i
            mal1, mir1 = nums1[i-1] if i>0 else -float('inf'), nums1[i] if i<m else float('inf')
            mal2, mir2 = nums2[j-1] if j>0 else -float('inf'), nums2[j] if j<n else float('inf')

            if mal1 > mir2: # too many elements from left
                r = i - 1
            elif mal2 > mir1: # too many elements from right
                l = i + 1
            else:
                if (m + n) % 2 == 1:
                    return float(max(mal1, mal2))
                else:
                    return (max(mal1, mal2) + min(mir1, mir2)) / 2.0