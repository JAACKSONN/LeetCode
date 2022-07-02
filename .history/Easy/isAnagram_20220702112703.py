class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = [0] * 26
        tCount = [0] * 26
        
        for i in range(len(s)):
            indexS = ord(s[i]) - ord('a')
            indexT = ord(t[i]) - ord('a')
            sCount[indexS] += 1
            tCount[indexT] += 1
        
        for i in range(26):
            if sCount[i] != tCount[i]:
                return False
        
        return True