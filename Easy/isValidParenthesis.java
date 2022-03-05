class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        aInt = 0;
        bInt = 0;
        for i in range(aLen):
            aInt += int(a[i]) * (2**(aLen - 1 - i))
        for i in range(bLen):
            bInt += int(b[i]) * (2**(bLen - 1 - i))
        result = aInt + bInt
        return format(result, "b")