class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1 = nums[0] * count[nums[0]]
        if len(nums) == 1:
            return earn1
        if nums[1] == nums[0] + 1:
            earn2 = max(earn1, nums[1] * count[nums[1]])
        else:
            earn2 = earn1 + nums[1] * count[nums[1]]
        
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                earn1, earn2 = earn2, max(earn1 + nums[i] * count[nums[i]], earn2)
            else:
                earn1, earn2 = earn2, earn2 + nums[i] * count[nums[i]]
        return earn2