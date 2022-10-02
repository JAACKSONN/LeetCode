class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        ans = ""
        
        while num:
            div = num // nums[i]
            num %= nums[i]
  
            while div:
                ans += sym[i]
                div -= 1
            i -= 1
        return ans
        