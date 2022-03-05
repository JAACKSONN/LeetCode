class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x+1
        ans = 0
        
        while high>low:
            mid = (high+low)//2
            if mid*mid<=x:
                low = mid+1
                ans = mid
            else:
                high = mid
        return ans