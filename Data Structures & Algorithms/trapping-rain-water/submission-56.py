class Solution:
    # the intuition is the we count the number of water above each column
    # the water stored above each column depends on the min(max(left_heights), max(right_height))
    # Basically the min of the tallest columns enclosing it
    # If left is smaller to right then take max(left_max, height[i]) move inwards else vice-a-versa
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        sum_water = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                sum_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                sum_water += right_max - height[r]
        
        return sum_water