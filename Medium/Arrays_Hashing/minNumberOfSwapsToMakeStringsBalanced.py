class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0 
        res = 0
        
        for char in s:
            if char == ']':
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return (res + 1) // 2