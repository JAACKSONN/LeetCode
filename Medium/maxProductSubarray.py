class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num == 0:
                res = max(0, res)
                curMax, curMin = 1, 1
                continue
                
            curMax, curMin = max(curMax * num, curMin * num, num), min(curMin * num, curMax * num, num)
            res = max(curMax, res)
            
        return res
            