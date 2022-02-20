class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        nums.sort()
        res = []
        l = 0
        r = length -1 
        
        while l < r:
            total = nums[l] + nums[r]
            
            if total  < target:
                l+=1
            elif total > target:
                r-= 1
            else:
                res.append(l)
                res.append(r)
                return res
        