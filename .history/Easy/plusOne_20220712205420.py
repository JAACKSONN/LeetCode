# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = 0

#         for i in range(len(digits)):
#     	    num += digits[i] * pow(10, (len(digits)-1-i))
            
#         return [int(i) for i in str(num+1)]
            
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n >= 0 and digits[n] == 9:
            digits[n] = 0
            n-=1
        if n == -1:
            digits.insert(0, 1)
        else:
            digits[n]+=1 
        
        return digits