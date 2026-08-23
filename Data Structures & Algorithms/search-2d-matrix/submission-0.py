class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten the matrix to a list and do binary search
        flat = []
        for i in range(len(matrix)):
            flat.extend(matrix[i])

        l, r = 0, len(flat) - 1

        while l <= r:
            mid = (l + r) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False