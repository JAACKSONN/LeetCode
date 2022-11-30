class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rowDist = (numRows - 1) * 2
        res = ""
        
        index = 0
        while index < len(s):
            res += s[index]
            index += rowDist
        
        for i in range(1, numRows - 1):
            index = i
            while index < len(s):
                res += s[index]
                index += rowDist
                if (index - (2 * i) < len(s)):
                    res += s[index - (2 * i)]
        
        index = numRows - 1
        while index < len(s):
            res += s[index]
            index += rowDist
        
        
        
        return res