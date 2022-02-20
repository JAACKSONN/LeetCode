class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        array = s.split(" ")
        print(array)
        return len(array[len(array) - 1])
        