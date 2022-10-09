class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return []
        countP = [0] * 26
        countS = [0] * 26
    
        for i in range(len(p)):
            countP[ord(p[i]) - ord('a')] += 1
            countS[ord(s[i]) - ord('a')] += 1
        
        
        matches = 0
        for i in range(26):
            if countP[i] == countS[i]:
                matches += 1
        l = 0
        for r in range(len(p), len(s)):
            if matches == 26:
                res.append(l)
            
            index = ord(s[l]) - ord('a')
            countS[index] -= 1
            
            if countS[index] == countP[index]:
                matches += 1
            elif countS[index] + 1 == countP[index]:
                matches -= 1
            
            index = ord(s[r]) - ord('a')
            countS[index] += 1
            
            if countS[index] == countP[index]:
                matches += 1
            elif countS[index] - 1 == countP[index]:
                matches -= 1
            
            l+=1
        if matches == 26:
            res.append(len(s) - len(p))
        return res