# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count


    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val
# class Solution:
#     def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         count = 0
#         def dfs(node):
#             nonlocal count
#             if not node:
#                 return True
#             if not node.left and not node.right:
#                 count += 1
#                 return True
            
#             left = dfs(node.left)
#             right = dfs(node.right)
            
#             if left and right and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
#                 count += 1
#                 return True
            
#             return False
#         dfs(root)
#         return count
            
            