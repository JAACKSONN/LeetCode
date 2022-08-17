class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn nums into a set
        numsSet = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in numsSet:
                # This means that it is the beginning of a sequence
                length = 1
                while (num + length) in numsSet:
                    length += 1
                res = max(res, length)
        return res
    
        