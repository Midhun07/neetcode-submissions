class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treating the values as indices we do a floyd's algo to find if cycle exists or not. start with 0,0. 
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the entrance to the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow