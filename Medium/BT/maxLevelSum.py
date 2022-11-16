# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1 
        globalMax = root.val
        currLevel = 2
        
        deq = deque()
        
        if root.left:
            deq.append(root.left)
        if root.right:
            deq.append(root.right)
        
        while deq:
            curSum = 0
            for i in range(len(deq)):
                node = deq.popleft()
                curSum += node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            if curSum > globalMax:
                level = currLevel
                globalMax= curSum
            currLevel += 1
        return level
            
        