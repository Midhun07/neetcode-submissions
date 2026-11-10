class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        temp = []
        nums.sort()

        def bk(sid):
            if sum(temp) == target:
                combs.append(list(temp))
            
            for i in range(sid, len(nums)):           
                if sum(temp) + nums[i] > target:
                    break
                else:
                    temp.append(nums[i])
                    bk(i)
                    temp.pop()
        bk(0)

        return combs
                
                