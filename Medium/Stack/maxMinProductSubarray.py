class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []
        prefix = [0]
        
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        for i in range(len(nums)):
            newStart = i
            while stack and stack[-1][1] > nums[i]:
                start, value = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, total * value)
                newStart = start
            stack.append((newStart, nums[i]))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, total * val)
            
        return res % (10**9 + 7)
            
                
        
        
        