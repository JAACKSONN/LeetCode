class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = Counter(s)
        left = set(s[0])
        res = set()
        right[s[0]] -= 1
        for mid in range(1, len(s) - 1):
            right[s[mid]] -= 1
            for j in range(26):
                char = chr(ord('a') + j)
                if char in right and right[char] > 0 and char in left:
                    res.add((s[mid], char))
            left.add(s[mid])
        return len(res)