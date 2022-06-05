class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
    
        res = []
        sCount = [0] * 26
        pCount = [0] * 26
        
        for i in range (len(p)):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1
        
        matches = 0
        
        for i in range (26):
            if pCount[i] == sCount[i]:
                matches += 1
        l = 0     
        for r in range (len(p), len(s)):
            if matches == 26:
                res.append(l)
            
            index = ord(s[r]) - ord('a')
            sCount[index] += 1
            if sCount[index] == pCount[index]:
                matches += 1
            elif sCount[index] - 1 == pCount[index]:
                matches -= 1
            
            index = ord(s[l]) - ord('a')
            sCount[index] -= 1
            if sCount[index] == pCount[index]:
                matches += 1
            elif sCount[index] + 1 == pCount[index]:
                matches -= 1
            l += 1
            
        if matches == 26: 
            res.append(l)
        return res
            