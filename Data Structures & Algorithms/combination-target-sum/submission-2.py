class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        temp = []
        self.curr_sum = 0
        nums.sort()

        def bk(sid):
            if self.curr_sum == target:
                combs.append(list(temp))
                return
            
            for i in range(sid, len(nums)):           
                if sum(temp) + nums[i] > target:
                    break
                else:
                    temp.append(nums[i])
                    self.curr_sum += nums[i]
                    bk(i)
                    temp.pop()
                    self.curr_sum -= nums[i]
        bk(0)

        return combs
                
                