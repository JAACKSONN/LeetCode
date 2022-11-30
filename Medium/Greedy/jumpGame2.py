class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = 0
        
        while r < len(nums) - 1:
            farthestIndex = 0
            for i in range(l, r + 1):
                farthestIndex = max(farthestIndex, i + nums[i])
            l = r + 1
            r = farthestIndex
            res += 1
        return res
            