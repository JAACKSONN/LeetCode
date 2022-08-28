class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(openCount, closedCount, curr):
            if openCount == n and closedCount == n:
                res.append(curr)
            elif openCount == n:
                helper(openCount, closedCount + 1, curr + ')')
            else:
                helper(openCount + 1, closedCount, curr + '(')
                if openCount > closedCount:
                    helper(openCount, closedCount + 1, curr + ')')
        helper(0, 0, '')
        return res
            