class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == '-':
            return False
        
        lo = 0
        hi = len(x) - 1
        if(hi + 1 == 1):
            return True
        if(hi + 1 == 0):
            return True
        if(hi + 1 < 0):
            return False
        while lo < hi:
            if x[lo] != x[hi]:
                return False
            lo += 1
            hi -=1
        return True