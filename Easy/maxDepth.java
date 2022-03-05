/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int helper(TreeNode l, TreeNode r){
        if(l == null && r == null) return 1;
        else if(l == null) return 1 + helper(r.left, r.right);
        else if(r == null) return 1 + helper(l.left, l.right);
        return 1 + Math.max(helper(l.left, l.right), helper(r.left,r.right));
        
    }
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        return helper(root.left, root.right);
    }
}