# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        # def inorder(node):
        #     return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        # return inorder(root)[k-1]
        
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k-=1
            if not k:
                return node.val
            root = node.right
                
            