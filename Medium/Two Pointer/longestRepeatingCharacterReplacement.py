class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = 0
        res = 0
        
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(count[s[r]], maxFreq)
            
            if (r - l + 1 - maxFreq <= k ):
                res = max(r - l + 1, res)
            else:
                count[s[l]] -= 1
                l += 1
        return res