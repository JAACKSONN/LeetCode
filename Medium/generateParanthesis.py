class Solution: 
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(res, s, o, c, n):
            if o == n and c == n:
                res.append(s)
                return
            if o < n:
                helper(res, s + "(", o + 1, c, n)
            if c < o:
                helper(res, s + ")", o, c + 1, n)
        helper(res, "", 0, 0, n)
        return res
    
        
        
        
        
        
        
        
        
        