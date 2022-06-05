class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            charS1 = s1[i]
            charS2 = s2[i]
            indexS1 = ord(charS1) - ord('a')
            indexS2 = ord(charS2) - ord('a')
            s1Count[indexS1] += 1
            s2Count[indexS2] += 1
        
        
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            s2Count[index] += 1
            
            if(s2Count[index] == s1Count[index]):
                matches += 1
            elif(s2Count[index] - 1 == s1Count[index]):
                matches -= 1
            
            index = ord(s2[i - len(s1)]) - ord('a')
            s2Count[index] -= 1
            
            if(s2Count[index] == s1Count[index]):
                matches += 1
            elif(s2Count[index] + 1 == s1Count[index]):
                matches -= 1
            
        return matches == 26
            
            