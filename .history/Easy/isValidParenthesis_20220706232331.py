class Solution:
    def isValid(self, s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for char in s:
            if char not in Map:
                stack.append(char)
            else:
                if not stack or stack.pop() != Map[char]:
                    return False
                
        return not stack