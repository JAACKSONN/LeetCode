class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        
        for i in range (0, len(s)):
            
            # odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            if (r - l - 1) > len(res):
                res = s[l + 1 : r]
                
            # even palindrome
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            if (r - l - 1) > len(res):
                res = s[l + 1 : r]
        return res
            
        
