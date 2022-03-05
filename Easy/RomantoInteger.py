class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s) - 1
        count = 0
        mp = {}
        mp['I'] = 1
        mp['V'] = 5
        mp['X'] = 10
        mp['L'] = 50
        mp['C'] = 100
        mp['D'] = 500
        mp['M'] = 1000
        count += mp[s[n]]
        i = n
        
        while i > 0:
            charAt = mp[s[i]]
            charLeft = mp[s[i-1]]
            if charAt > charLeft:
                count-=charLeft
            else:
                count+= charLeft
            i-=1
                
        
        
        return count
                
        